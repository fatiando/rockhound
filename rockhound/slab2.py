"""
Load the subduction geometry for a given zone.
"""
import os
import xarray as xr

from .registry import REGISTRY

DATASETS = {
    "depth": dict(name="Slab depth", units="meters"),
    "dip": dict(name="Slab dip", units="degree"),
    "strike": dict(name="Slab strike", units="degree"),
    "thickness": dict(name="Slab thickness", units="meters"),
    "depth_uncertainty": dict(name="Slab depth uncertainty", units="meters"),
}

ZONES = {
    "alaska": dict(fname_indicator="alu", name="Alaska"),
    "calabria": dict(fname_indicator="cal", name="Calabria"),
}


def fetch_slab2(zone, *, load=True, **kwargs):
    """
    Load the Slab2 model for a given subduction zone.

    Slab2 is a three-dimensional compilation of global subduction geometries,
    separated into regional models for each major subduction zone.
    Each model is based on a probabilistic non-linear fit to data from a combined
    catalog consisting of several independent data sets - historic earthquake
    catalogs, CMT solutions, active seismic profiles, global plate boundaries,
    bathymetry and sediment thickness information [BEDMAP2]_.

    Parameters
    ----------
    zone : str
        subduction zone to fech the model.
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
    if zone not in ZONES:
        raise ValueError(
            "Invalid slab zone: {}".format(set(zone).difference(ZONES.keys()))
        )
    fnames = [
        REGISTRY.fetch(
            "{}_slab2_{}.grd".format(ZONES[zone]["fname_indicator"], dataset)
        )
        for dataset in DATASETS
    ]
    if not load:
        return fnames
    arrays = [xr.open_dataarray(f).rename(x="longitude", y="latitude") for f in fnames]
    for array, dataset in zip(arrays, DATASETS):
        array.name = dataset
        # Change long_name and add units of each array
        array.attrs["long_name"] = DATASETS[dataset]["name"]
        array.attrs["units"] = DATASETS[dataset]["units"]
    # Merge arrays into a single xr.Dataset
    ds = xr.merge(arrays)
    # Change units of thickness, depth and depth_uncertainty to meters
    ds["thickness"] *= 1000
    ds["depth"] *= 1000
    ds["depth_uncertainty"] *= 1000
    # Change long_name and units of longitude and latitude coords
    ds.longitude.attrs["long_name"] = "Longitude"
    ds.longitude.attrs["units"] = "degrees"
    ds.latitude.attrs["long_name"] = "Latitude"
    ds.latitude.attrs["units"] = "degrees"
    # Add attributes to the xr.Dataset
    ds.attrs.update(
        {
            "title": "Slab2 model - Zone: {}".format(ZONES[zone]["name"]),
            "zone": ZONES[zone]["name"],
            "datum": "WGS84",
            "doi": "10.5066/F7PV6JNV.",
        }
    )
    return ds
