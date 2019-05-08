"""
Bedmap2
=======

Bedmap2 is a suite of gridded products describing surface elevation, ice-thickness, the
sea floor and subglacial bed elevation of the Antarctic south of 60°S [BEDMAP2]_.
Each dataset is projected in Antarctic Polar Stereographic projection, latitude of true
scale -71 degrees south, datum WGS84. All heights are in metres relative to sea level as
defined by the g104c geoid. The datasets are downloaded as ``tiff`` files and loaded
into a :class:`xarray.Dataset` object.
"""
import rockhound as rh
import matplotlib.pyplot as plt
import cmocean

# Load the ice thickness grid
bedmap = rh.fetch_bedmap2(datasets=["thickness"])
# bedmap = bedmap.sel(x=slice(None, 0), y=slice(0, None))
print(bedmap)

plt.figure(figsize=(8, 9.5))
ax = plt.subplot(111)
pc = bedmap.thickness.plot.pcolormesh(ax=ax, cmap=cmocean.cm.ice, add_colorbar=False)
plt.colorbar(pc, ax=ax, orientation="horizontal", pad=0.05, aspect=50, label="meters")
ax.set_title("Bedmap2 Antarctica Ice Thickness")
plt.tight_layout()
plt.show()
