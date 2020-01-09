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

from rockhound.slab2 import ZONES

plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.Robinson())

for zone in ZONES:
    grid = rh.fetch_slab2(zone)

    pc = grid.depth.plot.pcolormesh(
        cmap=cmocean.cm.thermal_r,
        ax=ax,
        transform=ccrs.PlateCarree(),
        add_colorbar=False,
        vmin=-701160.33935547,
        vmax=-1399.69277382,
    )

ax.set_title("Slab2 - A comprehensive subduction zone geometry model")
cb = plt.colorbar(
    pc, ax=ax, label="Depth (meters)", pad=0.05, aspect=40, orientation="horizontal"
)
ax.set_global()
ax.coastlines()
plt.show()
