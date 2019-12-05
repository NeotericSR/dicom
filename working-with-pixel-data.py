import pydicom
from pydicom.data import get_testdata_files

# load dicom file
filename = get_testdata_files("MR_small.dcm")[0]

# read loaded dicom file with dcmread to create a dataset
ds = pydicom.dcmread(filename)

# access the dataset PixelData property to retrieve the raw pixels
raw = ds.PixelData

# the flat property belongs to numpy and collapses the array into one dimension
for n,val in enumerate(ds.pixel_array.flat): # example: zero anything < 300
    if val < 300:
        ds.pixel_array.flat[n] = 0
        
# convert the array to bytes or raw pixels
ds.PixelData = ds.pixel_array.tobytes()
ds.save_as("newfilename.dcm")

import os
os.remove("newfilename.dcm")
