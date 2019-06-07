"""
Test the PREM loading function.
"""
from ..mcmurray_facies import fetch_mcmurray_facies


def test_mcmurray_facies_file_name_only():
    "Only fetch the file name."
    fname = fetch_mcmurray_facies(load=False)
    assert "mcmurray_facies_dataframe.h5.zip" in fname[0]


def test_mcmurray_facies():
    "Sanity checks for the mcmurray_facies DataFrame"
    mcmurray_facies = fetch_mcmurray_facies()
    assert len(mcmurray_facies) == 328204
    columns = str(
        [
            "CALI",
            "COND",
            "DELT",
            "DEPT",
            "DPHI",
            "DT",
            "GR",
            "ILD",
            "ILM",
            "NPHI",
            "PHID",
            "RHOB",
            "SFL",
            "SFLU",
            "SN",
            "SP",
            "UWI",
            "SitID",
            "lat",
            "lng",
            "Depth",
            "LithID",
            "W_Tar",
            "SW",
            "VSH",
            "PHI",
            "RW",
            "lithName",
        ]
    )
    mcmurray_facies_columns = str(list(mcmurray_facies.columns))
    assert mcmurray_facies_columns == columns
