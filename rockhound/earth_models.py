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
    function of depth. The model includes the depth, density, seismic velocities, attenuation (Q)
    on the boundaries of several Earth layers. It's available through IRIS Data Services Products [IRIS2011]_
    in a csv file (comma-separated values). The data is loaded into :class:`pandas.DataFrame` objects.

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
        - ``density`` in Mg/m³.
        - ``Vp`` and ``Vs`` in km/s.
        - ``Q_mu`` and ``Q_kappa`` (dimensionless).
    """
    fname = REGISTRY.fetch("AK135F_AVG_IDV.csv")
    if not load:
        return fname
    data = np.loadtxt(fname, delimiter=",", skiprows=2)
    columns = ["depth", "density", "Vp", "Vs", "Q_mu", "Q_kappa"]
    ak135f = pd.DataFrame(data=data, columns=columns)
    return ak135f


def fetch_iasp91(*, load=True):
    r"""
    Fetch the IASP91 Earth model.
    
    iasp91 [Kennett1991]_ is a one-dimensional model representing Earth properties as
    a function of depth or radius. This model has parameters for depth, radius, P-wave 
    velocity and S-wave velocity.It's available through IRIS Data Services Products [IRIS2011]_ in a csv file
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
    need to change this!!!!
    Fetch the IASP91 Earth model.
    
    iasp91 [Kennett1991]_ is a one-dimensional model representing Earth properties as
    a function of depth or radius. This model has parameters for depth, radius, P-wave 
    velocity and S-wave velocity.It's available through IRIS Data Services Products [IRIS2011]_ in a csv file
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
    fname = REGISTRY.fetch("MEAN.nc")
    if not load:
        return fname
    data = xr.open_dataset(fname)
    mean = data.to_dataframe()
    mean.reset_index(inplace=True)
    mean.columns = ['radius', 'density', 'Vp', 'Vs', 'Q_kappa', 'Q_mu']
    
    #mean = pd.DataFrame(data=data, columns=columns)
    return mean


