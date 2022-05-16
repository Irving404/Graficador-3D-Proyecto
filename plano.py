import pygame  
import math

eje_x = [600,0,0]
eje_y = [0,600,0]
eje_z = [0,0,600]
eje_m_x = [-600,0,0]
eje_m_y = [0,-600,0]
eje_m_z = [0,0,-600]
#------------------------------------------------------------------
mitad = 300
ang_x = 0
ang_y = 0
ang_z = 0
avance = 0.5
escala = 30
figuras = []
#------------------------------------------------------------------
identidad = [[1,0,0],
			  [0,1,0],
			  [0,0,0]]
#------------------------------------------------------------------
pantalla = pygame.display.set_mode((600,600))  
pantalla.fill((255, 255, 255))
pygame.display.set_caption('Pygame Window')
#------------------------------------------------------------------
def producto_punto(vari_1,vari_2):
	x = (vari_1[0][0]*vari_2[0])+(vari_1[1][0]*vari_2[1])+(vari_1[2][0]*vari_2[2])
	y = (vari_1[0][1]*vari_2[0])+(vari_1[1][1]*vari_2[1])+(vari_1[2][1]*vari_2[2])
	z = (vari_1[0][2]*vari_2[0])+(vari_1[1][2]*vari_2[1])+(vari_1[2][2]*vari_2[2])
	salida = [x,y,z]
	return salida

def rotacion_y():
	mat_rotacion = [[math.cos(ang_y),0,math.sin(ang_y)],
					[0,1,0],
					[-math.sin(ang_y), 0,math.cos(ang_y)]]
	return mat_rotacion

def rotacion_x():
	mat_rotacion = [[1,0,0],
					[0,math.cos(ang_x),-math.sin(ang_x)],
					[0, math.sin(ang_x),math.cos(ang_x)]]
	return mat_rotacion

def rotacion_z():
	mat_rotacion = [[math.cos(ang_z),-math.sin(ang_z),0],
					[math.sin(ang_z),math.cos(ang_z),0],
					[0,0,1]]
	return mat_rotacion

def proyection(vector):
	proyeccion = producto_punto(identidad,vector)
	return proyeccion

def transforma_punto(point):
	x_rotado = producto_punto(rotacion_x(),point)
	y_rotado = producto_punto(rotacion_y(),x_rotado)
	z_rotado = producto_punto(rotacion_z(),y_rotado)
	return z_rotado

def grafica_ejes():
	pantalla.fill((255, 255, 255))

	global eje_x,eje_y,eje_z,eje_m_x,eje_m_y,eje_m_z,plano

	punto_x = transforma_punto(eje_x)
	punto_y = transforma_punto(eje_y)
	punto_z = transforma_punto(eje_z)

	punto_x_m = transforma_punto(eje_m_x)
	punto_y_m = transforma_punto(eje_m_y)
	punto_z_m = transforma_punto(eje_m_z)

	R2_x = proyection(punto_x)
	R2_y = proyection(punto_y)
	R2_z = proyection(punto_z)
	R2_x_m = proyection(punto_x_m)
	R2_y_m = proyection(punto_y_m)
	R2_z_m = proyection(punto_z_m)

	pygame.draw.line(pantalla,(0,0,0),[R2_x[0]+300,R2_x[1]+300],[R2_x_m[0]+300,R2_x_m[1]+300])
	pygame.draw.line(pantalla,(0,0,255),[R2_y[0]+300,R2_y[1]+300],[R2_y_m[0]+300,R2_y_m[1]+300])
	pygame.draw.line(pantalla,(255,0,0),[R2_z[0]+300,R2_z[1]+300],[R2_z_m[0]+300,R2_z_m[1]+300])
	agregar_marcas()
	pinta_figuras()
	pygame.display.flip()

def pinta_plano(points,color):
	points_aux = []
	if(len(points)==4):
		for i in points:
			t = transforma_punto(i)
			points_aux.append(t)
		a_p = proyection(points_aux[0])
		b_p = proyection(points_aux[1])
		c_p = proyection(points_aux[2])
		d_p = proyection(points_aux[3])
		pygame.draw.line(pantalla,color,escalar(a_p),escalar(b_p))
		pygame.draw.line(pantalla,color,escalar(a_p),escalar(c_p))
		pygame.draw.line(pantalla,color,escalar(d_p),escalar(b_p))
		pygame.draw.line(pantalla,color,escalar(d_p),escalar(c_p))
		pygame.display.flip()

	return points_aux

def escalar(r2):
	x = (r2[0]*escala)+mitad
	y = (r2[1]*escala)+mitad
	return [x,y]

def rota_eje_x(mas):
	global ang_x
	ang_x += avance if mas else -avance
	grafica_ejes()


def rota_eje_y(mas):
	global ang_y
	ang_y += avance if mas else -avance
	grafica_ejes()

def rota_eje_z(mas):
	global ang_z
	ang_z += avance if mas else -avance
	grafica_ejes()

