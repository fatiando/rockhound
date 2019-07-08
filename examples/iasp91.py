r"""
IASP91: International Association of Seismology and Physics of the Earth's Interior Earth model
=======================================

IASP91 [Kennett1991]_ is a one-dimensional model representing Earth properties as
a function of depth or radius. This model has parameters for depth, radius, P-wave 
velocity and S-wave velocity.It's available through IRIS Data Services Products [IRIS2011]_ in a csv file
(comma-separated values). The data is loaded into :class:`pandas.DataFrame` objects, which can be used to plot and make computations.

"""
import rockhound as rh
import matplotlib.pyplot as plt

# Load IASP91 into a DataFrame
iasp91 = rh.fetch_iasp91()
print(iasp91)

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

