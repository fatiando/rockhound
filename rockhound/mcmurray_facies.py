"""
Load the Mannville Group Well Logs dataset from Alberta, Canada.
"""
import pandas as pd
from pooch import Unzip
from .registry import REGISTRY


def fetch_mcmurray_facies(*, load=True):
    r"""
    This is a preprocessed dataframe of well log information focused on facies prediction.

    The preprocessed data is coming from here: https://github.com/JustinGOSSES/McMurray-Wabiskaw-preprocessed-datasets

    The original dataset, unprocessed, comes from a collection of over 2000 wells made public by the Alberta Geological Survey’s
    Alberta Energy Regulator. To quote their webpage, “In 1986, Alberta Geological Survey
    began a project to map the McMurray Formation and the overlying Wabiskaw Member of
    the Clearwater Formation in the Athabasca Oil Sands Area. The data that accompany this
     report are one of the most significant products of the project and will hopefully
     facilitate future development of the oil sands.” It includes well log curves as LAS
     files and tops in txt files and xls files. There is a word doc and a text file that
     describes the files and associated metadata.

    _Wynne, D.A., Attalla, M., Berezniuk, T., Brulotte, M., Cotterill, D.K., Strobl, R.
    and Wightman, D. (1995): Athabasca Oil Sands data McMurray/Wabiskaw oil sands deposit
     - electronic data; Alberta Research Council, ARC/AGS Special Report 6._

    Please go to the links below for more information and the dataset:

    Report for Athabasca Oil Sands Data McMurray/Wabiskaw Oil Sands Deposit
    http://ags.aer.ca/document/OFR/OFR_1994_14.PDF

    Electronic data for Athabasca Oil Sands Data McMurray/Wabiskaw Oil Sands Deposit
    http://ags.aer.ca/publications/SPE_006.html

    In the metadata file
    https://github.com/JustinGOSSES/MannvilleGroup_Strat_Hackathon/blob/master/SPE_006_originalData/Metadata/SPE_006.txt -> SPE_006.txt.
    the dataset is described as Access Constraints: Public and Use Constraints:
    Credit to originator/source required. Commercial reproduction not allowed.

    _The Latitude and longitude of the wells is not in the original dataset.
    https://github.com/dalide -> @dalide used the Alberta Geological Society’s UWI
    conversion tool to find lat/longs for each of the well UWIs. A CSV with the
    coordinates of each well’s location can be found
    https://github.com/JustinGOSSES/MannvilleGroup_Strat_Hackathon/blob/master/well_lat_lng.csv.
    These were then used to find each well’s nearest neighbors.

    Please note that there are a few misformed .LAS files in the full dataset, so the code
    in this repository skips those.

    If for some reason the well data is not found at the links above, you should
    be able to find it https://github.com/JustinGOSSES/MannvilleGroup_Strat_Hackathon/tree/master/SPE_006_originalData

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    Returns
    -------
    mcmurray_facies : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        columns : ['CALI', 'COND', 'DELT', 'DEPT', 'DPHI', 'DT', 'GR', 'ILD', 'ILM','NPHI', 'PHID', 'RHOB', 'SFL', 'SFLU', 'SN', 'SP', 'UWI', 'SitID','lat', 'lng', 'Depth', 'LithID', 'W_Tar', 'SW', 'VSH', 'PHI', 'RW','lithName']
    """

    fname = REGISTRY.fetch("mcmurray_facies_dataframe.h5.zip", processor=Unzip())
    if not load:
        return fname

    ##### Insert here all the code to load to take the unzipped files and process into single dataframe for the called dataset

    ##### For debugging
    # print("fname",fname)
    # print("type fname ",type(fname ))

    ##### These try and excepts are here as some versions of pandas don't work with generic buffers, which fname may be depending on your OS, when reading H5 files into pandas.
    ##### We get around this, but turning the generic buffer fname into a string. This works on MacOS. It may not work on your OS.
    ##### IT HAS NOT BEEN TESTED IN ANY SIGNIFICANT MANNER AT THIS TIME
    try:
        data = pd.read_hdf(fname)
    except NotImplementedError:
        try:
            data = pd.read_hdf(str(fname[0]))
        except NotImplementedError:
            data = "could not read hdf as the conversion of fname to a stringified version didn't work well. Oops."
            print(
                "PyTables called by Pandas could not handle generic buffer. Tried to convert path to string. However, conversion of fname to a stringified version didn't work well. Oops."
            )

    return data
