#rojo,verde y azul
import pygame,sys
from pygame.locals import *
import random
from tkinter import *
import tkinter.font as tkFont
#from pynput import keyboard as kb
ancho = 700
alto = 520

x = [230,300,370,440]
end = ''

class Player(pygame.sprite.Sprite):

	def __init__(self,windows):
		pygame.sprite.Sprite.__init__(self)
		self.windows = windows
		X = random.choice(x)
		for i in range(len(x)):
			if X == x[i]:
				self.position = i
				break

		self.driver_car = 'img/carro1.png'
		self.image_drive = pygame.image.load(self.driver_car)

		self.rect = self.image_drive.get_rect()
		self.rect.centerx = random.choice(x)
		self.rect.centery = alto-100
		self.windows.blit(self.image_drive,self.rect)
		self.vida = True
		self.j = 3
		self.cont = 0
		self.white = (255,255,255)
		self.black = (0,0,0)
		self.fuente = pygame.font.SysFont('Arial',20)
		texto = self.fuente.render('Fuel',0,self.white)
		self.windows.blit(texto,(570,370))
		texto = self.fuente.render('Score:',0,self.black,(9,229,9))
		self.windows.blit(texto,(520,230))
		self.texto = self.fuente.render(str(self.cont),0,self.black,(9,229,9))
		self.windows.blit(self.texto,(570,230))
		texto = self.fuente.render('Life:',0,self.black,(9,229,9))
		self.windows.blit(texto,(520,160))
		texto = self.fuente.render(str(self.j),0,self.black,(9,229,9))
		self.windows.blit(texto,(560,160))
		texto = self.fuente.render('Atras(Esc)',0,self.black,(9,229,9))
		self.windows.blit(texto,(0,0))
		texto = self.fuente.render('Jugar(Space)',0,self.black,(9,229,9))
		self.windows.blit(texto,(515,0))

		
	def load_drive(self):
		#print(self.rect)
		self.windows.blit(self.image_drive,self.rect)


	def left(self):
		self.rect[0] = self.rect[0]-20

	def right(self):
		self.rect[0] = self.rect[0]+20

	def life(self):
		if self.j > 1:
			self.vida = True
			self.j -= 1
			texto = self.fuente.render(str(self.j),0,self.black,(9,229,9))
			self.windows.blit(texto,(560,160))
		else:
			self.vida = False

	def score(self):
		self.texto = self.fuente.render(str(self.cont),0,self.black,(9,229,9))
		self.windows.blit(self.texto,(565,230))
		self.cont += 1



class Word(pygame.sprite.Sprite):

	def __init__(self,windows):
		pygame.sprite.Sprite.__init__(self)
		self.y1 = -500
		self.y2 = -480
		self.line = []
		self.windows = windows
		#fondo verde izquierda
		pygame.draw.rect(self.windows,(9,229,9),(0,0,195,alto))
		#fondo verde derecha
		pygame.draw.rect(self.windows,(9,229,9),(505,0,200,360))
		#fondo blanco central
		pygame.draw.rect(self.windows,(247,249,239),(200,0,300,4520))

		image = pygame.image.load('img/derecha.gif')
		self.rect = image.get_rect()
		self.rect.centerx = 640
		self.rect.centery = 100
		self.windows.blit(image,self.rect)

		image2 = pygame.image.load('img/izquierda.gif')
		self.rect = image2.get_rect()
		self.rect.centerx = 540
		self.rect.centery = 100
		self.windows.blit(image2,self.rect)

		image3 = pygame.image.load('img/arriba.gif')
		self.rect = image3.get_rect()
		self.rect.centerx = 590
		self.rect.centery = 60
		self.windows.blit(image3,self.rect)

		image4 = pygame.image.load('img/abajo.gif')
		self.rect = image4.get_rect()
		self.rect.centerx = 590
		self.rect.centery = 100
		self.windows.blit(image4,self.rect)

		for i in range(50):
			self.line.append([])
			self.line[i].append(pygame.draw.line(self.windows,(0,0,0),(280,self.y1+30*i),(280,self.y2+30*i),2))
			self.line[i].append(pygame.draw.line(self.windows,(0,0,0),(350,self.y1+30*i),(350,self.y2+30*i),2))
			self.line[i].append(pygame.draw.line(self.windows,(0,0,0),(420,self.y1+30*i),(420,self.y2+30*i),2))

	def load_word(self,speed):
		pygame.draw.rect(self.windows,(247,249,239),(200,0,300,4520))
		if self.y1 <= 0:
			for i in range(50):
		
				self.line[i][0] = pygame.draw.line(self.windows,(0,0,0),(280,self.y1+30*i),(280,self.y2+30*i),2)
				self.line[i][1] = pygame.draw.line(self.windows,(0,0,0),(350,self.y1+30*i),(350,self.y2+30*i),2)
				self.line[i][2] = pygame.draw.line(self.windows,(0,0,0),(420,self.y1+30*i),(420,self.y2+30*i),2)

			self.y1 += speed
			self.y2 += speed

		else:
			self.y1 = -500
			self.y2 = -480
			print("reset")
		
