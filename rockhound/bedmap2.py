"""
Load the Bedmap2 datasets for Antarctica.
"""
import os
import tempfile
from zipfile import ZipFile

import xarray as xr
from pooch import Unzip

from .registry import REGISTRY

DATASETS = [
    "bed",
    "surface",
    "thickness",
    "icemask_grounded_and_shelves",
    "rockmask",
    "lakemask_vostok",
    "grounded_bed_uncertainty",
    "thickness_uncertainty_5km",
    "coverage",
    "geoid",
]
DATASET_FILES = {dataset: "bedmap2_{}.tif".format(dataset) for dataset in DATASETS}
DATASET_FILES["geoid"] = "gl04c_geiod_to_WGS84.tif"


def fetch_bedmap2(datasets, load=True):
    """
    Fetch the Bedmap2 datasets for Antarctica.

    Bedmap2 is a suite of gridded products describing surface elevation,
    ice-thickness, the sea floor and subglacial bed elevation of the Antarctic south
    of 60°S [BEDMAP2]_.
    The datasets are downloaded as ``tiff`` files and loaded into a
    :class:`xarray.Dataset` object.

    Each dataset is projected in Antarctic Polar Stereographic projection, latitude of
    true scale -71 degrees south, datum WGS84. All heights are in metres relative to
    sea level as defined by the g104c geoid.

    The available datasets are:

    - ``bed``: bedrock height
    - ``surface``: ice surface height
    - ``thickness``: ice thickness
    - ``icemask_grounded_and_shelves``: mask showing the grounding line and the extent
      of the floating ice shelves
    - ``rockmask``: mask showing rock outcrops
    - ``lakemask_vostok``: mask showing the extent of the lake cavity of Lake Vostok
    - ``grounded_bed_uncertainty``: ice bed uncertainty grid
    - ``thickness_uncertainty_5km``: ice thickness uncertainty grid
    - ``coverage``: binary grid showing the distribution of ice thickness data used
      in the grid of ice thickness
    - ``geoid``: values to convert from heights relative to WGS84 datum to heights
      relative to EIGEN-GL04C geoid (to convert back to WGS84, add this grid)

    .. warning ::
        Loading a great number of datasets may require a fair amount of memory that
        could crash your system. We recommend loading only the needed datasets.

    .. warning ::
        Loading any dataset along with ``thickness_uncertainty_5km`` would modify the
        shape of the ``grid`` because it's defined on a different set of points.

    Parameters
    ----------
    datasets : list or str
        Names of the datasets that will be loaded from the Bedmap2 model.
    load : bool
        Wether to load the data into an :class:`xarray.Dataset` or just return the
        path to the downloaded data in a tiff file.
        If False, the *datasets* argument is ignored.

    Returns
    -------
    grid : :class:`xarray.Dataset`
        The loaded Bedmap2 datasets.
    """
    if not load:
        return REGISTRY.fetch("bedmap2_tiff.zip")
    fnames = REGISTRY.fetch("bedmap2_tiff.zip", processor=Unzip())
    if isinstance(datasets, str):
        datasets = [datasets]
    if not set(datasets).issubset(DATASETS):
        raise ValueError(
            "Invalid datasets: {}".format(set(datasets).difference(DATASETS))
        )
    arrays = []
    for dataset in datasets:
        for fname in fnames:
            if fname.endswith(DATASET_FILES[dataset]):
                array = xr.open_rasterio(fname)
                # Replace no data values with nans
                array = array.where(array != array.nodatavals)
                # Remove "band" dimension and coordinate
                array = array.squeeze("band", drop=True)
                array.name = dataset
                arrays.append(array)
    grid = xr.merge(arrays)
    grid.attrs = {
        "projection": "Antarctic Polar Stereographic",
        "true_scale_latitude": -71,
        "datum": "WGS84",
        "EPSG": "3031",
    }
    return grid
