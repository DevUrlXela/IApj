from PIL import Image
import numpy as np
import webcolors as webcolors
from os import listdir

redcolors = (
'lightsalmon',
'salmon',
'darksalmon',
'lightcoral',
'indianred',
'crimson',
'firebrick',
'darkred',
'red'
)

orangecolors = (
'orangered',
'tomato',
'coral',
'darkorange',
'orange'
)


verdeOscuro = (
'darkolivegreen',
'olive',
'olivedrab',
'yellowgreen',
'limegreen',
'darkseagreen',
'mediumaquamarine',
'mediumseagreen',
'seagreen',
'forestgreen',
'green',
'darkgreen'
)


verdeClaro = (
'lime',
'lawngreen',
'chartreuse',
'greenyellow',
'springgreen',
'mediumspringgreen',
'lightgreen',
'palegreen'
)


amarillosC = (
'lightyellow',
'lemonchiffon',
'lightgoldenrodyellow',
'papayawhip',
'moccasin',
'peachpuff',
)

amarillosO = (
'yellow',
'lightyellow',
'palegoldenrod',
'khaki',
'darkkhaki',
'goldenrod',
)


brown = (
'darkgoldenrod',
'peru',
'chocolate',
'saddlebrown',
'sienna',
'brown',
'maroon',
)

black = (
'silver',
'darkgray',
'gray',
'dimgray',
'lightslategray',
'slategray',
'darkslategray',
'black'
)


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




im2 = Image.open('reconocimientoColor/cortar.jpg')
im = im2.convert("RGB")

pixels = list(im.getdata())
contRed = 0
contOrange = 0
contDarkGreen = 0
contLightGreen = 0
contLightYellow = 0
contDarkYellow = 0
contBrown = 0
contBlack = 0

for dato in range(4900):
    actual_name, closest_name = get_colour_name(pixels[dato])
    # buscarDato(closest_name)
    #print(actual_name)
    for iterador in range(len(redcolors)):
        if closest_name is redcolors[iterador]:
            contRed += 1

    for iterador in range(len(orangecolors)):
        if closest_name is orangecolors[iterador]:
            contOrange += 1

    for iterador in range(len(verdeOscuro)):
        if closest_name is verdeOscuro[iterador]:
            contDarkGreen += 1

    for iterador in range(len(verdeClaro)):
        if closest_name is verdeClaro[iterador]:
            contLightGreen += 1

    for iterador in range(len(amarillosC)):
        if closest_name is amarillosC[iterador]:
            contLightYellow += 1

    for iterador in range(len(amarillosO)):
        if closest_name is amarillosO[iterador]:
            contDarkYellow += 1

    for iterador in range(len(brown)):
        if closest_name is brown[iterador]:
            contBrown += 1

    for iterador in range(len(black)):
        if closest_name is black[iterador]:
            contBlack += 1


contRed = (contRed * 100) / 4900
contOrange = (contOrange * 100) / 4900
contDarkGreen = (contDarkGreen * 100) / 4900
contLightGreen = (contLightGreen * 100) / 4900
contLightYellow = (contLightYellow * 100) / 4900
contDarkYellow = (contDarkYellow * 100) / 4900
contBrown = (contBrown * 100) / 4900
contBlack = (contBlack * 100) / 4900


arrayFotos = []
print ("Rojo:               ","%.2f" %contRed + "%")
print ("Naranja:            ","%.2f" %contOrange + "%")
print ("Verde Oscuro:       ","%.2f" %contDarkGreen + "%")
print ("Verde Claro:        ","%.2f" %contLightGreen + "%")
print ("Amarillo Claro:     ","%.2f" %contLightYellow + "%")
print ("Amarillo Oscuro:    ","%.2f" %contDarkYellow + "%")
print ("Cafe:               ","%.2f" %contBrown + "%")
print ("Negro:              ","%.2f" %contBlack + "%")


for cosa in listdir("."):
    if cosa[-4:] == ".jpg":
        arrayFotos.append(cosa)

for iterador in range(len(arrayFotos)):
    print (arrayFotos[iterador])
