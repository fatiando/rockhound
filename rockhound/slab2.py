"""
Load the subduction geometry for a given zone.
"""
import os
import xarray as xr

from .registry import REGISTRY

DATASETS = {
    "depth": dict(name="Slab depth", units="meters"),
    "dip": dict(name="Slab dip", units=""),
    "strike": dict(name="Slab strike", unit="meters"),
    "thickness": dict(name="Slab thickness", unit="meters"),
    "depth_uncertainty": dict(name="Slab depth uncertainty", unit="meters"),
}

ZONES = {"alaska": dict(fname_indicator="alu"), "calabria": dict(fname_indicator="cal")}


def fetch_slab2(zone, datasets, *, load=True, **kwargs):
    """
    Load the Slab2 model for a given subduction zone.

    The available datasets are:
    - ``depth``: slab depth
    - ``dip``: slab dip
    - ``strike``: slab strike
    - ``thickness``: slab thickness
    - ``depth_uncertainty``: slab depth uncertainty

    Parameters
    ----------
    zone : str
        subduction zone to fech the model.
    datasets : list or str
        Names of the datasets that will be loaded from the Slab2 model.
    load : bool
        Wether to load the data into an :class:`xarray.Dataset` or just return the
        path to the downloaded data. If False, will return a list with the paths to the
        subduction grids, respectively.
    kwargs
        Keyword arguments will be forwarded to the :func:`xarray.open_dataset` function
        that loads the grid into memory.

    Returns
    -------
    grid : :class:`xarray.Dataset` or str
        The loaded grid or the file path to the downloaded data.
    """
    if isinstance(datasets, str):
        datasets = [datasets]
    if not set(datasets).issubset(DATASETS.keys()):
        raise ValueError(
            "Invalid datasets: {}".format(set(datasets).difference(DATASETS.keys()))
        )
    if zone not in ZONES:
        raise ValueError(
            "Invalid slab zone: {}".format(set(zone).difference(ZONES.keys()))
        )
    fnames = [
        REGISTRY.fetch(
            "{}_slab2_{}.grd".format(ZONES[zone]["fname_indicator"], dataset)
        )
        for dataset in datasets
    ]
    if not load:
        return fnames
    arrays = [xr.open_dataarray(f) for f in fnames]
    for array, dataset in zip(arrays, datasets):
        array.name = dataset
    ds = xr.merge(arrays)
    return ds
