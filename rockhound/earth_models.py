"""
Load IRIS reference earth models.
"""
import pandas as pd
import numpy as np
import xarray as xr

from .registry import REGISTRY


def fetch_prem(*, load=True):
    r"""
    Fetch the Preliminary Reference Earth Model (PREM).

    The Preliminary reference Earth model [Dziewonsky1981]_ is a one-dimensional model
    representing the average Earth properties as a function of planetary radius.
    The model includes the depth, density, seismic velocities, attenuation (Q) and
    anisotropic parameter (:math:`\eta`) on the boundaries of several Earth layers.
    It's available through IRIS Data Services Products [IRIS2011]_ in a csv file
    (comma-separated values). The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    prem : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``radius`` and ``depth`` in km.
        - ``density`` in g/cm³.
        - ``Vpv``, ``Vph``, ``Vsv`` and ``Vsh`` in km/s.
        - ``eta``, ``Q_mu`` and ``Q_kappa`` (dimensionless).
    """
    fname = REGISTRY.fetch("PREM_1s.csv")
    if not load:
        return fname
    data = np.loadtxt(fname, delimiter=",")
    columns = [
        "radius",
        "depth",
        "density",
        "Vpv",
        "Vph",
        "Vsv",
        "Vsh",
        "eta",
        "Q_mu",
        "Q_kappa",
    ]
    prem = pd.DataFrame(data=data, columns=columns)
    return prem


def fetch_ak135f(*, load=True):
    r"""
    Fetch the ak135-f Earth model.

    The ak135-f Earth model [Dziewonsky1981]_ is a variant of the ak135 velocity model.
    ak135-f is a one-dimensional model representing the average Earth properties as a 
    function of depth. The model includes the depth, density, seismic velocities and attenuation (Q)
    on the boundaries of several Earth layers. It's available through IRIS Data Services Products 
    [IRIS2011]_ in a csv file (comma-separated values). The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    ak135f : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``radius`` and ``depth`` in km.
        - ``density`` in Mg/m³.
        - ``Vp`` and ``Vs`` in km/s.
        - ``Q_mu`` and ``Q_kappa`` (dimensionless).
    """
    fname = REGISTRY.fetch("AK135F_AVG_IDV.csv")
    if not load:
        return fname
    data = np.loadtxt(fname, delimiter=",", skiprows=2)
    columns = ["depth", "density", "Vp", "Vs", "Q_kappa", "Q_mu"]
    ak135f = pd.DataFrame(data=data, columns=columns)
    return ak135f


def fetch_iasp91(*, load=True):
    r"""
    Fetch the IASP91 Earth model.
    
    iasp91 [Kennett1991]_ is a one-dimensional model representing Earth properties as
    a function of depth. This model has parameters for depth, radius, P-wave 
    velocity and S-wave velocity. It's available through IRIS Data Services Products [IRIS2011]_ in a csv file
    (comma-separated values). The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    iasp91 : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``radius`` and ``depth`` in km.
        - ``Vp`` and ``Vs`` in km/s.
    """
    fname = REGISTRY.fetch("IASP91.csv")
    if not load:
        return fname
    data = np.loadtxt(fname, delimiter=",")
    columns = ["depth", "radius", "Vp", "Vs"]
    iasp91 = pd.DataFrame(data=data, columns=columns)
    return iasp91


def fetch_mean(*, load=True):
    r"""
    Fetch the MEAN Earth model.
    
    MEAN [Marone 2004]_ is a one-dimensional model representing Earth properties as
    a function of radius. This model has parameters for radius, density, P-wave 
    velocity, S-wave velocity, and attenuation (Q).It's available through IRIS Data Services Products [IRIS2011]_ in a csv file
    (comma-separated values). The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    mean : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``radius`` in km.
        - ``density`` in g/cm³.
        - ``Vp`` and ``Vs`` in km/s.
        - ``Q_mu`` and ``Q_kappa`` (dimensionless).
    """
    fname = REGISTRY.fetch("MEAN.nc")
    if not load:
        return fname
    data = xr.open_dataset(fname)
    mean = data.to_dataframe()
    mean.reset_index(inplace=True)
    mean.columns = ["radius", "density", "Vp", "Vs", "Q_kappa", "Q_mu"]

    return mean


def fetch_pema(*, load=True):
    r"""
    Fetch the PEMA Earth model.

    The PEMA Earth model [Dziewonsky1975]_ is a one-dimensional model representing the average Earth properties as a 
    function of depth. The model includes the depth, density, and seismic velocities on the boundaries of several Earth layers.
    It's available through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values). 
    The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    pema : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``radius`` and ``depth`` in km.
        - ``density`` in g/cm³.
        - ``Vp`` and ``Vs`` in km/s.
    """
    fname = REGISTRY.fetch("PEMA.csv")
    if not load:
        return fname
    pema = pd.read_csv(
        fname, header=None
    )  # np.loadtxt(fname, delimiter=",", skiprows=2)
    pema.columns = ["radius", "depth", "density", "Vp", "Vs"]
    return pema


