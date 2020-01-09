"""
Test the Slab2 loading function.
"""
import os
import pytest
import numpy.testing as npt

from .. import fetch_slab2
from ..slab2 import ZONES, DATASETS


def test_slab2_invalid_zone():
    "Test if invalid zone is caught"
    with pytest.raises(ValueError):
        fetch_slab2(zone="this is an invalid zone")


def test_slab2_file_name_only():
    "Fetch only the filename of the files"
    for zone in ZONES:
        fnames = fetch_slab2(zone, load=False)
        fnames = [os.path.basename(f) for f in fnames]
        expected_fnames = set(
            "{}_slab2_{}.grd".format(ZONES[zone]["fname_indicator"], dataset)
            for dataset in DATASETS
        )
        assert len(fnames) == 5
        assert set(fnames) == expected_fnames


def test_slab2():
    """
    Test if loaded files are correct
    """
    for zone in ZONES:
        dataset = fetch_slab2(zone)
        assert dataset.title == "Slab2 model - Zone: {}".format(ZONES[zone]["name"])
        assert dataset.datum == "WGS84"
        assert dataset.zone == zone
        assert dataset.zone_full_name == ZONES[zone]["name"]
        assert dataset.doi == "10.5066/F7PV6JNV"
        # Sanity checks for longitude and latitude
        assert dataset.longitude.long_name == "Longitude"
        assert dataset.longitude.units == "degrees"
        assert dataset.longitude.min() == dataset.longitude.actual_range[0]
        assert dataset.longitude.max() == dataset.longitude.actual_range[1]
        assert dataset.latitude.long_name == "Latitude"
        assert dataset.latitude.units == "degrees"
        assert dataset.latitude.min() == dataset.latitude.actual_range[0]
        assert dataset.latitude.max() == dataset.latitude.actual_range[1]
        # Sanity checks for data
        for element in DATASETS:
            assert dataset[element].long_name == DATASETS[element]["name"]
            assert dataset[element].units == DATASETS[element]["units"]
            npt.assert_allclose(
                dataset[element].min(), dataset[element].actual_range[0]
            )
            npt.assert_allclose(
                dataset[element].max(), dataset[element].actual_range[1]
            )
