"""
Test the ETOPO1 loading function.
"""
import pytest

from .. import fetch_etopo1


def test_etopo1_invalid_version():
    "Use invalid version"
    with pytest.raises(ValueError):
        fetch_etopo1(version="bla")


def test_etopo1_file_name_only():
    "Only fetch the file name."
    name = fetch_etopo1(version="ice", load=False)
    assert name.endswith("ETOPO1_Ice_g_gmt4.grd.gz.decomp")
    name = fetch_etopo1(version="bedrock", load=False)
    assert name.endswith("ETOPO1_Bed_g_gmt4.grd.gz.decomp")


def test_etopo1():
    "Sanity checks for the grid."
    grid = fetch_etopo1(version="ice")
    assert grid.ice.shape == (10801, 21601)
    assert grid.attrs["title"] == "ETOPO1 Ice Surface Relief"
    assert tuple(grid.dims) == ("latitude", "longitude")
    grid = fetch_etopo1(version="bedrock")
    assert grid.bedrock.shape == (10801, 21601)
    assert grid.attrs["title"] == "ETOPO1 Bedrock Relief"
    assert tuple(grid.dims) == ("latitude", "longitude")
