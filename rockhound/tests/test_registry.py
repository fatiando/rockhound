"""
Test the registry operation functions
"""
import os

from ..registry import data_location


def test_data_location():
    "Make sure the registry has the right last name"
    path = data_location()
    assert os.path.exists(path)
    assert os.path.split(path)[-1] == "rockhound"
