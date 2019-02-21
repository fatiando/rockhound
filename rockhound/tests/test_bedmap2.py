"""
Test the Bedmap2 loading function.
"""
import pytest
import numpy as np

from .. import fetch_bedmap2


def test_bedmap2_invalid_dataset():
    "Use invalid dataset"
    with pytest.raises(ValueError):
        fetch_bedmap2(datasets=["bla"])


def test_bedmap2_file_name_only():
    "Only fetch the file name."
    name = fetch_bedmap2(datasets=None, load=False)
    assert name.endswith("bedmap2_tiff.zip")


def test_bedmap2():
    "Sanity checks for the grid."
    # Check datasets with shape (6667, 6667)
    # Define dictionary with min max values
    datasets = {
        "bed": [-7.054e03, 3.972e03],
        "surface": [1.0, 4.082e03],
        "thickness": [0.0, 4.621e03],
        "icemask_grounded_and_shelves": [0.0, 1.0],
        "rockmask": [0.0, 0.0],
        "grounded_bed_uncertainty": [0.0, 65535.0],
        "coverage": [1.0, 1.0],
        "geoid": [np.float32(-65.86805), np.float32(36.63612)],
    }
    for dataset in datasets:
        grid = fetch_bedmap2(datasets=datasets)
        assert getattr(grid, dataset).shape == (6667, 6667)
        assert tuple(grid.dims) == ("x", "y")
        assert getattr(grid, dataset).min() == datasets[dataset][0]
        assert getattr(grid, dataset).max() == datasets[dataset][1]
    # Check lakemask_vostok
    grid = fetch_bedmap2(datasets=["lakemask_vostok"])
    assert grid.lakemask_vostok.shape == (112, 281)
    assert tuple(grid.dims) == ("x", "y")
    assert grid.lakemask_vostok.min() == 1.0
    assert grid.lakemask_vostok.max() == 1.0
    # Check thickness_uncertainty_5km
    grid = fetch_bedmap2(datasets=["thickness_uncertainty_5km"])
    assert grid.thickness_uncertainty_5km.shape == (1361, 1361)
    assert tuple(grid.dims) == ("x", "y")
    assert grid.thickness_uncertainty_5km.min() == 0.0
    assert grid.thickness_uncertainty_5km.max() == 65535.0
