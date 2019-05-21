"""
Load the ETOPO1 Earth Relief dataset.
"""
import xarray as xr
from pooch import Decompress

from .registry import REGISTRY


def fetch_etopo1(version, *, load=True, **kwargs):
    """
    Fetch the ETOPO1 global relief model.

    ETOPO1 is a 1 arc-minute global relief model of Earth's surface that integrates land
    topography and ocean bathymetry [AmanteEakins2009]_. It's available in two versions:
    "Ice Surface" (top of Antarctic and Greenland ice sheets) and "Bedrock" (base of the
    ice sheets). Each grid is in a separate gzipped netCDF file (grid-line registered
    version). The grids are loaded into :class:`xarray.Dataset` objects.

    The vertical datum is sea level and the horizontal reference is the WGS84 ellipsoid.

    If the files aren't already in your data directory, they will be downloaded
    automatically (which may take a while). Each grid is approximately 380Mb.

    Parameters
    ----------
    version : str
        Which version of the dataset to load. Can be ``"ice"`` for the ice surface
        version, ``'bedrock'`` for the bedrock version.
    load : bool
        Wether to load the data into an :class:`xarray.Dataset` or just return the
        path to the downloaded data.
    kwargs
        Keyword arguments will be forwarded to the :func:`xarray.open_dataset` function
        that loads the grid into memory.

    Returns
    -------
    grid : :class:`xarray.Dataset` or str
        The loaded grid or the file path to the downloaded data.

    """
    version = version.lower()
    available = {
        "ice": "ETOPO1_Ice_g_gmt4.grd.gz",
        "bedrock": "ETOPO1_Bed_g_gmt4.grd.gz",
    }
    if version not in available:
        raise ValueError("Invalid ETOPO1 version '{}'.".format(version))
    fname = REGISTRY.fetch(available[version], processor=Decompress())
    if not load:
        return fname
    grid = xr.open_dataset(fname, **kwargs)
    # Add more metadata and fix some names
    names = {"ice": "Ice Surface", "bedrock": "Bedrock"}
    grid = grid.rename(z=version, x="longitude", y="latitude")
    grid[version].attrs["long_name"] = "{} relief".format(names[version])
    grid[version].attrs["units"] = "meters"
    grid[version].attrs["vertical_datum"] = "sea level"
    grid[version].attrs["datum"] = "WGS84"
    grid.attrs["title"] = "ETOPO1 {} Relief".format(names[version])
    grid.attrs["doi"] = "10.7289/V5C8276M"
    return grid
