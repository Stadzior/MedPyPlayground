import SimpleITK as sitk
import numpy as np
from PIL import Image
import os
'''
This funciton reads a '.mhd' file using SimpleITK and return the image array, origin and spacing of the image.
'''
def load_itk(filename):
    # Reads the image using SimpleITK
    itkimage = sitk.ReadImage(filename)

    # Convert the image to a  numpy array first and then shuffle the dimensions to get axis in the order z,y,x
    ct_scan = sitk.GetArrayFromImage(itkimage)

    # Read the origin of the ct_scan, will be used to convert the coordinates from world to voxel and vice versa.
    origin = np.array(list(reversed(itkimage.GetOrigin())))

    # Read the spacing along each dimension
    spacing = np.array(list(reversed(itkimage.GetSpacing())))

    return ct_scan, origin, spacing

oldMin = -3024
oldMax = 0
newMin = 0
newMax = 255

def arrayToRgbArray(value):
    oldRange = (oldMax - oldMin)  
    newRange = (newMax - newMin)  
    pixelValue = (((value - oldMin) * newRange) / oldRange) + newMin
    return [pixelValue, pixelValue, pixelValue]

os.chdir("./mhdraw")
for file in filter(lambda x: x.endswith(".mhd"), os.listdir(".")):
    [ctScan, origin, spacing] = load_itk(file)
    print("-----------------CT SCAN-----------------")
    (height, width, depth) = ctScan.shape
    print("Dims: {}, {}, {}".format(height, width, depth))
    img = Image.frombuffer("I", (512,512), ctScan)
    img.show()
    print("-----------------ORIGIN-----------------")
    print(origin)
    print("-----------------SPACING-----------------")
    print(spacing)
