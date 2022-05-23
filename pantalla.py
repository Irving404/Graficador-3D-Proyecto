import tkinter as tk
import tkinter
from tkinter import * 
from tkinter import colorchooser
import plano
import pygame  
import re
import math
import random

l_b = 12
l_e = 10
l_en = 15
l_t = 10
color_code=((0,0,255),('#0000ff'))
arr_cor = []
contador = 0.5

def limpiar_pantalla():
	plano.inicia_todo()

def choose_color():
    global color_code
    color_code = colorchooser.askcolor(title ="Choose color")
    color_et.config(bg=color_code[1])

def pinta_punto():
	x_p = float(x_txt.get())
	y_p = float(y_txt.get())
	z_p = float(z_txt.get())
	point = [x_p,y_p,z_p]
	plano.pinta_figura('punto',point,color_code[0])
	agrega_figura("PUNTO")
	

def pinta_plano():
	points = secciona(parsea(get_coordenadas()))
	plano.pinta_figura('plano',points,color_code[0])
	agrega_figura("PLANO")

def pinta_caja():
	points = secciona(parsea(get_coordenadas()))
	plano.pinta_figura('caja',points,color_code[0])
	agrega_figura("CAJA")

def pinta_vector():
	x_p = float(x_txt.get())
	y_p = float(y_txt.get())
	z_p = float(z_txt.get())
	x1_p = float(x1_txt.get())
	y1_p = float(y1_txt.get())
	z1_p = float(z1_txt.get())
	points = [[x_p,y_p,z_p],[x1_p,y1_p,z1_p]]
	plano.pinta_figura('vector',points,color_code[0])
	agrega_figura("VECTOR")

def pinta_todos():
	points = secciona(parsea(get_coordenadas()))
	plano.pinta_figura('todos',points,color_code[0])
	agrega_figura("FIGURA")
	
def genera_fun():
	tamaño = 15
	ava = 1

	points = []
	valores = []
	cambio = int(255/(tamaño*tamaño))
	dic = {}
	x = 0
	ii = 0
	while x<=tamaño:
		y = 0
		while y<=tamaño:
			z = math.sin(x)
			#z = x*x
			points.append([x,y,z])
			if not(z in valores):
				valores.append(z)
			y +=ava
		ii +=1
		x += ava
	valores = sorted(valores)
	for i in valores:
		dic.setdefault(i,get_color())
	colores=[ii]
	for i in points:
		colores.append(dic.get(i[2]))
	plano.pinta_figura('funcion',points,colores)



def get_color():
	return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def cargar_archivo():
    global arr_cor
    archivo = open("Coordenadas.txt")
    texto = (archivo.read())
    archivo.close()
    textoo = re.sub('\n', ',', texto)
    arr_cor = re.split(r',', textoo)
    T.delete('1.0', END) 
    T.insert(tk.END, texto)

def get_coordenadas():
    global arr_cor
    texto = T.get("1.0",END)
    textoo = re.sub('\n', ',', texto)
    arr_cor = re.split(r',', textoo)
    arr_cor = arr_cor[:len(arr_cor)-1]
    return arr_cor

def parsea(arr):
	arr_aux = []
	for i in arr:
		arr_aux.append(float(i))
	return arr_aux

def secciona(arr):
	arr_f = []
	cont = 0
	arrr = []
	for i in arr:
		if cont == 3:
			arr_f.append(arrr)
			arrr = [i]
			cont = 1
		else:
			arrr.append(i)
			cont += 1
	arr_f.append([arr[len(arr)-3],arr[len(arr)-2],arr[len(arr)-1]])
	return(arr_f)

def agrega_figura(tipo):
	global contador
	tagg = "tag_"+str(contador)
	T2.tag_configure(tagg, background=color_code[1],foreground="#FFFFFF")
	T2.insert(END, tipo+"\n", (tagg))
	contador +=1

def evento():
	plano.eventos()
	
#------------------------------------------------------------------------------

fondo='#49A'
raiz = Tk() 
raiz.resizable(False, False)
mi_Frame = Frame() #Creacion del Frame
mi_Frame.pack(side=RIGHT)  
mi_Frame.config(bg="blue") 
mi_Frame['bg'] = fondo
mi_Frame.config(width="800", height="640") 
mi_Frame.config(bd=10) 
mi_Frame.config(relief="sunken") 

