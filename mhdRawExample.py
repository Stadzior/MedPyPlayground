import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
import skimage.io as io

os.chdir("./mhdraw")

for file in filter(lambda x: x.endswith(".raw"), os.listdir(".")):
    f = open(file, 'rb')
    img_str = f.read()

    # converting to a int16 numpy array
    ct_image_as_vector = np.fromstring(img_str, dtype=np.int8) if "MM" in file else np.fromstring(img_str, np.int16)

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
    plt.figure()
    plt.savefig("{0}_matplotlib.png".format(file))
    image = Image.fromarray(layer, "1")
    image.save("{0}_pil.png".format(file), "PNG")
    io.imsave("{0}_skimage.png".format(file), layer)