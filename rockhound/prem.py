"""
Load the Preliminary Reference Earth Model (PREM) dataset.
"""
import pandas as pd
import numpy as np

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
