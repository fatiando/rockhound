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

# Fetch all Slab2 subduction zones and add them inside a list
subduction_zones = []
for zone in ZONES:
    subduction_zones.append(rh.fetch_slab2(zone))

# Get min and max values of the subducting plates' depths
vmax = max([grid.depth.actual_range[1] for grid in subduction_zones])
vmin = min([grid.depth.actual_range[0] for grid in subduction_zones])

# Plot the depth of each subducting plate inside Slab2 with the same colorscale
for grid in subduction_zones:
    pc = grid.depth.plot.pcolormesh(
        cmap=cmocean.cm.thermal_r,
        ax=ax,
        transform=ccrs.PlateCarree(),
        add_colorbar=False,
        vmin=vmin,
        vmax=vmax,
    )

ax.set_title("Slab2: Geometry model for subduction zones")
cb = plt.colorbar(
    pc, ax=ax, label="Depth (meters)", pad=0.05, aspect=40, orientation="horizontal"
)
ax.set_global()
ax.coastlines()
plt.show()