class Object_insert(pygame.sprite.Sprite):

	def __init__(self,windows):

		self.windows = windows
		self.object = [ 
						"img/carro1.png",
						"img/carro2.png",
						"img/carro3.png",
						"img/carro4.png",
						"img/carro5.png",
						"img/carro6.png",
						"img/carro7.png",
						"img/roca.png",
						"img/Senal.png",
						"img/carro8.png",
						"img/carro9.png",
						"img/senal2.png"
					]
		self.y = -100
		self.file = []

		self.img = []
		self.end = ''

		self.file = random.choice(self.object)
		self.img = pygame.image.load(self.file)
		self.rect = self.img.get_rect()
		self.rect.centerx = random.choice(x)
		self.rect.centery = self.y
		self.control = True


	#mueve los objetos que se ponen en el camino
	def start_up(self,speed):
		if end != 'end':
			if self.rect[1] <= alto:
				#print(self.rect)
				self.windows.blit(self.img,self.rect)
				self.y += speed
				self.rect[1] = self.y

		else:
			print("start_up ha finalizado, has chocado")

class Casas(pygame.sprite.Sprite):
	
	def __init__(self,windows):
		self.windows = windows
		self.object = ['img/casa1.png',
						'img/casa2.png',
						'img/casa3.png',
						'img/casa4.png'
					]
		self.y = -100
		self.file = []

		self.img = []
		self.end = ''

		self.file = random.choice(self.object)
		self.img = pygame.image.load(self.file)
		self.rect = self.img.get_rect()
		self.rect.centerx = 145
		self.rect.centery = self.y
		self.control = True


	#mueve los objetos que se ponen en el camino
	def start_up(self,speed):
		if end != 'end':
			if self.rect[1] <= alto:
				#print(self.rect)
				self.windows.blit(self.img,self.rect)
				self.y += speed
				self.rect[1] = self.y

		else:
			print("start_up ha finalizado, has chocado")


#combustible
class Fuel(pygame.sprite.Sprite):

	def __init__(self,windows):
		pygame.sprite.Sprite.__init__(self)
		self.windows = windows
		X = random.choice(x)
		for i in range(len(x)):
			if X == x[i]:
				self.position = i
				break

		self.y = -100
		self.file = "img/gasolina.png"
		self.img = pygame.image.load(self.file)

		self.rect = self.img.get_rect()
		self.rect.centerx = random.choice(x)
		self.rect.centery = self.y
		

	def start_up(self,speed):
		if end != 'end':
			if self.rect[1] <= 480:
				#print(self.rect)
				self.windows.blit(self.img,self.rect)
				self.y += speed
				self.rect[1] = self.y

		else:
			print("start_up ha finalizado, has chocado")


