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

# Load a geometry of the Alaska subduction zone
grid = rh.fetch_slab2(zone="alaska")
print(grid)

# Plot the age grid.
# We're not using a map projection to speed up the plotting but this NOT recommended.
plt.figure(figsize=(9, 8))
ax = plt.subplot(111)
grid.depth.plot.pcolormesh(
    cmap=cmocean.cm.thermal_r, cbar_kwargs=dict(pad=0.01, aspect=30), ax=ax
)
plt.tight_layout()
plt.show()
