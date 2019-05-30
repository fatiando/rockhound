#### SHA256(mannville_demo_data.zip)= 5e60e02306b15ce7bcb6ec35278566696a6b37627ce095360cdba26ef3f99fdf

"""
Load the Mannville Group Well Logs dataset from Alberta, Canada.
"""
import pandas as pd
import numpy as np

from .registry import REGISTRY

# DATASETS = {
#     "bed": dict(name="Bedrock Height", units="meters"),
#     "surface": dict(name="Ice Surface Height", units="meters"),
#     "thickness": dict(name="Ice Thickness", units="meters"),
#     "icemask_grounded_and_shelves": dict(
#         name="Mask of Grounding Line and Floating Ice Shelves"
#     ),
#     "rockmask": dict(name="Mask of Rock Outcrops"),
#     "lakemask_vostok": dict(name="Mask for Lake Vostok"),
#     "grounded_bed_uncertainty": dict(name="Ice Bed Uncertainty", units="meters"),
#     "thickness_uncertainty_5km": dict(name="Ice Thickness Uncertainty", units="meters"),
#     "coverage": dict(name="Distribution of Ice Thickness Data (binary)"),
#     "geoid": dict(name="Geoid Height (WGS84)", units="meters"),
# }

def fetch_prem(*, load=True):
    r"""
    Fetch the Preliminary Reference Earth Model (PREM).

    is a collection of over 2000 wells made public by the Alberta Geological Survey’s 
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
    https://github.com/JustinGOSSES/MannvilleGroup_Strat_Hackathon/blob/master/well_lat_lng.csv . 
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
    prem : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        ##### EDIT THESE TO REFLECT FINAL DATAFRAME !!!!!!!!!!!!
        # - ``radius`` and ``depth`` in km.
        # - ``density`` in g/cm³.
        # - ``Vpv``, ``Vph``, ``Vsv`` and ``Vsh`` in km/s.
        # - ``eta``, ``Q_mu`` and ``Q_kappa`` (dimensionless).
    """

    if isinstance(datasets, str):
        datasets = [datasets]
    if not set(datasets).issubset(DATASETS.keys()):
        raise ValueError(
            "Invalid datasets: {}".format(set(datasets).difference(DATASETS.keys()))
        )



    fname = REGISTRY.fetch("mannville_demo_data.zip", processor=Unzip())
    if not load:
        return fname

    ##### Insert here all the code to load to take the unzipped files and process into single dataframe for the called dataset


    data = np.loadtxt(fname, delimiter=",")
    columns = [
        ##### Replace these with real ones
        # "radius",
        # "depth",
        # "density",
        # "Vpv",
        # "Vph",
        # "Vsv",
        # "Vsh",
        # "eta",
        # "Q_mu",
        # "Q_kappa",
    ]
    mannville = pd.DataFrame(data=data, columns=columns)
    return mannville
