"""
Load the ak135-f dataset.
"""
import pandas as pd
import numpy as np

from .registry import REGISTRY


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
    columns = [
        "depth",
        "density",
        "Vp",
        "Vs",
        "Q_mu",
        "Q_kappa",
    ]
    ak135f = pd.DataFrame(data=data, columns=columns)
    return ak135f
