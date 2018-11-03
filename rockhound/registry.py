"""
Create a dataset registry using Pooch and the rockhound/registry.txt file.
"""
import os

import pooch


REGISTRY = pooch.create(
    path=["~", ".rockhound", "data"], base_url="", env="ROCKHOUND_DATA_DIR"
)
REGISTRY.load_registry(os.path.join(os.path.dirname(__file__), "registry.txt"))
