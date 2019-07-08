"""
Load the  (IASP91) dataset.
"""
import pandas as pd
import numpy as np

from .registry import REGISTRY
    
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
    columns = [
        "depth", 
        "radius",
        "Vp",
        "Vs"
    ]
    iasp91 = pd.DataFrame(data=data, columns=columns)
    return iasp91
    