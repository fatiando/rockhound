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
import cartopy.crs as ccrs

# Load both the ice surface and bedrock grids and merge them into a single Dataset
grid = rh.fetch_etopo1(version="ice")
grid = grid.merge(rh.fetch_etopo1(version="bedrock"))
print("Entire dataset:\n\n", grid)

# Select a subset of this large grid that corresponds to Iceland and Greenland
iceland = grid.sel(latitude=slice(55, 80), longitude=slice(-50, -10))
print("\nIceland subsection:\n\n", iceland)

# Make maps of both versions using an Albers Equal Area projection
proj = ccrs.AlbersEqualArea(central_longitude=-30, central_latitude=67.5)
trans = ccrs.PlateCarree()

# Setup some common arguments for the colorbar and pseudo-color plot
cbar_kwargs = dict(pad=0, orientation="horizontal")
pcolor_args = dict(cmap="terrain", add_colorbar=False, transform=ccrs.PlateCarree())

# Draw the maps
fig, axes = plt.subplots(1, 2, figsize=(9, 5), subplot_kw=dict(projection=proj))
fig.suptitle("ETOPO1 Earth Relief of Iceland and Greenland")
ax = axes[0]
tmp = iceland.ice.plot.pcolormesh(ax=ax, **pcolor_args)
plt.colorbar(tmp, ax=ax, **cbar_kwargs).set_label("[meters]")
ax.gridlines()
ax.set_title("Ice Surface")
ax = axes[1]
tmp = iceland.bedrock.plot.pcolormesh(ax=ax, **pcolor_args)
plt.colorbar(tmp, ax=ax, **cbar_kwargs).set_label("[meters]")
ax.gridlines()
ax.set_title("Bedrock")
plt.tight_layout()
plt.show()
