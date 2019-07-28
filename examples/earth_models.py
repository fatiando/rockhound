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

# load MEAN into a DataFrame
mean = rh.fetch_mean()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("MEAN")
ax = axes[0]
mean.plot("density", "radius", legend=False, ax=ax)
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

# load PEMA into a DataFrame
pema = rh.fetch_pema()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("PEMA")
ax = axes[0]
pema.plot("density", "radius", legend=False, ax=ax)
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Radius [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vp", "Vs"]:
    pema.plot(velocity, "radius", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()

# load PEMC into a DataFrame
pemc = rh.fetch_pemc()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("PEMC")
ax = axes[0]
pemc.plot("density", "radius", legend=False, ax=ax)
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Radius [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vp", "Vs"]:
    pemc.plot(velocity, "radius", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()

# load PEMO into a DataFrame
pemo = rh.fetch_pemo()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("PEMO")
ax = axes[0]
pemo.plot("density", "radius", legend=False, ax=ax)
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Radius [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vp", "Vs"]:
    pemo.plot(velocity, "radius", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()

# load MC35 into a DataFrame
mc35 = rh.fetch_mc35()

# Plot density and velocities
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
fig.suptitle("MC35")
mc35.plot("Vs", "depth", legend=False, ax=ax, label="Vs")
ax.invert_yaxis()
ax.grid()
ax.legend()
ax.set_ylabel("Depth [km]")
ax.set_xlabel("Velocity [km/s]")
plt.show()

# load STW105 into a DataFrame
stw105 = rh.fetch_stw105()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("STW105")
ax = axes[0]
stw105.plot("density", "radius", legend=False, ax=ax)
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Radius [m]")
ax.grid()
ax = axes[1]
for velocity in ["Vpv", "Vsv", "Vph", "Vsh"]:
    stw105.plot(velocity, "radius", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()

fig, ax = plt.subplots()
# ax = axes[0]
stw105.plot("eta", "radius", legend=False, ax=ax)  ## Some QC required?
ax.invert_yaxis()
#%%
# load MC35 into a DataFrame
tna_sna = rh.fetch_tna_sna()

# Plot density and velocities
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
fig.suptitle("TNA/SNA")
tna_sna.plot("Vs", "radius", legend=False, ax=ax, label="Vs")
# ax.invert_yaxis()
ax.grid()
ax.legend()
ax.set_ylabel("Radius [km]")
ax.set_xlabel("Velocity [km/s]")
plt.show()

#%%
# import pandas as pd
# fname = '/home/chet/Desktop/fatiando/rockhound/rockhound/data_to_delete/dat/STW105.txt'#REGISTRY.fetch("STW105.txt")
##if not load:
#    #return fname
##stw105 = pd.read_fwf(fname)
##stw105 = pd.read_csv(fname, sep=None, skiprows=4)
# data = np.loadtxt(fname, skiprows=3)
# columns = ["radius",
#           "density",
#           "Vpv",
#           "Vsv",
#           "Q_kappa",
#           "Q_mu",
#           "Vph",
#           "Vsh",
#           "eta"]
# stw105 = pd.DataFrame(data, columns=columns)
# return stw105
