"""
Test the registry operation functions
"""
import os

from ..registry import data_location


def test_data_location():
    "Make sure the registry has the right last name"
    path = data_location()
    assert os.path.exists(path)
    # This is the most we can check in a platform independent way without testing
    # appdirs itself.
    assert "rockhound" in path