class Tank(pygame.sprite.Sprite):
	def __init__(self,windows):
		self.windows = windows
		self.tank = []
		self.full = True
		self.miFuente = pygame.font.SysFont('Arial',40)
		self.miTexto = self.miFuente.render(' ',0,(200,60,80),(38,33,219))

		self.miFuente2 = pygame.font.SysFont('Arial',40)
		self.miTexto2 = self.miFuente2.render(' ',0,(200,60,80),(255,255,255))

		self.i = 14

		for i in range(15):
			self.tank.append('')

		self.reloj = pygame.time.Clock()

	def full_fuel(self):
		
		print("colocar combustible")
		self.full = False
		for i in range(15):
			self.tank[i] = self.windows.blit(self.miTexto,(520+i*10,400))

		self.i = 14

	def empy_fuel(self):
		if self.i >= 0:
			self.tank[self.i] = self.windows.blit(self.miTexto2,(520+self.i*10,400))
			self.i -= 1
			#print(self.i)
		else:
			end = 'end'
			fuente = pygame.font.SysFont('Arial',17)
			texto = fuente.render('Se termino el combustible',0,(0,0,0),(9,229,9))
			self.windows.blit(texto,(520,300))
			return end


class Play():


	def __init__(self):
		#self.capture = kb.Listener(self.press)
		#self.capture.start()
		#inicia pygame
		pygame.init()
		#inicia ventana
		self.windows = pygame.display.set_mode((680,520))
		icono = pygame.image.load('img/carro1.png')
		pygame.display.set_icon(icono)
		pygame.display.set_caption("Infinity Car V2")

		self.object_int = ['','','','','','']
		#inicia el mundo
		self.word = Word(self.windows)
		#inserta los objetos en la carretera
		self.object_int[0] = Object_insert(self.windows)
		#inserta el objeto de jugador
		self.playing = Player(self.windows)
		#llenado de tanque de combustible
		self.tank = Tank(self.windows)
		self.tank.full_fuel()
		#self.end = ''
		self.casa = ['','','','','']
		self.casa[0] = Casas(self.windows)
		self.aux2 = 0
		self.aux = 0
		self.fuel = False
		self.jugar = False
		self.speed = 0.1
		#Reloj para hacer un retardo
		#reloj = pygame.time.clock()
		#reloj.tick(60)

		
	def run(self):
		end = ''
		aux = ''
		while True:
			#windows.fill(Color)
			#pygame.draw.rect(self.windows,(9,229,9),(505,0,200,360))

			pygame.draw.rect(self.windows,(9,229,9),(95,0,100,alto))
			for obj in self.object_int:
				if obj != '':

					if self.playing.rect.colliderect(obj.rect):
						if 'gasolina' in obj.file:

							if self.tank.full == True:
								self.tank.full_fuel()
								print("recarga combustible")

						else:
							if end != 'end':
								self.playing.life()
								self.playing.rect[0] = random.choice(x)
								fuente = pygame.font.SysFont('Arial',20)
								texto = fuente.render('Has chocado',0,(0,0,0),(9,229,9))
								self.windows.blit(texto,(520,300))
								self.jugar = False
								#end = 'end'
			
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == pygame.KEYDOWN:
				
					if event.key == K_LEFT:
						if self.playing.rect[0] >= 230:					
							self.playing.left()
						
					elif event.key == K_RIGHT:
						if self.playing.rect[0] <= 440:
							self.playing.right()

					elif event.key == K_UP:
						self.speed += 0.1

					elif event.key == K_DOWN:
						self.speed -= 0.1

					elif event.key == K_SPACE:

						if self.playing.vida == True:
							self.jugar = True
							pygame.draw.rect(self.windows,(9,229,9),(505,300,200,60))
							self.tank.full_fuel()
						else:
							self.__init__()

					elif event.key == K_ESCAPE:
						pygame.quit()
						#sys.exit()
						home = Home()

				elif event.type == pygame.KEYUP:
				
					if event.key == K_LEFT:
						print("tecla izquierda liberada")

					elif event.key == K_RIGHT:	
						print("tecla derecha liberada")
				
			if self.jugar == True:
				self.playing.score()
				for obj in self.casa:
					if obj != '':
						obj.start_up(self.speed)

				if self.casa[self.aux2].rect[1] > 100:
					if self.aux2 < 4:
						self.aux2 += 1
						self.casa[self.aux2] = Casas(self.windows)
					else:
						self.aux2 = 0
						self.casa[self.aux2] = Casas(self.windows)

				if end != 'end':
					self.word.load_word(self.speed)
					for obj in self.object_int:
						if obj != '':
							obj.start_up(self.speed)

					self.playing.load_drive()

					if self.object_int[self.aux].rect[1] > 150:
						self.aux += 1
						if self.aux == len(self.object_int)-1:
							self.object_int[self.aux] = Fuel(self.windows)
							self.aux = -1
							self.tank.full = True
						else:
							self.object_int[self.aux] = Object_insert(self.windows)

						end = self.tank.empy_fuel()

				else:
					self.playing.life()
					self.tank.full_fuel()
					self.jugar = False
					end = ''

			#tecla = pygame.key.get_pressed()
			#print(tecla)
			pygame.display.update()
						
