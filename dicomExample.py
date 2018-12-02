import os
import pydicom
from pydicom.data import get_testdata_files
os.chdir("./dicom")
for file in filter(lambda x: x.endswith(".dcm"), os.listdir(".")):
    ds = pydicom.dcmread(file)  # plan dataset
    print(ds.PatientName)
    print(ds)
    print(ds.dir("setup"))    # get a list of tags with "setup" somewhere in the name
    ds.save_as("./output"+ file)

