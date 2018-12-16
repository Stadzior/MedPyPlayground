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

def arrayToRgbArray(value):
    pixelValue = 255-(1000-value)
    pixelValue = pixelValue if pixelValue > 0 else 0
    pixelValue = pixelValue if pixelValue < 255 else 255
    return [pixelValue, pixelValue, pixelValue]

os.chdir("./mhdraw")
for file in filter(lambda x: x.endswith(".mhd"), os.listdir(".")):
    [ctScan, origin, spacing] = load_itk(file)
    print("-----------------CT SCAN-----------------")
    (height, width, depth) = ctScan.shape
    print("Dims: {}, {}, {}".format(height, width, depth))
    for ctScan2d in ctScan[32:52]:
        print(ctScan2d) 
        ctScan2dRgb = np.asarray(list(map(lambda row: np.asarray(list(map(arrayToRgbArray, row))), ctScan2d)))
        print(ctScan2dRgb)
        img = Image.fromarray(ctScan2dRgb, 'RGB')
        img.show()
    print("-----------------ORIGIN-----------------")
    print(origin)
    print("-----------------SPACING-----------------")
    print(spacing)
