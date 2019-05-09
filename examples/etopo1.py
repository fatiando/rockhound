"""
ETOPO1 Earth Relief
===================

ETOPO1 is a 1 arc-minute global relief model of Earth's surface that integrates land
topography and ocean bathymetry [AmanteEakins2009]_. It's available in two versions:
"Ice Surface" (top of Antarctic and Greenland ice sheets) and "Bedrock" (base of the ice
sheets). The grids are loaded into :class:`xarray.Dataset` which can be used to plot
and make computations.
"""
import rockhound as rh
import matplotlib.pyplot as plt
import cmocean

# Load a version of the topography grid
grid = rh.fetch_etopo1(version="bedrock")
print(grid)

# Select a subset that corresponds to Africa to make plotting faster given the size of
# the grid.
africa = grid.sel(latitude=slice(-40, 45), longitude=slice(-20, 60))

# Plot the age grid.
# We're not using a map projection to speed up the plotting but this NOT recommended.
plt.figure(figsize=(9, 8))
ax = plt.subplot(111)
africa.bedrock.plot.pcolormesh(
    cmap=cmocean.cm.topo, cbar_kwargs=dict(pad=0.01, aspect=30), ax=ax
)
ax.set_title("ETOPO1")
plt.tight_layout()
plt.show()
