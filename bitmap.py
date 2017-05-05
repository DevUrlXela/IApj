from PIL import Image
import numpy as np
import webcolors as webcolors


def displayImage(image):
    displayList=np.array(image).T
    im1 = Image.fromarray(displayList)
    im1.show()

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def buscarDato(nombre):
    cont=0
    for dato in lista_nombreReal:
        if dato  == nombre:
            cont = 1
    if cont != 1:
        lista_nombreReal.append(nombre)








im2 = Image.open('reconocimientoColor/cortar.jpg')
im = im2.convert("RGB")
global lista_nombreReal
global lista_nombreCercano

lista_nombreReal = ['hola']


pixels = list(im.getdata())
width, height = im.size

# print (width)
# print (height)


for dato in range(4900):
    actual_name, closest_name = get_colour_name(pixels[dato])
    buscarDato(closest_name)
        #print(actual_name)


    #print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)
print (lista_nombreReal)
print(len(lista_nombreReal))
