"""
Load the ETOPO1 Earth Relief dataset.
"""
import os
import gzip
import shutil

import xarray as xr

from .registry import REGISTRY


class Decompress:  # pylint: disable=too-few-public-methods
    """
    Decompress the gzip compressed grid after download.

    This is a Pooch processor class that will be used with ``Pooch.fetch``.
    """

    def __call__(self, fname, action, pooch):
        """
        Decompress the given file.

        The output file will be ``fname`` without the ``.gz`` extension.

        Parameters
        ----------
        fname : str
            Full path of the compressed file in local storage.
        action : str
            Indicates what action was taken by :meth:`pooch.Pooch.fetch`. One of:

            * ``"download"``: The file didn't exist locally and was downloaded
            * ``"update"``: The local file was outdated and was re-download
            * ``"fetch"``: The file exists and is updated so it wasn't downloaded

        pooch : :class:`pooch.Pooch`
            The instance of :class:`pooch.Pooch` that is calling this.

        Returns
        -------
        fname : str
            The full path to the decompressed file.

        """
        # Get rid of the .gz
        decomp = os.path.splitext(fname)[0]
        if action in ("update", "download") or not os.path.exists(decomp):
            with open(decomp, "w+b") as output:
                with gzip.open(fname) as compressed:
                    shutil.copyfileobj(compressed, output)
        return decomp


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
    fname = REGISTRY.fetch(available[version], processor=Decompress())
    if not load:
        return fname
    grid = xr.open_dataset(fname, **kwargs)
    # Add more metadata and fix some names
    names = {"ice": "Ice Surface", "bedrock": "Bedrock"}
    grid = grid.rename(z=version, x="longitude", y="latitude")
    grid[version].attrs["long_name"] = "ETOPO1 {} relief [meters]".format(
        names[version]
    )
    grid.attrs["title"] = grid[version].attrs["long_name"]
    return grid
