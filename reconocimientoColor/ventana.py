from tkinter import *
import cv2
from PIL import ImageTk, Image



root = Tk()
root.title("Labeler")
root.geometry("1050x600")



imagen=cv2.imread('bananaFinal.jpg')
imagen = cv2.resize(imagen,(400, 400))
cv2.imwrite('ventana/opcion1.jpg',imagen)
img = ImageTk.PhotoImage(Image.open('ventana/opcion1.jpg'))

panel = Label(root, image = img)
panel2 = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
app = Frame(root)
app.grid()
label = Label(app, text="Elige la opcion que mejor detecto el banano")

boton1 = Button(app,text="OPCION 1")
boton2 = Button(app,text="OPCION 2")

label.config(font=30)
label.grid(row=0, column=200)
boton1.grid(row=1, column=150)
boton2.grid(row=1, column=200)

panel.config(height=500)
panel.grid(row=40)

panel2.config(height=500)
panel2.grid(row=40,column=80)

root.mainloop()
