"""
Fetch sample datasets
"""
import pandas as pd
import xarray as xr
from pooch import Decompress

from .registry import REGISTRY


def fetch_baja_bathymetry():
    """
    Fetch sample bathymetry data from Baja California.

    This is the ``@tut_ship.xyz`` sample data from the `GMT
    <http://gmt.soest.hawaii.edu/>`__ tutorial.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        The bathymetry data. Columns are longitude, latitude, and bathymetry
        (in meters) for each data point.

    See also
    --------
    setup_baja_bathymetry_map: Utility function to help setup a Cartopy map.
    """
    data_file = REGISTRY.fetch("baja-bathymetry.csv.xz")
    data = pd.read_csv(data_file, compression="xz")
    return data


def fetch_california_gps():
    """
    Fetch sample GPS velocity data from California (the U.S. West coast).

    Velocities and their standard deviations are in meters/year. Height is
    geometric height above WGS84 in meters. Velocities are referenced to the
    North American tectonic plate (NAM08). The average velocities were released
    on 2017-12-27.

    This material is based on EarthScope Plate Boundary Observatory data
    services provided by UNAVCO through the GAGE Facility with support from the
    National Science Foundation (NSF) and National Aeronautics and Space
    Administration (NASA) under NSF Cooperative Agreement No. EAR-1261833.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        The GPS velocity data. Columns are longitude, latitude, height
        (geometric, in meters), East velocity (meter/year), North velocity
        (meter/year), upward velocity (meter/year), standard deviation of East
        velocity (meter/year), standard deviation of North velocity
        (meter/year), standard deviation of upward velocity (meter/year).

    See also
    --------
    setup_california_gps_map: Utility function to help setup a Cartopy map.

    """
    data_file = REGISTRY.fetch("california-gps.csv.xz")
    data = pd.read_csv(data_file, compression="xz")
    return data


def fetch_texas_wind():
    """
    Fetch sample wind speed and air temperature data for Texas, USA.

    Data are average wind speed and air temperature for data for February 26
    2018. The original data was downloaded from `Iowa State University
    <https://mesonet.agron.iastate.edu/request/download.phtml>`__.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        Columns are the station ID, longitude, latitude, air temperature in C,
        east component of wind speed in knots, and north component of wind
        speed in knots.

    See also
    --------
    setup_texas_wind_map: Utility function to help setup a Cartopy map.

    """
    data_file = REGISTRY.fetch("texas-wind.csv")
    data = pd.read_csv(data_file)
    return data


def fetch_geoid_earth():
    """
    Fetch a global grid of the geoid height.

    The geoid height is the height of the geoid above (positive) or below
    (negative) the ellipsoid (WGS84). The data are on a regular grid with 0.5
    degree spacing, which was generated from the spherical harmonic model
    EIGEN-6C4 [Forste_etal2014]_ using the `ICGEM Calculation Service
    <http://icgem.gfz-potsdam.de/>`__. See the ``attrs`` attribute of the
    :class:`xarray.Dataset` for information regarding the grid generation.

    Returns
    -------
    grid : :class:`xarray.Dataset`
        The geoid grid (in meters). Coordinates are geodetic latitude and
        longitude.

    """
    fname = REGISTRY.fetch("geoid-earth-0.5deg.nc.xz", processor=Decompress())
    data = xr.open_dataset(fname, engine="scipy").astype("float64")
    return data


def fetch_topography_earth():
    """
    Fetch a global grid of Earth relief (topography and bathymetry).

    The grid is based on the ETOPO1 model [AmanteEakins2009]_. The original
    model has 1 arc-minute grid spacing but here we downsampled to 0.5 degree
    grid spacing to save space and download times. The downsampled grid was
    generated from a spherical harmonic model using the `ICGEM Calculation
    Service <http://icgem.gfz-potsdam.de/>`__. See the ``attrs`` attribute of
    the returned :class:`xarray.Dataset` for information regarding the grid
    generation.

    ETOPO1 heights are referenced to "sea level".

    Returns
    -------
    grid : :class:`xarray.Dataset`
        The topography grid (in meters) relative to sea level. Coordinates are
        geodetic latitude and longitude.

    """
    fname = REGISTRY.fetch("etopo1-0.5deg.nc.xz", processor=Decompress())
    # The data are stored as int16 to save disk space. Cast them to floats to
    # avoid integer division problems when processing.
    data = xr.open_dataset(fname, engine="scipy").astype("float64")
    return data


def fetch_britain_magnetic():
    """
    Fetch total-field magnetic anomaly data of Great Britain.

    These data are a complete airborne survey of the entire Great Britain
    conducted between 1955 and 1965. The data are made available by the
    British Geological Survey (BGS) through their `geophysical data portal
    <https://www.bgs.ac.uk/products/geophysics/aeromagneticRegional.html>`__.

    License: `Open Government License
    <http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/>`__

    The columns of the data table are longitude, latitude, total-field magnetic
    anomaly (nanoTesla), observation height relative to the WGS84 datum (in
    meters), survey area, and line number and line segment for each data point.

    Latitude, longitude, and elevation data converted from original OSGB36
    (epsg:27700) coordinate system to WGS84 (epsg:4326) using to_crs function
    in GeoPandas.

    See the original data for more processing information.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        The magnetic anomaly data.
    """
    return pd.read_csv(REGISTRY.fetch("britain-magnetic.csv.xz"), compression="xz")


def fetch_south_africa_gravity():
    """
    Fetch gravity station data from South Africa

    This data base (14559 records), received in January 1986, consists in land
    gravity surveys within the boundaries of the Republic of South Africa. The
    survey was conducted by Dr. R.J. Kleywegt with the contribution of the
    Republic of South Africa, the Department of Mineral and Energy Affairs and
    the Geological Survey. The data was made available by the `National Centers
    for Environmental Information (NCEI) <https://www.ngdc.noaa.gov/>`__
    (formerly NGDC) and are in the `public domain
    <https://www.ngdc.noaa.gov/ngdcinfo/privacy.html#copyright-notice>`__.
    Original data files can be found at:
    https://www.ngdc.noaa.gov/mgg/gravity/1999/data/regional/africa/

    Principal gravity parameters include elevation and observed gravity. The
    observed gravity values are referenced to the International Gravity
    Standardization Net 1971 (IGSN 71). Elevations are referenced above the sea
    level. Both ``longitude`` and ``latitude`` are given in degrees,
    ``elevation`` in meters and ``gravity`` in mGal.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        The gravity data.

    """
    fname = REGISTRY.fetch("south-africa-gravity.ast.xz")
    columns = ["latitude", "longitude", "elevation", "gravity"]
    return pd.read_csv(fname, sep=r"\s+", names=columns, compression="xz")
