import SimpleITK as sitk
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

os.chdir("./mhdraw")
for file in filter(lambda x: x.endswith(".raw"), os.listdir(".")):
    f = open(file, 'rb')
    img_str = f.read()

    # converting to a uint16 numpy array
    img_arr = np.fromstring(img_str, np.uint16)
    # get the first image and plot it
    im1 = img_arr[512*512*46:512*512*47]
    
    #im1.byteswap(inplace=True)
    im1 = np.reshape(im1, (512, 512))
    plt.imshow(im1, cmap=plt.cm.gray_r)
    plt.show()