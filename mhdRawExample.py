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

np.set_printoptions(threshold=np.nan)
os.chdir("./mhdraw")
for file in filter(lambda x: x.endswith(".mhd"), os.listdir(".")):
    [ct_scan, origin, spacing] = load_itk(file)
    print("-----------------CT SCAN-----------------")
    print("Dims:{}".format(ct_scan.shape))
    oneDimImage = ct_scan[242]
    print(ct_scan[242])
    boolToRgb = lambda value : [255,255,255] if value == 1 else [0,0,0]
    boolToRgbVec = np.vectorize(boolToRgb)
    rgb_ct_scan = boolToRgbVec(ct_scan[242])
    img = Image.fromarray(oneDimImage, 'RGB')
    print("-----------------ORIGIN-----------------")
    print(origin)
    print("-----------------SPACING-----------------")
    print(spacing)
