import pygame
import sys
import random
import pygame.gfxdraw
from pygame.locals import *
import math



#Inicializamos el motor de juego
pygame.init() 

pygame.font.init()
FONT = pygame.font.Font(None, 15)

clock = pygame.time.Clock()

ancho = 800


#definimos escenario. importante no cambiar
pantalla = pygame.display.set_mode((ancho, ancho))
pygame.display.set_caption("CHESS")

def imagen(filename, transparent=False):
	try: image = pygame.image.load(filename)
	except pygame.error as message:
			raise SystemExit
	image = image.convert()
	if transparent:
			color = image.get_at((0,0))
			image.set_colorkey(color, RLEACCEL)
	image = pygame.transform.scale(image, (round(ancho/10), round(ancho/10)))
	return image
		
    
def draw_mouse_position():
	global pantalla
	x, y = pygame.mouse.get_pos()
	text(x, y - 15, "x: {0}, y: {1}".format(x, y),1)
	
def text(x, y, t, c = 0):
	global pantalla, FONT
	text_image = FONT.render(t, 1, (255, 255, 255))
	if c == 1:
		r = text_image.get_rect()
		pantalla.blit(text_image, (x - r.width / 2, y))
	elif c == 2:
		r = text_image.get_rect()
		pantalla.blit(text_image, (x, y - r.height / 2))
	elif c == 3:
		r = text_image.get_rect()
		pantalla.blit(text_image, (x - r.width / 2, y - r.height / 2))
	else:
		pantalla.blit(text_image, (x, y))

#Obtenemos forma de las figuras

def tablero():
	for i in range(0,8):
		for j in range(0,8):
			if (i+j)%2 == 0:
				pygame.draw.rect(pantalla,(200,200,200),(i * (ancho/8),j * (ancho/8),ancho/8,ancho/8))

#Importamos las piezas
ancho_pieza = float(ancho*0.1)
KB = imagen('.\Ajedrez\piezas\KB.png', True)
#KB = pygame.transform.scale(KB, (round(ancho_pieza), round(ancho_pieza)))
forma_KB = KB.get_rect()
QB = imagen('.\Ajedrez\piezas\QB.png', True)
#QB = pygame.transform.scale(QB, (round(ancho_pieza), round(ancho_pieza)))
forma_QB = QB.get_rect()
AB = imagen('.\Ajedrez\piezas\AB.png', True)
#AB = pygame.transform.scale(AB, (round(ancho_pieza), round(ancho_pieza)))
forma_AB = AB.get_rect()
CB = imagen('.\Ajedrez\piezas\CB.png', True)
#CB = pygame.transform.scale(CB, (round(ancho_pieza), round(ancho_pieza)))
forma_CB = CB.get_rect()
PB = imagen('.\Ajedrez\piezas\PB.png', True)
#PB = pygame.transform.scale(PB, (round(ancho_pieza), round(ancho_pieza)))
forma_PB = PB.get_rect()
TB = imagen('.\Ajedrez\piezas\TB.png', True)
#TB = pygame.transform.scale(TB, (round(ancho_pieza), round(ancho_pieza)))
forma_TB = TB.get_rect()

KN = imagen('.\Ajedrez\piezas\KN.png', True)
#KN = pygame.transform.scale(KN, (round(ancho_pieza), round(ancho_pieza)))
forma_KN = KN.get_rect()
QN = imagen('.\Ajedrez\piezas\QN.png', True)
#QN = pygame.transform.scale(QN, (round(ancho_pieza), round(ancho_pieza)))
forma_QN = QN.get_rect()
AN = imagen('.\Ajedrez\piezas\AN.png', True)
#AN = pygame.transform.scale(AN, (round(ancho_pieza), round(ancho_pieza)))
forma_AN = AN.get_rect()
CN = imagen('.\Ajedrez\piezas\CN.png', True)
#CN = pygame.transform.scale(CN, (round(ancho_pieza), round(ancho_pieza)))
forma_CN = CN.get_rect()
PN = imagen('.\Ajedrez\piezas\PN.png', True)
#PN = pygame.transform.scale(PN, (round(ancho_pieza), round(ancho_pieza)))
forma_PN = PN.get_rect()
TN = imagen('.\Ajedrez\piezas\TN.png', True)
#TN = pygame.transform.scale(TN, (round(ancho_pieza), round(ancho_pieza)))
forma_TN = TN.get_rect()


