from tkinter import *
import cv2
from PIL import ImageTk, Image

def funcion(event):
    print("funcion1")
    root.destroy()

def funcion2(event):
    print("funcion2")

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))



global root
root = Tk()
root.title("Labeler")
root.geometry("1050x600")

imagen=cv2.imread('banana.jpg')
cv2.imwrite('ventana/opcion1_resize.jpg',imagen)

img = ImageTk.PhotoImage(Image.open('ventana/opcion1_resize.jpg'))

panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
app = Frame(root)
app.grid()
label = Label(app, text="Elige la opcion que mejor detecto el banano")
panel.grid()
root.bind('<Button-1>', motion)

root.mainloop()
