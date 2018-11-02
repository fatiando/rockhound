"""
Functions for loading and downloading models.

Uses Pooch to manage the downloads. Available models (including hashes and urls) are in
the rockhound/registry.txt file.
"""
import os
import gzip
import tempfile
import shutil

import pooch
import xarray as xr


POOCH = pooch.create(
    path=["~", ".rockhound", "data"], base_url="", env="ROCKHOUND_DATA_DIR"
)
POOCH.load_registry(os.path.join(os.path.dirname(__file__), "registry.txt"))


def fetch_etopo1(version, load=True):
    """
    Fetch the ETOPO1 global relief model.

    ETOPO1 is a 1 arc-minute global relief model of Earth's surface that integrates land
    topography and ocean bathymetry [AmanteEakins2009]_. It's available in two versions:
    "Ice Surface" (top of Antarctic and Greenland ice sheets) and "Bedrock" (base of the
    ice sheets).

    The grid is loaded into an :class:`xarray.Dataset` and the coordinates are grid-line
    registered.

    If the file isn't already in your data directory, it will be downloaded
    automatically (which may take a while).

    Parameters
    ----------
    version : str
        Which version of the dataset to load. Can be ``"ice"`` for the ice surface
        version or ``'bedrock'`` for the bedrock version.
    load : bool
        Wether to load the data into an :class:`xarray.Dataset` or just return the path
        to the downloaded data.

    Returns
    -------
    grid : :class:`xarray.Dataset` or str
        The loaded grid or the file path to the downloaded data.

    """
    version = version.lower()
    versions = {
        "ice": "ETOPO1_Ice_g_gmt4.grd.gz",
        "bedrock": "ETOPO1_Bed_g_gmt4.grd.gz",
    }
    if version not in versions:
        raise ValueError("Invalid ETOPO1 version '{}'.".format(version))
    fname = POOCH.fetch(versions[version])
    if not load:
        return fname
    with tempfile.NamedTemporaryFile() as temporary:
        # Decompress the file into a temporary file so we can load it with xarray
        with gzip.open(fname) as unzipped:
            shutil.copyfileobj(unzipped, temporary)
        grid = xr.open_dataarray(temporary.name)
    # Add more metadata and fix some names
    names = {"ice": "Ice Surface", "bedrock": "Bedrock"}
    grid.name = "relief"
    grid.attrs["long_name"] = "ETOPO1 {} relief [meters]".format(names[version])
    grid = grid.rename(x="longitude", y="latitude")
    return grid
