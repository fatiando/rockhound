"""
Test the Slab2 loading function.
"""
import os
import pytest

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
        ds = fetch_slab2(zone)
        assert ds.title == "Slab2 model - Zone: {}".format(ZONES[zone]["name"])
        assert ds.datum == "WGS84"
        assert ds.zone == ZONES[zone]["name"]
        assert ds.doi == "10.5066/F7PV6JNV"
        # Sanity checks for longitude and latitude
        assert ds.longitude.long_name == "Longitude"
        assert ds.longitude.units == "degrees"
        assert ds.longitude.min() == ds.longitude.actual_range[0]
        assert ds.longitude.max() == ds.longitude.actual_range[1]
        assert ds.latitude.long_name == "Latitude"
        assert ds.latitude.units == "degrees"
        assert ds.latitude.min() == ds.latitude.actual_range[0]
        assert ds.latitude.max() == ds.latitude.actual_range[1]
        # Sanity checks for data
        for dataset in DATASETS:
            assert ds[dataset].long_name == DATASETS[dataset]["name"]
            assert ds[dataset].units == DATASETS[dataset]["units"]
            assert ds[dataset].min() == ds[dataset].actual_range[0]
            assert ds[dataset].max() == ds[dataset].actual_range[1]
