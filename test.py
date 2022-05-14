import math
import numpy as np

color1 = (10,12,77)
color2 = (89,255,66)
color3 = (75,30,255)

puntooo = [6,5,1]

vector = [[3,3,3],[8,8,8]]

plano = [[5,-2,3],
		[4,4,-2],
		[1,2,3],
		[2,10,3]]

fig_1 = ["caja",plano,color1]
fig_2 = ["punto",puntooo,color2]
fig_3 = ["vector",vector,color3]

figuras = [fig_1,fig_2]

figuras.append(fig_3)
print(figuras)

from tkinter import *

win = Tk()

win.geometry("500x250")

frame= Frame(win)

text= Text(frame)

text.insert(INSERT, "Hey!!, You can Start Python Programming Now")

text.pack()

text.tag_add("start", "0.1", "2.0")

text.tag_configure("start", background= "black", foreground= "red")

frame.pack()

win.mainloop()