class Home:

	#muestra la ventana de inicio de el juego
	def __init__(self):
		self.aux=-45
		self.Y = random.choice([295,390])
		self.mundo=Tk()
		self.mundo.title("Infinit Car V3")
		self.mundo.iconbitmap("img/car.ico")
		self.mundo.geometry("680x480")
		self.mundo.resizable(0,0)
		#self.tam=tkFont.Font(family="Lucida Grande", size=30)

		#self.image_Principal=PhotoImage(file="img/pistahoriz.gif")
		self.imagePrincipal=Label(self.mundo,bg="white")
		self.imagePrincipal.place(x=0,y=290)

		self.image_verde=PhotoImage(file="img/verde.gif")
		self.imageverde=Label(self.mundo,image=self.image_verde)
		self.imageverde.place(x=0,y=0)

		self.image_carro=PhotoImage(file="img/car.png")
		self.imagecarro=Label(self.mundo,image=self.image_carro)
		self.imagecarro.place(x=self.aux,y=295)

		self.botonJugar=Button(self.mundo,text="JUGAR",command=self.play)
		self.botonJugar.place(x=350,y=200)

		for i in range(85):
			Label(self.mundo,text=' ',bg="black").place(x=0+8*i,y=280)

		for i in range(85):
			Label(self.mundo,text=' ',bg="black").place(x=0+8*i,y=465)

		for i in range(85):
			Label(self.mundo,text='-',fg="black").place(x=0+8*i,y=370)


		self.titulo=Label(self.mundo,text="Infinit Car",font=tkFont.Font(family="Times New Roman",size=50),bg="#33d533")
		self.titulo.place(x=220,y=100,width=300,height=100)
		#transparencia a la ventana
		#self.mundo.attributes("-alpha",0.9)
		self.moverCarro()
		self.BarraMenu()

		self.mundo.mainloop()

	#mueve carro de ventana principal
	def moverCarro(self):
		
		self.imagecarro.configure(image=self.image_carro)
		self.imagecarro.place(x=self.aux,y=self.Y)
		self.aux+=5
		self.AuxMover=self.mundo.after(50,self.moverCarro)

		if(self.aux>=700):
			self.Y = random.choice([295,390])
			self.aux=-45

	def BarraMenu(self):
		barra_Menu=Menu(self.mundo)

		self.mundo.config(menu=barra_Menu, width=300, height=100)
		archivoMenu=Menu(barra_Menu, tearoff=0)
		archivoMenu.add_command(label="Facil", )
		archivoMenu.add_command(label="Medio", )
		archivoMenu.add_command(label="Dificil", )
		archivoMenu.add_separator()
		archivoMenu.add_command(label="Record", )
		archivoMenu.add_separator()
		archivoMenu.add_command(label="Cerrar", )
		archivoMenu.add_command(label="Salir", command=self.exit)
		
		archivoAyuda=Menu(barra_Menu, tearoff=0)
		archivoAyuda.add_command(label="Licencia", )
		archivoAyuda.add_command(label="Documentacion")
		archivoAyuda.add_command(label="Acerca de...")

		barra_Menu.add_cascade(label="Archivo", menu=archivoMenu)
		barra_Menu.add_cascade(label="Ayuda", menu=archivoAyuda)

	def exit(self):
		self.mundo.destroy()

	def play(self):
		self.mundo.destroy()
		play = Play()
		play.run()


home = Home()