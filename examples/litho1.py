"""
LITHO1.0 - An updated crust and lithospheric model of the Earth
===============================================================
The LITHO1.0 model is a 1° tessellated model of the crust and uppermost
mantle of the earth, extending into the upper mantle to include the
lithospheric lid and underlying asthenosphere.

Each of the nodes has a unique profile where the layers are:
    - water
    - ice
    - upper sediments
    - middle sediments
    - lower sediments
    - upper crust
    - middle crust
    - lower crust
    - lithospheric mantle (lid)
    - asthenospheric mantle
    - ak135

More information at the
`model <https://igppweb.ucsd.edu/~gabi/litho1.0.html>`__
website.
"""

import rockhound as rh
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cmocean

# Fetch all LiTHO model
litho = rh.fetch_litho1()

# Save as NetCDF
litho.to_netcdf("~/temp/litho1.nc")

# The model has different boundaries, so we only plot the
# lithospheric mantle boundary (LID)
lid = litho.loc[dict(boundary="LID-TOP")]
plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.Robinson())
pc = plt.scatter(
    lid.longitude,
    lid.latitude,
    c=lid.depth.values,
    cmap=cmocean.cm.thermal_r,
    transform=ccrs.PlateCarree(),
)
ax.set_title("LAB depth from LITHO1.0 model")
plt.colorbar(
    pc,
    label="Depth (meters)",
    pad=0.05,
    aspect=40,
    shrink=0.7,
    orientation="horizontal",
)
ax.set_global()
ax.coastlines()
plt.show()
