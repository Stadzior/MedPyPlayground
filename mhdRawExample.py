import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
import skimage.io as io

os.chdir("./mhdraw")

oldMin = -1024
oldMax = 701
newMin = 0
newMax = 255
oldRange = (oldMax - oldMin)  
newRange = (newMax - newMin)  

for file in filter(lambda x: x.endswith(".raw"), os.listdir(".")):
    f = open(file, 'rb')
    img_str = f.read()

    isMask = "MM" in file
    # converting to a int16 numpy array
    ct_image_as_vector = np.fromstring(img_str, dtype=np.int8) if isMask else np.fromstring(img_str, np.int16)

    #layering
    layer_dimensions = (512, 512)
    layer_size = layer_dimensions[0]*layer_dimensions[1]
    layers_count = int(len(ct_image_as_vector) / layer_size)
    ct_image_layered = np.reshape(ct_image_as_vector, (layers_count, layer_size))

    # get the image and plot it
    layer = ct_image_layered[200]    
    #layer.byteswap(inplace=True)
    layer = np.reshape(layer, (512, 512))
    normalize = lambda x: int((((x - oldMin) * newRange) / oldRange) + newMin)
    npNormalize = np.vectorize(normalize)
    layer8int = npNormalize(layer).astype(np.int8)
    plt.imshow(layer, cmap=plt.cm.gray)
    plt.show()
    image = Image.fromarray(layer8int, "L") #https://stackoverflow.com/questions/47290668/image-fromarray-just-produces-black-image
    image.save("{0}_pil.png".format(file), "PNG")