def pinta_punto(punto,color):
	punto_x = transforma_punto(punto)
	r2 = proyection(punto_x)
	esca = escalar(r2)
	fuente = pygame.font.Font(None, 30)
	text = str(".")
	mensaje = fuente.render(text, 0, color)
	pantalla.blit(mensaje, (esca[0]-3,esca[1]-14))
	pygame.display.flip()

def pinta_num(punto,color,txt):
	punto_x = transforma_punto(punto)
	r2 = proyection(punto_x)
	esca = escalar(r2)
	fuente = pygame.font.Font(None, 15)
	text = str(txt)
	mensaje = fuente.render(text, 0, color)
	pantalla.blit(mensaje, (esca[0]+10,esca[1]+5))
	pygame.display.flip()


def agregar_marcas():

	global escala
	cantidad = int(600/escala)
	
	for i in range(1,cantidad):
		x = [(i),0,0]
		y = [0,(i),0]
		z = [0,0,(i)]
		m_x = [-(i),0,0]
		m_y = [0,-(i),0]
		m_z = [0,0,-(i)]

		pinta_punto(x,(0,0,0))
		pinta_num(x,(0,0,0),str(i))

		pinta_punto(m_x,(0,0,0))
		pinta_num(m_x,(0,0,0),"-- "+str(i))

		pinta_punto(y,(0,0,255))
		pinta_num(y,(0,0,255),str(i))

		pinta_punto(m_y,(0,0,255))
		pinta_num(m_y,(0,0,255),"-- "+str(i))

		pinta_punto(z,(255,0,0))
		pinta_num(z,(255,0,0),(i))

		pinta_punto(m_z,(255,0,0))
		pinta_num(m_z,(255,0,0),"-- "+str(i))
		


def pinta_caja(points,color):
	points_aux = []
	for i in points:
		t = transforma_punto(i)
		points_aux.append(t)

	a_p = proyection(points_aux[0])
	b_p = proyection(points_aux[1])
	c_p = proyection(points_aux[2])
	d_p = proyection(points_aux[3])
	
	a1_p = proyection(points_aux[4])
	b1_p = proyection(points_aux[5])
	c1_p = proyection(points_aux[6])
	d1_p = proyection(points_aux[7])


	pygame.draw.line(pantalla,color,escalar(a_p),escalar(b_p))
	pygame.draw.line(pantalla,color,escalar(a_p),escalar(c_p))
	pygame.draw.line(pantalla,color,escalar(d_p),escalar(b_p))
	pygame.draw.line(pantalla,color,escalar(d_p),escalar(c_p))

	pygame.draw.line(pantalla,color,escalar(a1_p),escalar(b1_p))
	pygame.draw.line(pantalla,color,escalar(a1_p),escalar(c1_p))
	pygame.draw.line(pantalla,color,escalar(d1_p),escalar(b1_p))
	pygame.draw.line(pantalla,color,escalar(d1_p),escalar(c1_p))

	pygame.draw.line(pantalla,color,escalar(a_p),escalar(a1_p))
	pygame.draw.line(pantalla,color,escalar(b_p),escalar(b1_p))
	pygame.draw.line(pantalla,color,escalar(c_p),escalar(c1_p))
	pygame.draw.line(pantalla,color,escalar(d_p),escalar(d1_p))
	pygame.display.flip()


def pinta_linea(points,color):
	vec1 = points[0]
	vec2 = points[1]
	pinta_punto(vec1,color)
	pinta_punto(vec2,color)
	v1_r = proyection(transforma_punto(vec1))
	v2_r = proyection(transforma_punto(vec2))
	pygame.draw.line(pantalla, color,escalar(v1_r),escalar(v2_r))
	pygame.display.flip()

def limpiar_pantalla():
	pantalla.fill((255, 255, 255))
	pygame.display.flip()

def inicia_todo():
	global ang_x,ang_y,ang_z,figuras
	figuras=[]
	ang_z=0
	ang_y=0
	ang_x=0
	pantalla.fill((255, 255, 255))
	pygame.display.flip()
	iniciar(escala)

def iniciar(esca):
	global escala
	escala= esca
	pygame.init()
	grafica_ejes()
	
def pinta_todos(points,color):
	for i in range(len(points)):
		pinta_punto(points[i],color)
		for j in range(i+1,len(points)):
			pinta_linea([points[i],points[j]],color)
	

def get_angulos():
	return ang_x,ang_y,ang_z

def pinta_figura(tipo,points,color):
	global figuras
	figuras.append([tipo,points,color])
	if tipo == 'plano':
		pinta_plano(points,color)
	elif tipo == 'caja':
		pinta_caja(points,color)
	elif tipo == 'vector':
		pinta_linea(points,color)
	elif tipo == 'punto':
		pinta_punto(points,color)
	elif tipo == 'todos':
		pinta_todos(points,color)	

def pinta_figuras():

	for fig in figuras:
		if fig[0] == 'plano':
			pinta_plano(fig[1],fig[2])
		elif fig[0] == 'caja':
			pinta_caja(fig[1],fig[2])
		elif fig[0] == 'vector':
			pinta_linea(fig[1],fig[2])
		elif fig[0] == 'punto':
			pinta_punto(fig[1],fig[2])
		elif fig[0] == 'todos':
			pinta_todos(fig[1],fig[2])		
	