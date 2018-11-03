"""
Load the ETOPO1 Earth Relief dataset.
"""
import gzip
import tempfile
import shutil

import xarray as xr

from .registry import REGISTRY


def fetch_etopo1(version, load=True):
    """
    Fetch the ETOPO1 global relief model.

    ETOPO1 is a 1 arc-minute global relief model of Earth's surface that integrates land
    topography and ocean bathymetry [AmanteEakins2009]_. It's available in two versions:
    "Ice Surface" (top of Antarctic and Greenland ice sheets) and "Bedrock" (base of the
    ice sheets). You can optionally load both into a single dataset.

    The grid is loaded into an :class:`xarray.Dataset` and the coordinates are
    grid-line registered.

    If the files aren't already in your data directory, it will be downloaded
    automatically (which may take a while).

    Parameters
    ----------
    version : str
        Which version of the dataset to load. Can be ``"ice"`` for the ice surface
        version, ``'bedrock'`` for the bedrock version.
    load : bool
        Wether to load the data into an :class:`xarray.Dataset` or just return the
        path to the downloaded data.

    Returns
    -------
    grid : :class:`xarray.Dataset` or str
        The loaded grid(s) or the file path(s) to the downloaded data.

    """
    version = version.lower()
    available = {
        "ice": "ETOPO1_Ice_g_gmt4.grd.gz",
        "bedrock": "ETOPO1_Bed_g_gmt4.grd.gz",
    }
    if version not in available:
        raise ValueError("Invalid ETOPO1 version '{}'.".format(version))
    fname = REGISTRY.fetch(available[version])
    if not load:
        return fname
    with tempfile.NamedTemporaryFile() as temporary:
        # Decompress the file into a temporary file so we can load it with xarray
        with gzip.open(fname) as unzipped:
            shutil.copyfileobj(unzipped, temporary)
        grid = xr.open_dataset(temporary.name)
    # Add more metadata and fix some names
    names = {"ice": "Ice Surface", "bedrock": "Bedrock"}
    grid = grid.rename(z=version, x="longitude", y="latitude")
    grid[version].attrs["long_name"] = "ETOPO1 {} relief [meters]".format(names[version])
    grid.attrs["title"] = grid[version].attrs["long_name"]
    return grid
