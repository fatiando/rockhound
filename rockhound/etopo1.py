"""
Load the ETOPO1 Earth Relief dataset.
"""
import os
import gzip
import tempfile
import shutil

import xarray as xr

from .registry import REGISTRY


def fetch_etopo1(version, load=True, **kwargs):
    """
    Fetch the ETOPO1 global relief model.

    ETOPO1 is a 1 arc-minute global relief model of Earth's surface that integrates land
    topography and ocean bathymetry [AmanteEakins2009]_. It's available in two versions:
    "Ice Surface" (top of Antarctic and Greenland ice sheets) and "Bedrock" (base of the
    ice sheets). Each grid is in a separate gzipped netCDF file (grid-line registered
    version). The grids are loaded into :class:`xarray.Dataset` objects.

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
    fname = REGISTRY.fetch(available[version])
    if not load:
        return fname

    # Windows complains about file permissions if trying to open a file with xarray that
    # is already open. So we can't use the tempfile directly in a 'with' block.
    temporary = tempfile.NamedTemporaryFile(delete=False)
    try:
        with temporary:
            # Decompress the file into a temporary file so we can load it with xarray
            with gzip.open(fname) as unzipped:
                shutil.copyfileobj(unzipped, temporary)
        # Make sure the data are loaded into memory and not linked to file
        grid = xr.open_dataset(temporary.name, **kwargs).load()
        # Close any files associated with this dataset to make sure can delete them
        grid.close()
    finally:
        os.remove(temporary.name)
    # Add more metadata and fix some names
    names = {"ice": "Ice Surface", "bedrock": "Bedrock"}
    grid = grid.rename(z=version, x="longitude", y="latitude")
    grid[version].attrs["long_name"] = "ETOPO1 {} relief [meters]".format(
        names[version]
    )
    grid.attrs["title"] = grid[version].attrs["long_name"]
    return grid
