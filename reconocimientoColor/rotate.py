from PIL import Image
img = Image.open("banana_new.jpg")
img2 = img.rotate(45)
img2.save("img2.jpg")
