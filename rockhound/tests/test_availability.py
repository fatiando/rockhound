"""
Test if all files on registry are available for download
"""
import pytest
from ..registry import REGISTRY


@pytest.mark.minimal
def test_available():
    """
    Check that files in registry are available for download
    """
    for fname in REGISTRY.registry_files:
        assert REGISTRY.is_available(fname)
