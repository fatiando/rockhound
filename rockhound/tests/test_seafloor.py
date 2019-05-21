"""
Test the seafloor age grids.
"""
import pytest
import numpy.testing as npt

from .. import fetch_seafloor_age


def test_seafloor_age_file_name_only():
    "Make sure the correct file names are being returned"
    names = fetch_seafloor_age(load=False)
    assert len(names) == 2
    assert names[0].endswith("age.3.6.nc.bz2.decomp")
    assert names[1].endswith("ageerror.3.6.nc.bz2.decomp")


def test_seafloor_age_invalid_resolution():
    "Make sure an error is raised"
    with pytest.raises(ValueError):
        fetch_seafloor_age(resolution=6)
    with pytest.raises(ValueError):
        fetch_seafloor_age(resolution="bla")


def test_seafloor_age():
    "Sanity checks for the data"
    grid = fetch_seafloor_age()
    assert set(grid.data_vars) == {"age", "uncertainty"}
    assert tuple(grid.dims) == ("latitude", "longitude")
    assert grid.age.shape == (1801, 3601)
    assert grid.uncertainty.shape == (1801, 3601)
    npt.assert_allclose([grid.age.min(), grid.age.max()], [0, 280])
    npt.assert_allclose([grid.uncertainty.min(), grid.uncertainty.max()], [0, 15])
