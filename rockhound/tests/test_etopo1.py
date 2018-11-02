"""
Test the ETOPO1 loading function.
"""

from .. import fetch_etopo1


def test_etopo1_file_name_only():
    "Only fetch the file name."
    name = fetch_etopo1(version="ice", load=False)
    assert name.endswith("ETOPO1_Ice_g_gmt4.grd.gz")
    name = fetch_etopo1(version="bedrock", load=False)
    assert name.endswith("ETOPO1_Bed_g_gmt4.grd.gz")
