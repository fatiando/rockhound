"""
Load the seafloor age, spreading rate, and spreading symmetry grids by
Müller et al. (2008).
"""
import xarray as xr
from pooch import Decompress

from .registry import REGISTRY


def fetch_seafloor_age(*, resolution="6min", load=True, **kwargs):
    """
    Fetch the age of the oceanic lithosphere global grid

    Grids produced by [Muller2008]_.

    Includes the age uncertainty grid as well. Both are available in 2 and 6 arc-minute
    resolutions. The units for the ages are millions of years. The grids span longitudes
    from 0 E to 360 E and latitudes from 90 N to -90 N and are grid-line registered.

    If the files aren't already in your data directory, they will be downloaded
    automatically.

    Parameters
    ----------
    resolution : str
        Which resolution grid to load. Must be ``"6min"`` or ``"2min"``.
    load : bool
        Wether to load the data into an :class:`xarray.Dataset` or just return the
        path to the downloaded data. If False, will return a list with the paths to the
        age and age uncertainty grids, respectively.
    kwargs
        Keyword arguments will be forwarded to the :func:`xarray.open_dataset` function
        that loads the grid into memory.

    Returns
    -------
    grid : :class:`xarray.Dataset` or str
        The loaded grid or the file path to the downloaded data.

    """
    resolutions = ["6min", "2min"]
    if resolution not in resolutions:
        raise ValueError(
            "Invalid seafloor age grid resolution '{}'. Must be one of {}.".format(
                resolution, resolutions
            )
        )
    fname_age = REGISTRY.fetch(
        "age.3.{}.nc.bz2".format(resolution[0]), processor=Decompress()
    )
    fname_error = REGISTRY.fetch(
        "ageerror.3.{}.nc.bz2".format(resolution[0]), processor=Decompress()
    )
    if not load:
        return [fname_age, fname_error]
    grid = xr.merge(
        [
            xr.open_dataset(fname_age, **kwargs).rename(z="age") / 100,
            xr.open_dataset(fname_error, **kwargs).rename(z="uncertainty") / 100,
        ]
    )
    # Add more metadata and fix some names
    grid = grid.rename(x="longitude", y="latitude")
    grid.attrs["title"] = "Age of oceanic lithosphere"
    grid.attrs["doi"] = "10.1029/2007GC001743"
    grid.age.attrs["long_name"] = "Age of oceanic lithosphere"
    grid.age.attrs["units"] = "million_years"
    grid.uncertainty.attrs["long_name"] = "Age uncertainty"
    grid.uncertainty.attrs["units"] = "million_years"
    return grid
