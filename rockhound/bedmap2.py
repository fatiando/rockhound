"""
Load the Bedmap2 datasets for Antarctica.
"""
import os

import xarray as xr
from pooch import Unzip

from .registry import REGISTRY

DATASETS = {
    "bed": dict(name="Bedrock Height", units="meters"),
    "surface": dict(name="Ice Surface Height", units="meters"),
    "thickness": dict(name="Ice Thickness", units="meters"),
    "icemask_grounded_and_shelves": dict(
        name="Mask of Grounding Line and Floating Ice Shelves"
    ),
    "rockmask": dict(name="Mask of Rock Outcrops"),
    "lakemask_vostok": dict(name="Mask for Lake Vostok"),
    "grounded_bed_uncertainty": dict(name="Ice Bed Uncertainty", units="meters"),
    "thickness_uncertainty_5km": dict(name="Ice Thickness Uncertainty", units="meters"),
    "coverage": dict(name="Distribution of Ice Thickness Data (binary)"),
    "geoid": dict(name="Geoid Height (WGS84)", units="meters"),
}


def fetch_bedmap2(datasets, *, load=True):
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
        path to the downloaded data tiff files. If False, will return a list with the
        paths to the files corresponding to *datasets*.

    Returns
    -------
    grid : :class:`xarray.Dataset`
        The loaded Bedmap2 datasets.

    """
    if isinstance(datasets, str):
        datasets = [datasets]
    if not set(datasets).issubset(DATASETS.keys()):
        raise ValueError(
            "Invalid datasets: {}".format(set(datasets).difference(DATASETS.keys()))
        )
    fnames = REGISTRY.fetch("bedmap2_tiff.zip", processor=Unzip())
    if not load:
        return [get_fname(dataset, fnames) for dataset in datasets]
    arrays = []
    for dataset in datasets:
        array = xr.open_rasterio(get_fname(dataset, fnames))
        # Replace no data values with nans
        array = array.where(array != array.nodatavals)
        # Remove "band" dimension and coordinate
        array = array.squeeze("band", drop=True)
        array.name = dataset
        array.x.attrs["units"] = "meters"
        array.y.attrs["units"] = "meters"
        array.attrs["long_name"] = DATASETS[dataset]["name"]
        if "units" in DATASETS[dataset]:
            array.attrs["units"] = DATASETS[dataset]["units"]
        arrays.append(array)
    grid = xr.merge(arrays)
    grid.attrs.update(
        {
            "title": "Bedmap2",
            "projection": "Antarctic Polar Stereographic",
            "true_scale_latitude": -71,
            "datum": "WGS84",
            "EPSG": "3031",
            "doi": "10.5194/tc-7-375-2013",
        }
    )
    return grid


def get_fname(dataset, fnames):
    "Return the file name corresponding to the given dataset"
    if dataset == "geoid":
        dataset_name = "gl04c_geiod_to_WGS84.tif"
    else:
        dataset_name = "bedmap2_{}.tif".format(dataset)
    result = None
    for fname in fnames:
        if os.path.basename(fname) == dataset_name:
            result = fname
    return result
