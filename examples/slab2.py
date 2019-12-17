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

# Load a geometry of the Alaska subduction zone
grid = rh.fetch_slab2(zone="south_america")
print(grid)

# Plot the sibductin zones using cartopy
plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.Robinson())
pc = grid.depth.plot.pcolormesh(
    cmap=cmocean.cm.thermal_r,
    cbar_kwargs=dict(pad=0.01, aspect=30),
    ax=ax,
    transform=ccrs.PlateCarree(),
)
# make the map global rather than have it zoom in to the extents of any plotted data
ax.set_global()
ax.coastlines()
plt.show()