etiqueta1 = tk.Label(text="♣ ♣ GRAFICADOR 3D ♣ ♣",font=("Times", 40)).place(x=80,y=10)
etiqueta1 = tk.Label(text="♣ ♣ IRVING ALDAHI BENITEZ HERNANDEZ ♣ ♣",font=("Times", 10)).place(x=30,y=610)
etiqueta1 = tk.Label(text="♣ ♣ JOSE SOTELO ROMAN ♣ ♣",font=("Times", 10)).place(x=600,y=610)

#------------------------------MOVIMIENTO---------------------------------------
boton = tk.Button(text="MOVER GRAFICA", command=evento,font=("Times", l_b))
boton.place(x=600, y=550)

#---------------------------Limpiar Plano---------------------------------------
boton4 = tk.Button(text="LIMPIAR GRAFICA",command=(limpiar_pantalla),font=("Times", l_b))
boton4.place(x=50, y=550)
#-----------------------------PINTA LINEA---------------------------------------
#texto 2 
etiqueta1 = tk.Label(text="POINT 1",font=("Times", l_e)).place(x=120,y=100)
etiqueta1 = tk.Label(text="POINT 2",font=("Times", l_e)).place(x=620,y=100)
etiqueta1 = tk.Label(text="X",font=("Times", l_e)).place(x=30,y=130)
#boton 2 
boton2 = tk.Button(text="PINTAR PUNTO",command=(pinta_punto),font=("Times", l_b))
boton2.place(x=335, y=135)
boton2 = tk.Button(text="PINTAR VECTOR",command=(pinta_vector),font=("Times", l_b))
boton2.place(x=330, y=172)
#caja de texto de texto 2.
x_txt = tk.Entry(font=("Times", l_en))
x_txt.place(x=50, y=130)
#texto 3 
etiqueta1 = tk.Label(text="Y",font=("Times", l_e)).place(x=30,y=160)
#caja de texto de texto 3.
y_txt = tk.Entry(font=("Times", l_en))
y_txt.place(x=50, y=160)
#texto 4 
etiqueta1 = tk.Label(text="Z",font=("Times", l_e)).place(x=30,y=190)
#caja de texto de texto 3.
z_txt = tk.Entry(font=("Times", l_en))
z_txt.place(x=50, y=190)
etiqueta1 = tk.Label(text="X",font=("Times", l_e)).place(x=30,y=130)
#***********************************
#caja de texto de texto 2.
etiqueta1 = tk.Label(text="X",font=("Times", l_e)).place(x=530,y=130)
x1_txt = tk.Entry(font=("Times", l_en))
x1_txt.place(x=550, y=130)
#texto 3 
etiqueta1 = tk.Label(text="Y",font=("Times", l_e)).place(x=530,y=160)
#caja de texto de texto 3.
y1_txt = tk.Entry(font=("Times", l_en))
y1_txt.place(x=550, y=160)
#texto 4 
etiqueta1 = tk.Label(text="Z",font=("Times", l_e)).place(x=530,y=190)
#caja de texto de texto 3.
z1_txt = tk.Entry(font=("Times", l_en))
z1_txt.place(x=550, y=190)
#---------------------------PINTA Plano---------------------------------------

etiqueta1 = tk.Label(text="COORDENADAS",font=("Times", l_e)).place(x=80,y=240)
T = tk.Text(height = 10, width = 25,font=("Times", 15))
T.place(x=15,y=270)
boton3 = tk.Button(text="CARGAR ARCHIVO",command=(cargar_archivo),font=("Times", l_b))
boton3.place(x=300, y=270)
boton4 = tk.Button(text="GRAFICAR PLANO",command=(pinta_plano),font=("Times", l_b))
boton4.place(x=300, y=310)
boton4 = tk.Button(text="GRAFICAR CAJA",command=(pinta_caja),font=("Times", l_b))
boton4.place(x=300, y=350)
boton4 = tk.Button(text="GRAFICAR FUN",command=(genera_fun),font=("Times", l_b))
boton4.place(x=300, y=390)
boton4 = tk.Button(text="GRAFICAR TODOS",command=(pinta_todos),font=("Times", l_b))
boton4.place(x=300, y=430)
etiqueta1 = tk.Label(text="FIGURAS CARGADAS",font=("Times", l_e)).place(x=570,y=240)
T2 = tk.Text(height = 10, width = 25,font=("Times", 15))
T2.place(x=500,y=270)
#------------Boton color----------------------
boton4 = tk.Button(text = "COLOR",font=("Times", l_b),command = (choose_color))
boton4.place(x=300, y=490)
color_et = tk.Label(text="     ",font=("Times", l_b),bg=color_code[1])
color_et.place(x=380,y=493)


es = int(15)
plano.iniciar(15)

raiz.mainloop()