def fetch_pemc(*, load=True):
    r"""
    Fetch the PEMC Earth model.

    The PEMC Earth model [Dziewonsky1975]_ is a one-dimensional model representing the average Earth properties as a 
    function of depth. The model includes the depth, density, and seismic velocities on the boundaries of several Earth layers.
    It's available through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values). 
    The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    pemc : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``radius`` and ``depth`` in km.
        - ``density`` in g/cm³.
        - ``Vp`` and ``Vs`` in km/s.
    """
    fname = REGISTRY.fetch("PEMC.csv")
    if not load:
        return fname
    pemc = pd.read_csv(fname, header=None)
    pemc.columns = ["radius", "depth", "density", "Vp", "Vs"]
    return pemc


def fetch_pemo(*, load=True):
    r"""
    Fetch the PEMO Earth model.

    The PEMO Earth model [Dziewonsky1975]_ is a one-dimensional model representing the average Earth properties as a 
    function of depth. The model includes the depth, density, and seismic velocities on the boundaries of several Earth layers.
    It's available through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values). 
    The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    pemo : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``radius`` and ``depth`` in km.
        - ``density`` in g/cm³.
        - ``Vp`` and ``Vs`` in km/s.
    """
    fname = REGISTRY.fetch("PEMO.csv")
    if not load:
        return fname
    pemo = pd.read_csv(fname, header=None)
    pemo.columns = ["radius", "depth", "density", "Vp", "Vs"]
    return pemo


def fetch_mc35(*, load=True):
    r"""
    Fetch the MC35 Earth model.

    The MC35 Earth model [VanderLee1997]_ is a one-dimensional model representing the average Earth properties as a 
    function of depth. The model includes the depth and S-wave velocities on the boundaries of several Earth layers.
    It's available through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values). 
    The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    mc35 : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``depth`` in km.
        - ``Vs`` in km/s.
    """
    fname = REGISTRY.fetch("MC35.csv")
    if not load:
        return fname
    mc35 = pd.read_csv(fname, header=None)
    mc35.columns = ["depth", "Vs"]
    return mc35


def fetch_stw105(*, load=True):
    r"""
    Fetch the MC35 Earth model.

    The MC35 Earth model [VanderLee1997]_ is a one-dimensional model representing the average Earth properties as a 
    function of depth. The model includes the depth and S-wave velocities on the boundaries of several Earth layers.
    It's available through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values). 
    The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    stw105 : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``radius`` in m.
        - ``density`` in kg/m^3.
        - ``Vpv``, ``Vsv``, ``Vph``, ``Vsh``, and ``eta`` in m/s.?
        - ``Q_kappa`` and ``Q_mu`` (dimensionless)
    """
    fname = REGISTRY.fetch("STW105.txt")
    if not load:
        return fname
    data = np.loadtxt(fname, skiprows=3)
    columns = [
        "radius",
        "density",
        "Vpv",
        "Vsv",
        "Q_kappa",
        "Q_mu",
        "Vph",
        "Vsh",
        "eta",
    ]
    stw105 = pd.DataFrame(data, columns=columns)
    return stw105


def fetch_tna_sna(*, load=True):
    r"""
    Fetch the TNA/SNA Earth model.

    The MC35 Earth model [VanderLee1997]_ is a one-dimensional model representing the average Earth properties as a 
    function of depth. The model includes the depth and S-wave velocities on the boundaries of several Earth layers.
    It's available through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values). 
    The data is loaded into :class:`pandas.DataFrame` objects.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    stw105 : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        - ``radius`` in m.
        - ``density`` in kg/m^3.
        - ``Vpv``, ``Vsv``, ``Vph``, ``Vsh``, and ``eta`` in m/s.?
        - ``Q_kappa`` and ``Q_mu`` (dimensionless)
    """
    fname = REGISTRY.fetch("StartingVsModel_TNA-SNA-average_IDV.csv")
    if not load:
        return fname
    names = ["radius", "Vs"]
    tna_sna = pd.read_csv(fname, names=names, skiprows=2)
    return tna_sna


#%%

# fname = REGISTRY.fetch("STW105.txt")
# if not load:
#    return fname
# data = np.loadtxt(fname, skiprows=3)
# columns = ["radius",
#           "density",
#           "Vpv",
#           "Vsv",
#           "Q_kappa",
#           "Q_mu",
#           "Vph",
#           "Vsh",
#           "eta"]
# stw105 = pd.DataFrame(data, columns=columns)
##return stw105
