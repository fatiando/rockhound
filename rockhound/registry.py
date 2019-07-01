"""
Create a dataset registry using Pooch and the rockhound/registry.txt file.
"""
import os

import pooch


REGISTRY = pooch.create(
    path=pooch.os_cache("rockhound"), base_url="", env="ROCKHOUND_DATA_DIR"
)
REGISTRY.load_registry(os.path.join(os.path.dirname(__file__), "registry.txt"))


def data_location():
    r"""
    The absolute path to the data storage location on disk.

    This is where the data sets are saved on your computer. The data location is
    dependent on the operating system. The folder locations are defined by the
    ``appdirs``  package (see the
    `appdirs documentation <https://github.com/ActiveState/appdirs>`__).
    It can also be overwritten by the ``ROCKHOUND_DATA_DIR`` environment variable.

    Returns
    -------
    path : str
        The local data storage location.

    """
    return str(REGISTRY.abspath)
