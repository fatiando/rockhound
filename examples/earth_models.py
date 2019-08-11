import rockhound as rh
import matplotlib.pyplot as plt

r"""
PREM: Preliminary Reference Earth Model
=======================================

The Preliminary reference Earth model (PREM) [Dziewonsky1981]_ is a one-dimensional
model representing the average Earth properties as a function of planetary radius.  The
model includes the depth, density, seismic velocities, attenuation (Q) and anisotropic
parameter (:math:`\eta`) on the boundaries of several Earth layers.  The data is loaded
into :class:`pandas.DataFrame` objects, which can be used to plot and make computations.
"""

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

r"""
ak135-f:
========

The ak135-f Earth model [Kennett1995]_ is a variant of the ak135 Earth model
with the density and Q model from [Montagner1996]_ added.
The ak135-f Earth model is a one-dimensional model representing average Earth properties as a
function of depth. The model includes the depth, density, seismic velocities and attenuation (Q)
on the boundaries of several Earth layers. It's available through IRIS Data Services Products
[IRIS2011]_ in a csv file (comma-separated values). The data is loaded into
:class:`pandas.DataFrame` objects.
"""

# Load ak135f into a DataFrame
ak135f = rh.fetch_ak135f()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("ak135-f")
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

r"""
IASP91:
=======

IASP91 [Kennett1991]_ is a widely used one-dimensional model representing average Earth properties
as a function of depth. This model has parameters for depth, radius, P-wave velocity and S-wave
velocity. It's available through IRIS Data Services Products [IRIS2011]_ in a csv file
(comma-separated values). The data is loaded into :class:`pandas.DataFrame` objects.
"""

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

r"""
MEAN:
=====

The MEAN Earth model is a variant of the IASP91 Earth model. MEAN [Marone 2004]_ is a
one-dimensional earth model representing average Earth properties as a function of Earth radius.
This model has parameters for radius, density, P-wave velocity, S-wave velocity, and attenuation
(Q).It's available through IRIS Data Services Products [IRIS2011]_ in a nc file (netCDF). The data
is loaded into :class:`pandas.DataFrame` objects.
"""

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

r"""
PEM-A: Average Parametric Earth Model
=====================================

The PEM-A Earth model [Dziewonsky1975]_ is a weighted average of both the
PEM-O Earth model and the PEM-C Earth model. It is a one-dimensional model
representing average Earth properties as a function of depth. The model
includes the radius, depth, density, P-wave velocity, and S-wave velocity on the boundaries of
several Earth layers. It's available through IRIS Data Services Products [IRIS2011]_
in a csv file (comma-separated values). The data is loaded into
:class:`pandas.DataFrame` objects.
"""

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

r"""
PEM-C: Continental Parametric Earth Model
=========================================

The PEM-C Earth model [Dziewonsky1975]_ is a one-dimensional model representing average continental
Earth properties as a function of depth. The model includes the radius, depth, density, P-wave
velocity, and S-wave velocity on the boundaries of several Earth layers. It's available through
IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values). The data is loaded
into :class:`pandas.DataFrame` objects.
"""

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

r"""
PEM-O: Oceanic Parametric Earth Model
=====================================

The PEM-O Earth model [Dziewonsky1975]_ is a one-dimensional model representing average oceanic
Earth properties as a function of radius and depth. The model includes radius, depth, density,
P-wave velocitiy, and S-wave velocity on the boundaries of several Earth layers. It's available
through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values).
The data is loaded into :class:`pandas.DataFrame` objects.
"""

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

r"""
MC35:
=====

The MC35 Earth model [VanderLee1997]_ is a one-dimensional model based off of the PEM-C. This model
represents average Earth properties as a function of depth. The model includes the depth and S-wave
velocities on the boundaries of several Earth layers. It's available through IRIS Data Services
Products [IRIS2011]_ in a csv file (comma-separated values). The data is loaded into
:class:`pandas.DataFrame` objects.
"""

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

r"""
STW105:
=======

The STW105 Earth model [Kustowski2008]_ is a one-dimensional model representing average Earth
properties as a function of depth. The model includes the radius, density, seismic velocities,
attenuation (Q), and anisotropic parameter (:math:`\eta`) on the boundaries of several Earth layers.
It's available through IRIS Data Services Products [IRIS2011]_ in a txt file (text).
The data is loaded into :class:`pandas.DataFrame` objects.
"""

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
stw105.plot("eta", "radius", legend=False, ax=ax)
ax.set_xlabel("eta")
ax.set_ylabel("Radius [m]")

r"""
TNA/SNA: Tectonic North America/Shield North America
====================================================

The TNA/SNA Earth model [Simmons2010]_ is a one-dimensional model based off of the S velocity models
of [Grand1984]_. This model represents average Earth properties as a function of depth. The model
includes radius and S-wave velocities on the boundaries of several Earth layers. It's available
through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values).
The data is loaded into :class:`pandas.DataFrame` objects.
"""

# load TNA/SNA into a DataFrame
tna_sna = rh.fetch_tna_sna()

# Plot density and velocities
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
fig.suptitle("TNA/SNA")
tna_sna.plot("Vs", "radius", legend=False, ax=ax, label="Vs")
ax.grid()
ax.legend()
ax.set_ylabel("Radius [km]")
ax.set_xlabel("Velocity [km/s]")
plt.show()
