"""
Slab2 - A Comprehensive Subduction Zone Geometry Model
======================================================

Slab2 is a three-dimensional compilation of global subduction geometries, separated
into regional models for each major subduction zone.
More information at the
`USGS <https://www.sciencebase.gov/catalog/item/5aa1b00ee4b0b1c392e86467>`__ website.
"""

import rockhound as rh
import matplotlib.pyplot as plt
import cmocean
import cartopy.crs as ccrs

plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.Robinson())

zones = {
    "alaska",
    "calabria",
    "caribbean",
    "cascadia",
    "central_america",
    "cotabalo",
    "halmahera",
    "hellenic",
    "himalaya",
    "hindu_kush",
    "izu_bonin",
    "kamchatka",
    "kermadec",
    "makran",
    "manila_trench",
    "muertos_trough",
    "new_guinea",
    "pamir",
    "philippines",
    "puysegur",
    "ryukyu",
    "scotia_sea",
    "solomon_islands",
    "south_america",
    "sulawesi",
    "sumatra_java",
    "vanuatu",
}
# Load a geometry of the Alaska subduction zone
for zone in zones:
    grid = rh.fetch_slab2(zone)

    pc = grid.depth.plot.pcolormesh(
        cmap=cmocean.cm.thermal_r,
        ax=ax,
        transform=ccrs.PlateCarree(),
        add_colorbar=False
    )
# make the map global rather than have it zoom in to the extents of any plotted data
ax.set_global()
ax.coastlines()
plt.show()
