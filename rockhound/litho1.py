"""
Fetch and load the LITHO1.0 model
"""
import os
import xarray as xr
from pooch import Untar
import pandas as pd
import numpy as np

from .registry import REGISTRY


COORDINATES_FILE = "Icosahedron_Level7_LatLon_mod.txt"
PROPERTIES = ["depth", "density", "Vp", "Vs", "Qkappa", "Qmu", "Vp2", "Vs2", "eta"]
COL_NAMES = PROPERTIES + ["boundaries"]
BOUNDARIES = [
    "IC0",
    "IC1",
    "IC2",
    "IC3",
    "IC4",
    "IC5",
    "IC6",
    "IC7",
    "IC8",
    "IC9",
    "IC10",
    "IC11",
    "IC12",
    "IC13",
    "IC14",
    "IC15",
    "IC16",
    "IC17",
    "IC18",
    "IC19",
    "IC20",
    "IC21",
    "IC22",
    "IC23",
    "IC24",
    "OC0",
    "OC1",
    "OC2",
    "OC3",
    "OC4",
    "OC5",
    "OC6",
    "OC7",
    "OC8",
    "OC9",
    "OC10",
    "OC11",
    "OC12",
    "OC13",
    "OC14",
    "OC15",
    "OC16",
    "OC17",
    "OC18",
    "OC19",
    "OC20",
    "OC21",
    "OC22",
    "OC23",
    "OC24",
    "OC25",
    "OC26",
    "OC27",
    "OC28",
    "OC29",
    "OC30",
    "OC31",
    "OC32",
    "OC33",
    "OC34",
    "OC35",
    "OC36",
    "OC37",
    "OC38",
    "OC39",
    "OC40",
    "OC41",
    "OC42",
    "OC43",
    "OC44",
    "OC45",
    "M0",
    "M1",
    "M2",
    "M3",
    "M4",
    "M5",
    "M6",
    "M7",
    "M8",
    "M9",
    "M10",
    "M11",
    "M12",
    "M13",
    "M14",
    "M15",
    "M16",
    "M17",
    "M18",
    "M19",
    "M20",
    "M21",
    "M22",
    "M23",
    "M24",
    "M25",
    "M26",
    "M27",
    "M28",
    "M29",
    "M30",
    "M31",
    "M32",
    "M33",
    "M34",
    "M35",
    "M36",
    "M37",
    "M38",
    "M39",
    "M40",
    "M41",
    "M42",
    "M43",
    "M44",
    "M45",
    "M46",
    "M47",
    "M48",
    "M49",
    "M50",
    "M51",
    "M52",
    "M53",
    "M54",
    "M55",
    "M56",
    "M57",
    "M58",
    "M59",
    "M60",
    "M61",
    "M62",
    "M63",
    "M64",
    "M65",
    "M66",
    "M67",
    "M68",
    "M69",
    "M70",
    "M71",
    "A-BOTTOM",
    "A-TOP",
    "ASTHENO-BOTTOM",
    "ASTHENO-TOP",
    "LID-BOTTOM",
    "LID-TOP",
    "CRUST3-BOTTOM",
    "CRUST3-TOP",
    "CRUST2-BOTTOM",
    "CRUST2-TOP",
    "CRUST1-BOTTOM",
    "CRUST1-TOP",
    "SEDS3-BOTTOM",
    "SEDS3-TOP",
    "SEDS2-BOTTOM",
    "SEDS2-TOP",
    "SEDS1-BOTTOM",
    "SEDS1-TOP",
    "ICE-BOTTOM",
    "ICE-TOP",
    "WATER-BOTTOM",
    "WATER-TOP",
]


def fetch_litho1(*, load=True):
    """
    Load the LITHO1 model.

    LITHO1.0 model is a 1$^o$ tessellated model of the crust and uppermost
    mantle of the Earth, extending into the upper mantle to include the
    lithospheric lid and underlying asthenosphere.
    The model is parameterized laterally by tessellated nodes and vertically
    as a series of geophysically identified layers, such as water, ice,
    sediments, crystalline crust, lithospheric lid, and asthenosphere.
    More details can be found in the model webside
    https://igppweb.ucsd.edu/~gabi/litho1.0.html and [PASYANOS]_.
    """
    fnames = REGISTRY.fetch("litho1.0.tar.gz", processor=Untar())
    if not load:
        return fnames

    # Load the space coordinates
    (coord_file,) = tuple(i for i in fnames if i.endswith(COORDINATES_FILE))
    latitude, _, longitude = np.loadtxt(coord_file, unpack=True)
    # Create array of nodes indices (nodes indices start on 1)
    nodes = np.arange(1, latitude.size + 1)
    # Initialize xr.Dataset
    coords = {
        "nodes": ("nodes", nodes),
        "longitude": ("nodes", longitude),
        "latitude": ("nodes", latitude),
        "boundaries": ("boundaries", BOUNDARIES),
    }
    arrays = {
        i: (["nodes", "boundaries"], np.nan * np.ones((nodes.size, len(BOUNDARIES))))
        for i in PROPERTIES
    }
    dataset = xr.Dataset(arrays, coords=coords)
    # Read node files
    for node in nodes:
        (node_file,) = tuple(
            i for i in fnames if os.path.basename(i) == "node{}.model".format(node)
        )
        node_df = pd.read_csv(
            node_file, sep=r"\s+", skiprows=1, names=COL_NAMES, index_col=-1
        )
        # Remove duplicate rows in the dataframe
        node_df = node_df.drop_duplicates()
        # Remplace the dataframe information in the dataset
        for b, p in zip(node_df.index, PROPERTIES):
            dataset[p].loc[dict(nodes=node, boundaries=b)] = node_df[p].loc[b]
    return dataset
