import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files

filename = get_testdata_files("CT_small.dcm")[0]
ds = pydicom.dcmread(filename)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
