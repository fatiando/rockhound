"""
Load the subduction geometry for a given zone.
"""
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
    "caribbean": dict(fname_indicator="car", name="Caribbean"),
    "cascadia": dict(fname_indicator="cas", name="Cascadia"),
    "central_america": dict(fname_indicator="cam", name="Central America"),
    "cotabalo": dict(fname_indicator="cot", name="Cotabalo"),
    "halmahera": dict(fname_indicator="hal", name="Halmahera"),
    "hellenic": dict(fname_indicator="hel", name="Hellenic Arc"),
    "himalaya": dict(fname_indicator="him", name="Himalaya"),
    "hindu_kush": dict(fname_indicator="hin", name="Hindu Kush"),
    "izu_bonin": dict(fname_indicator="izu", name="Izu-Bonin"),
    "kamchatka": dict(fname_indicator="kur", name="Kamchatka-Kuril Islands-Japan"),
    "kermadec": dict(fname_indicator="ker", name="Kermadec"),
    "makran": dict(fname_indicator="mak", name="Makran"),
    "manila_trench": dict(fname_indicator="man", name="Manila Trench"),
    "muertos_trough": dict(fname_indicator="mue", name="Muertos Trough"),
    "new_guinea": dict(fname_indicator="png", name="New Guinea"),
    "pamir": dict(fname_indicator="pam", name="Pamir"),
    "philippines": dict(fname_indicator="phi", name="Philippines"),
    "puysegur": dict(fname_indicator="puy", name="Puysegur"),
    "ryukyu": dict(fname_indicator="ryu", name="Ryukyu"),
    "scotia_sea": dict(fname_indicator="sco", name="Scotia Sea"),
    "solomon_islands": dict(fname_indicator="sol", name="Solomon Islands"),
    "south_america": dict(fname_indicator="sam", name="South America"),
    "sulawesi": dict(fname_indicator="sul", name="Sulawesi"),
    "sumatra_java": dict(fname_indicator="sum", name="Sumatra-Java"),
    "vanuatu": dict(fname_indicator="van", name="Vanuatu"),
}


def fetch_slab2(zone, *, load=True):
    """
    Load the Slab2 model for a given subduction zone.

    Slab2 is a three-dimensional compilation of global subduction geometries
    (depth, dip, strike and thickness), separated into regional models for each
    major subduction zone.
    Each model is based on a probabilistic non-linear fit to data from
    a combined catalog consisting of several independent data sets - historic
    earthquake catalogs, CMT solutions, active seismic profiles, global plate
    boundaries, bathymetry and sediment thickness information [SLAB2]_.

    Parameters
    ----------
    zone : str
        Subduction zone to fech the model.
        Available zones:

        - ``alaska``: Alaska
        - ``calabria``: Calabria
        - ``caribbean``: Caribbean
        - ``cascadia``: Cascadia
        - ``central_america``: Central America
        - ``cotabalo``: Cotabalo
        - ``halmahera``: Halmahera
        - ``hellenic``: Hellenic Arc
        - ``himalaya``: Himalaya
        - ``hindu_kush``: Hindu Kush
        - ``izu_bonin``: Izu-Bonin
        - ``kamchatka``: Kamchatka-Kuril Islands-Japan
        - ``kermadec``: Kermadec
        - ``makran``: Makran
        - ``manila_trench``: Manila Trench
        - ``muertos_trough``: Muertos Trough
        - ``new_guinea``: New Guinea
        - ``pamir``: Pamir
        - ``philippines``: Philippines
        - ``puysegur``: Puysegur
        - ``ryukyu``: Ryukyu
        - ``scotia_sea``: Scotia Sea
        - ``solomon_islands``: Solomon Islands
        - ``south_america``: South America
        - ``sulawesi``: Sulawesi
        - ``sumatra_java``: Sumatra-Java
        - ``vanuatu``: Vanuatu

    load : bool
        Whether to load the data into an :class:`xarray.Dataset` or just return
        the path to the downloaded data. If False, will return a list with the
        paths to the subduction grids, respectively.
    kwargs
        Keyword arguments will be forwarded to the :func:`xarray.open_dataset`
        function that loads the grid into memory.

    Returns
    -------
    grid : :class:`xarray.Dataset` or str
        The loaded grid or the file path to the downloaded data.
    """
    if zone not in ZONES:
        raise ValueError("Invalid slab zone: {}".format(zone))
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
    grid = xr.merge(arrays)
    # Change units of thickness, depth and depth_uncertainty to meters
    # Also change units of the actual_range attribute to meters
    for field in ("thickness", "depth", "depth_uncertainty"):
        grid[field] *= 1000
        grid[field].attrs["actual_range"] *= 1000
    # Change long_name and units of longitude and latitude coords
    grid.longitude.attrs["long_name"] = "Longitude"
    grid.longitude.attrs["units"] = "degrees"
    grid.latitude.attrs["long_name"] = "Latitude"
    grid.latitude.attrs["units"] = "degrees"
    # Add attributes to the xr.Dataset
    grid.attrs.update(
        {
            "title": "Slab2 model - Zone: {}".format(ZONES[zone]["name"]),
            "zone": zone,
            "zone_full_name": ZONES[zone]["name"],
            "datum": "WGS84",
            "doi": "10.5066/F7PV6JNV",
        }
    )
    return grid
