r"""
mcmurray_facies: Preprocessed well log and facies data for facies predictions
============================================================================

    This is a preprocessed dataframe of well log information focused on facies prediction.

    The preprocessed data is coming from here:
    https://github.com/JustinGOSSES/McMurray-Wabiskaw-preprocessed-datasets

    The original dataset, unprocessed, comes from a collection of over 2000 wells made
    public by the Alberta Geological Survey’s Alberta Energy Regulator. To quote their webpage,
    “In 1986, Alberta Geological Survey began a project to map the McMurray Formation and
    the overlying Wabiskaw Member of the Clearwater Formation in the Athabasca Oil Sands Area.
    The data that accompany this report are one of the most significant products of the project
    and will hopefully facilitate future development of the oil sands.” It includes well log
    curves as LAS files and tops in txt files and xls files. There is a word doc and a text
    file that describes the files and associated metadata.

    _Wynne, D.A., Attalla, M., Berezniuk, T., Brulotte, M., Cotterill, D.K., Strobl, R.
    and Wightman, D. (1995): Athabasca Oil Sands data McMurray/Wabiskaw oil sands deposit
     - electronic data; Alberta Research Council, ARC/AGS Special Report 6._

    Please go to the links below for more information and the dataset:

    Report for Athabasca Oil Sands Data McMurray/Wabiskaw Oil Sands Deposit
    http://ags.aer.ca/document/OFR/OFR_1994_14.PDF

    Electronic data for Athabasca Oil Sands Data McMurray/Wabiskaw Oil Sands Deposit
    http://ags.aer.ca/publications/SPE_006.html

    In the metadata file
    https://github.com/JustinGOSSES/MannvilleGroup_Strat_Hackathon/blob/ \
    master/SPE_006_originalData/Metadata/SPE_006.txt -> SPE_006.txt.
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
    be able to find it
    https://github.com/JustinGOSSES/MannvilleGroup_Strat_Hackathon/tree/master/SPE_006_originalData

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

        columns : ['CALI', 'COND', 'DELT', 'DEPT', 'DPHI', 'DT', 'GR', 'ILD', 'ILM', \
            'NPHI', 'PHID', 'RHOB', 'SFL', 'SFLU', 'SN', 'SP', 'UWI', 'SitID','lat', \
                 'lng', 'Depth', 'LithID', 'W_Tar', 'SW', 'VSH', 'PHI', 'RW','lithName']
"""
import matplotlib.pyplot as plt
import rockhound as rh

# Load mcmurray_facies into a DataFrame
FACIES = rh.fetch_mcmurray_facies()
print("first few rows of facies dataframe", FACIES.head())
print("facies columns", FACIES.columns)

# Example Plots
FACIES.plot(kind="scatter", x="GR", y="DPHI", color="red")
plt.show()