#Vectores de posiciones de las casillas
cord_x = []
cord_y = []

for i in range(0,8):
	cord_x.append((ancho/16) + i * (ancho/8))
	cord_y.append((ancho/16) + i * (ancho/8))

def inicio():
	forma_KN.center = (cord_x[4], cord_y[0])
	pantalla.blit(KN, (forma_KN.centerx - (ancho_pieza*0.5), forma_KN.centery - (ancho_pieza*0.5)))		
	forma_KB.center = (cord_x[4], cord_y[7])
	pantalla.blit(KB, (forma_KB.centerx - (ancho_pieza*0.5), forma_KB.centery - (ancho_pieza*0.5)))		

	forma_QN.center = (cord_x[3], cord_y[0])
	pantalla.blit(QN, (forma_QN.centerx - (ancho_pieza*0.5), forma_QN.centery - (ancho_pieza*0.5)))		
	forma_QB.center = (cord_x[3], cord_y[7])
	pantalla.blit(QB, (forma_QB.centerx - (ancho_pieza*0.5), forma_QB.centery - (ancho_pieza*0.5)))		


	for i in range(0,8):
		forma_PN.center = (cord_x[i], cord_y[1])
		pantalla.blit(PN, (forma_PN.centerx - (ancho_pieza*0.5), forma_PN.centery - (ancho_pieza*0.5)))		
		forma_PB.center = (cord_x[i], cord_y[6])
		pantalla.blit(PB, (forma_PB.centerx - (ancho_pieza*0.5), forma_PB.centery - (ancho_pieza*0.5)))

	for i in [0,1]:
		forma_TN.center = (cord_x[i*7], cord_y[0])
		pantalla.blit(TN, (forma_TN.centerx - (ancho_pieza*0.5), forma_TN.centery - (ancho_pieza*0.5)))
		forma_TB.center = (cord_x[i*7], cord_y[7])
		pantalla.blit(TB, (forma_TB.centerx - (ancho_pieza*0.5), forma_TB.centery - (ancho_pieza*0.5)))		

		forma_AN.center = (cord_x[i*3 + 2], cord_y[0])
		pantalla.blit(AN, (forma_AN.centerx - (ancho_pieza*0.5), forma_AN.centery - (ancho_pieza*0.5)))		
		forma_AB.center = (cord_x[i*3 + 2], cord_y[7])
		pantalla.blit(AB, (forma_AB.centerx - (ancho_pieza*0.5), forma_AB.centery - (ancho_pieza*0.5)))		

		forma_CN.center = (cord_x[i*5 + 1], cord_y[0])
		pantalla.blit(CN, (forma_CN.centerx - (ancho_pieza*0.5), forma_CN.centery - (ancho_pieza*0.5)))		
		forma_CB.center = (cord_x[i*5 + 1], cord_y[7])
		pantalla.blit(CB, (forma_CB.centerx - (ancho_pieza*0.5), forma_CB.centery - (ancho_pieza*0.5)))		

def distance(p0, p1):
       return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def movimiento():
	event = pygame.event.wait()
	mx, my = pygame.mouse.get_pos()
	if event.type == pygame.MOUSEBUTTONDOWN:
		if event.button == 1:
			print ("Boton apretado")
			if distance(pygame.mouse.get_pos() ,forma_PN.center) < ancho/8:
				pantalla.blit(PN, (mx, my))		

				print("Cerca")



	if event.type == pygame.MOUSEBUTTONUP:
		if event.button == 1:
			print ("Boton LEVANTADO")

pantalla.fill([80,80,80])	
tablero()
inicio()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:#si apretamos cerrar ventana, el juego se acaba
			pygame.quit()
			sys.exit()

	
	
	#draw_mouse_position()



	movimiento()

	#Actualizar la pantalla
	pygame.display.update()

	
	clock.tick(60) #60fps. Si no controlamos esto, el ordenador intentará procesarlo al máximo. Puede petar
