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
    ct_image_as_vector = np.fromstring(img_str, np.int16)

    #layering
    layer_dimensions = (512, 512)
    layer_size = layer_dimensions[0]*layer_dimensions[1]
    layers_count = int(len(ct_image_as_vector) / layer_size)
    ct_image_layered = np.reshape(ct_image_as_vector, (layers_count, layer_size))
    # get the image and plot it
    layer = ct_image_layered[200]
    
    #layer.byteswap(inplace=True)
    layer = np.reshape(layer, (512, 512))
    plt.imshow(layer, cmap=plt.cm.gray)
    plt.show()