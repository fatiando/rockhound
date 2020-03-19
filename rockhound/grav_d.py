import pandas as pd
from pooch import Unzip

from .registry import REGISTRY


ZONES = {
    "alaska": [
        "AN01",
        "AN02",
        "AN03",
        "AN04",
        "AN05",
        "AN06",
        "AN07",
        "AN08",
        "AN09",
        "AS01",
        "AS02",
        "AS03",
        "AS04",
        "AS05",
        "AS06",
        "AS07",
        "AS08",
        "AS09",
    ],
}
COLUMN_NAMES = ["flight_id", "point_id", "latitude", "longitude", "height", "gravity"]


def fetch_gravd(zone="alaska", *, load=True):
    """
    Fetch GRAV-D Airborne Gravity data
    """
    frames = []
    for zone_code in ZONES[zone]:
        zipfile = "NGS_GRAVD_Block_{}_BETA1.zip".format(zone_code)
        filename = "NGS_GRAVD_Block_{}_Gravity_Data_BETA1.txt".format(zone_code)
        (fname,) = tuple(
            f
            for f in REGISTRY.fetch(zipfile, processor=Unzip())
            if f.endswith(filename)
        )
        frames.append(
            pd.read_csv(fname, sep=r"\s+", index_col=1, names=COLUMN_NAMES)
        )
    return pd.concat(frames)
