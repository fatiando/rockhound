"""
Load the Preliminary Reference Earth Model (PREM) dataset.
"""
import numpy as np
import pandas as pd
from .registry import REGISTRY


def fetch_prem(load=True):
    """
    Fetch the Preliminary Reference Earth Model (PREM) model.

    The Preliminary reference Earth model [Dziewonsky1981]_ is a one-dimensional model
    representing the average Earth properties as a function of planetary radius.
    The model includes the depth, density, seismic velocities, attenuation (Q) and
    anisotropic parameter (:math:`\eta`) on the boundaries of several Earth layers.
    It's available through IRIS Data Services Products [IRIS2011]_ in a csv file
    (comma-separated values).

    If the file isn't already in your data directory, it will be downloaded
    automatically.


    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.
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
        "Q_kappa"
    ]
    prem = pd.DataFrame(data=data, columns=columns)
    return prem
