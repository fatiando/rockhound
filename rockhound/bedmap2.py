"""
Load the Bedmap2 datasets for Antarctica.
"""
import os
import tempfile
from zipfile import ZipFile

import xarray as xr

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


def fetch_bedmap2(datasets, load=True):
    """
    Fetch the Bedmap2 datasets for Antarctica.

    Bedmap2 is a suite of gridded products describing surface elevation,
    ice-thickness, the sea ﬂoor and subglacial bed elevation of the Antarctic south
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

    Parameters
    ----------
    datasets : list
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
    fname = REGISTRY.fetch("bedmap2_tiff.zip")
    if not load:
        return fname

    if not set(datasets).issubset(DATASETS):
        raise ValueError(
            "Invalid datasets: {}".format(set(datasets).difference(DATASETS))
        )
    available_datasets = {
        dataset: "bedmap2_{}.tif".format(dataset) for dataset in DATASETS
    }
    available_datasets["geoid"] = "gl04c_geiod_to_WGS84.tif"
    for i, dataset in enumerate(datasets):
        with tempfile.TemporaryDirectory() as tempdir:
            # Decompress the file into a temporary file so we can load it with xr
            # The .tif files inside the zip are located inside a bedmap2_tiff directory
            with ZipFile(fname, "r") as zip_file:
                zip_file.extract(
                    os.path.join("bedmap2_tiff", available_datasets[dataset]),
                    path=tempdir,
                )
            array = xr.open_rasterio(
                os.path.join(tempdir, "bedmap2_tiff", available_datasets[dataset])
            )
            # Replace no data values with nans
            array = array.where(array != array.nodatavals)
            # Remove "band" dimension and coordinate
            array = array.squeeze("band", drop=True)
            array.name = dataset
            if i == 0:
                grid = array.to_dataset()
            else:
                grid = xr.merge([grid, array])
    return grid
