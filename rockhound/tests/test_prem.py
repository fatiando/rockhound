"""
Test the PREM loading function.
"""
from ..prem import fetch_prem


def test_prem_file_name_only():
    "Only fetch the file name."
    fname = fetch_prem(load=False)
    assert fname.endswith("PREM_1s.csv")


def test_prem():
    "Sanity checks for the prem DataFrame"
    prem = fetch_prem()
    assert prem.shape == (199, 10)
    assert prem["radius"].min() == 0
    assert prem["radius"].max() == 6371.0
    assert prem["depth"].min() == 0
    assert prem["depth"].max() == 6371.0
    assert prem["density"].min() == 1.02
    assert prem["density"].max() == 13.0885
    assert prem["Vpv"].min() == 1.45
    assert prem["Vpv"].max() == 13.71662
    assert prem["Vph"].min() == 1.45
    assert prem["Vph"].max() == 13.71662
    assert prem["Vsv"].min() == 0
    assert prem["Vsv"].max() == 7.26597
    assert prem["Vsh"].min() == 0
    assert prem["Vsh"].max() == 7.26597
    assert prem["eta"].min() == 0.90039
    assert prem["eta"].max() == 1
    assert prem["Q_mu"].min() == 0
    assert prem["Q_mu"].max() == 600
    assert prem["Q_kappa"].min() == 1327.7
    assert prem["Q_kappa"].max() == 57823
