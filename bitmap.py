from PIL import Image
import numpy as np

def displayImage(image):
    displayList=np.array(image).T
    im1 = Image.fromarray(displayList)
    im1.show()


im2 = Image.open('test1.png')
im = im2.convert("RGB")

pixels = list(im.getdata())
width, height = im.size

print (width)
print (height)

print (pixels)

displayImage(pixels)
