r"""
PREM: Preliminary Reference Earth Model
=======================================

The Preliminary reference Earth model (PREM) [Dziewonsky1981]_ is a one-dimensional
model representing the average Earth properties as a function of planetary radius.  The
model includes the depth, density, seismic velocities, attenuation (Q) and anisotropic
parameter (:math:`\eta`) on the boundaries of several Earth layers.  The data is loaded
into :class:`pandas.DataFrame` objects, which can be used to plot and make computations.
"""
import rockhound as rh
import matplotlib.pyplot as plt

# Load PREM into a DataFrame
prem = rh.fetch_prem()
# print(prem)

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("PREM: Preliminary Reference Earth Model")
ax = axes[0]
prem.plot("density", "depth", legend=False, ax=ax)
ax.invert_yaxis()
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Depth [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vpv", "Vph", "Vsv", "Vsh"]:
    prem.plot(velocity, "depth", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()

# Load ak135f into a DataFrame
ak135f = rh.fetch_ak135f()
# print(ak135f)

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("ak135f")
ax = axes[0]
ak135f.plot("density", "depth", legend=False, ax=ax)
ax.invert_yaxis()
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Depth [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vp", "Vs"]:
    ak135f.plot(velocity, "depth", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()

# Load IASP91 into a DataFrame
iasp91 = rh.fetch_iasp91()
# print(iasp91)

# Plot density and velocities
fig, ax = plt.subplots(1, 1, figsize=(9, 5), sharey=True)
fig.suptitle("IASP91")
for velocity in ["Vp", "Vs"]:
    iasp91.plot(velocity, "depth", legend=False, ax=ax, label=velocity)
ax.invert_yaxis()
ax.grid()
ax.legend()
ax.set_ylabel("Depth [km]")
ax.set_xlabel("Velocity [km/s]")
plt.show()

#import os
#print(os.getcwd())
#%%
#from netCDF4 import Dataset
#import pandas as pd

#import xarray as xr
#
#dat = xr.open_dataset('MEAN.nc')
##my_df = dat.reset_index(dims_or_levels=index)
#df = dat.to_dataframe()
#my_df = df.reset_index()
#my_df.columns = ['radius', 'depth', 'Vp', 'Vs', 'Q_kappa', 'Q_mu']
#dat = Dataset('MEAN.nc')
#print(dat.variables.keys())
#print(dat.variables['radius'][20])
#pd_dat = dat.to_dataframe()
#pd_dat = pd.DataFrame(dat)
#pd_dat = pd.read_csv('MEAN.nc')

#%%

#load MEAN into a DataFrame
mean = rh.fetch_mean()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("MEAN")
ax = axes[0]
mean.plot("density", "radius", legend=False, ax=ax)
#ax.invert_yaxis()
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Radius [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vp", "Vs"]:
    mean.plot(velocity, "radius", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()
