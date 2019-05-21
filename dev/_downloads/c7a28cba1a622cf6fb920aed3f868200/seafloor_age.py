"""
Age of the Oceanic Lithosphere
==============================

Global grids of the age of the oceanic lithosphere produced by [Muller2008]_.
Available in 2 and 6 arc-minute resolutions and include grids of the age uncertainty.
More information at the
`NOAA NCEI <https://www.ngdc.noaa.gov/mgg/ocean_age/ocean_age_2008.html>`__ and
`EarthByte <http://www.earthbyte.org/age-spreading-rates-and-spreading-asymmetry-of-the-worlds-ocean-crust/>`__
websites.
"""
import rockhound as rh
import matplotlib.pyplot as plt
import cmocean

# Load the age and uncertainty grids in the default 6 arc-minute resolution
grid = rh.fetch_seafloor_age()
print(grid)

# Plot the age grid.
# We're not using a map projection to speed up the plotting but this NOT recommended.
plt.figure(figsize=(9, 5))
ax = plt.subplot(111)
grid.age.plot.pcolormesh(
    cmap=cmocean.cm.thermal_r, cbar_kwargs=dict(pad=0.01, aspect=30), ax=ax
)
ax.set_title("Age of Oceanic Lithosphere")
plt.tight_layout()
plt.show()
