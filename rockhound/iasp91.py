import pandas as pd
import numpy as np

from .registry import REGISTRY
    
def fetch_iasp91(*, load=True):
    r"""
   

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
    