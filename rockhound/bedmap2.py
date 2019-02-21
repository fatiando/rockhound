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


def fetch_bedmap2(datasets=DATASETS, load=True):
    """
    Fetch the Bedmap2 datasets for Antarctica.

    Bedmap2 is a suite of gridded products describing surface elevation,
    ice-thickness, the sea ﬂoor and subglacial bed elevation of the Antarctic south
    of 60°S [BEDMAP2]_.
    The datasets are downloaded as `tiff` files and loaded into
    :class:`xarray.Dataset`s.

    Each dataset is projected in Antarctic Polar Stereographic projection, latitude of
    true scale -71 degrees south, datum WGS84.  All heights are in metres relative to
    sea level as defined by the g104c geoid.

    Parameters
    ----------
    datasets : list
        Datasets that wants to be loaded from the Bedmap2 model.
        The available datasets are: `bed`, `surface`, `thickness`,
        `icemask_grounded_and_shelves`, `rockmask`, `lakemask_vostok`,
        `bed_uncertainty`, `thickness_uncertainty_5km`, `data_coverage` and
        `geoid`. For more information read the `bedmap2_readme.txt` file.
    load : bool
        Wether to load the data into an :class:`xarray.Dataset` or just return the
        path to the downloaded data.

    Returns
    -------
    ds : :class:`xarray.Dataset`
        The loaded Bedmap2 datasets.
    """
    for dataset in datasets:
        if dataset not in DATASETS:
            raise IOError("Dataset {} not found in bedmap2_tiff.zip".format(dataset))
    available_datasets = dict(
        zip(DATASETS, ["bedmap2_{}.tif".format(dataset) for dataset in DATASETS])
    )
    available_datasets["geoid"] = "gl04c_geiod_to_WGS84.tif"
    fname = REGISTRY.fetch("bedmap2_tiff.zip")
    if not load:
        return fname

    arrays = []
    for dataset in datasets:
        with tempfile.TemporaryDirectory() as tempdir:
            # Decompress the file into a temporary file so we can load it with xr
            # The .tif files inside the zip are located inside a bedmap2_tiff directory
            with ZipFile(fname, 'r') as zip_file:
                zip_file.extract(
                    os.path.join("bedmap2_tiff", available_datasets[dataset]),
                    path=tempdir
                )
            array = xr.open_rasterio(
                os.path.join(tempdir, "bedmap2_tiff", available_datasets[dataset])
            )
            array.name = dataset
            arrays.append(array)
    ds = xr.merge(arrays)
    return ds
