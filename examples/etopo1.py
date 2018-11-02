"""
ETOPO1 Earth Relief
===================

ETOPO1 is a 1 arc-minute global relief model of Earth's surface that integrates land
topography and ocean bathymetry [AmanteEakins2009]_. It's available in two versions:
"Ice Surface" (top of Antarctic and Greenland ice sheets) and "Bedrock" (base of the ice
sheets).
"""
import matplotlib.pyplot as plt
import rockhound as rh

grid = rh.fetch_etopo1(version="ice")
print(grid)

plt.figure(figsize=(13.5, 6))
# Downsample the grid a bit so we can plot it quickly for this example.
# NEVER do this in practice because it may introduce aliasing effects.
grid[::60, ::60].plot.pcolormesh(cmap=plt.cm.terrain, cbar_kwargs=dict(pad=0.01))
plt.axis("scaled")
plt.tight_layout()
plt.show()
