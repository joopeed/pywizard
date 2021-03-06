# -*- coding: utf-8 -*-
import pygame, urllib
from projeteis import *
from dropfire import *
from sets import Set
"""
nick = raw_input()
s = urllib.urlopen('http://twitter.com/'+nick)
data = s.read()	
data = data.split()
for i in range(len(data)):
	#if 'id="profile-image"' in data[i]:
		foto = data[i+1][5:-1]
		break
s = urllib.urlopen(foto)
data = s.read()
f = open('foto.jpg', 'wb')	
f.write(data)
f.close()"""	

images = {}

images["bluemagoR"] = pygame.image.load("./images/bluemagoR.png").convert_alpha()
images["bluemagoL"] = pygame.image.load("./images/bluemagoL.png").convert_alpha()
images["bluemagoU"] = pygame.image.load("./images/bluemagoU.png").convert_alpha()
images["bluemagoD"] = pygame.image.load("./images/bluemagoD.png").convert_alpha()
images["redmagoR"]  = pygame.image.load("./images/redmagoR.png").convert_alpha()
images["redmagoL"]  = pygame.image.load("./images/redmagoL.png").convert_alpha()
images["redmagoU"]  = pygame.image.load("./images/redmagoU.png").convert_alpha()
images["redmagoD"]  = pygame.image.load("./images/redmagoD.png").convert_alpha()
images["blackmagoR"] = pygame.image.load("./images/blackmagoR.png").convert_alpha()
images["blackmagoL"] = pygame.image.load("./images/blackmagoL.png").convert_alpha()
images["blackmagoU"] = pygame.image.load("./images/blackmagoU.png").convert_alpha()
images["blackmagoD"] = pygame.image.load("./images/blackmagoD.png").convert_alpha()
images["whitemagoR"] = pygame.image.load("./images/whitemagoR.png").convert_alpha()
images["whitemagoL"] = pygame.image.load("./images/whitemagoL.png").convert_alpha()
images["whitemagoU"] = pygame.image.load("./images/whitemagoU.png").convert_alpha()
images["whitemagoD"] = pygame.image.load("./images/whitemagoD.png").convert_alpha()
images["sombra"] = pygame.image.load("./images/sombra.png").convert_alpha()
images["fogo"] = pygame.image.load("./images/fogo.png").convert_alpha()
#images["fototwitter"] = pygame.image.load("foto.jpg").convert_alpha()
projectiles = Set()
drops = Set()
#Fonts
pygame.font.init()
font_of_life = pygame.font.Font(None, 17)
font_of_mana = pygame.font.Font(None, 17)
#End of Fonts


class Wizard:
	"""
	Class to create Magos/Wizards
	"""
	def __init__(self, name, color, posInitial, screen, show_atributos):
		self.direction = "magoD"
		self.life = 100
		self.mana = 100
		self.velocity = 1
		self.color = color # "white" # color
		self.position = self.x, self.y = posInitial
		self.name = name # "Kindrug" 
		self.color_of_life = (0, 200,0)
		self.color_of_mana = (200, 200,100)
		self.items = {"potion2":0, "potion3":0,  "earrings":0}
		self.mago = images[self.color + self.direction]
		#self.chao = pygame.sprite.Sprite() .rect
		self.chao = pygame.Rect(self.x, self.y+114, 45,10)
		# Laterais possiveis
		self.chaoright = pygame.Rect(self.x+self.velocity, self.y+114, 45,10)
		self.chaoleft = pygame.Rect(self.x-self.velocity, self.y+114, 45,10)
		self.chaoup = pygame.Rect(self.x, self.y+114-self.velocity, 45,10)
		self.chaodown = pygame.Rect(self.x, self.y+114+self.velocity, 45,10)
		self.screen = screen
		self.fogo = False
		self.show = show_atributos
		rect = pygame.Rect(self.x,self.y,self.mago.get_width(),self.mago.get_height())
		self.center = rect.centerx -15, rect.centery+20
		self.invisible = False	
	
	def __str__(self):	
		return self.name.strip()
	
	def __repr__(self):
        	return self.name.strip()

	def lower(self,value):
		if self.life-value>0:
			self.life -=value
		else:
			self.life =0
		if self.life > 40: # If at least 40%, its green
			self.color_of_life = (0, 200,0)
		else:
			self.color_of_life = (200, 0,0)
		
	def upper(self,value):
		if self.life <=100-value:
			self.life +=value
		else:
			self.life +=100-self.life
		if self.life > 40: # If at least 40%, its green
			self.color_of_life = (0, 200,0)
		else:
			self.color_of_life = (200, 0,0)

	def lowermana(self,value):
		if self.mana >=value:
			self.mana -=value
		if self.mana > 80: # If at least 80%, its yellow
			self.color_of_mana = (200, 200,0)
		else:
			self.color_of_mana = (180, 180,100)

	def uppermana(self,value):
		if self.mana <=100-value:
			self.mana +=value
		else:
			self.mana+= 100-self.mana
		if self.mana > 80: # If at least 80%, its yellow
			self.color_of_mana = (200, 200,0)
		else:
			self.color_of_mana = (180, 180,100)
		

	def moveright(self):
		self.direction = "magoR"
		self.position = self.x, self.y = self.x+1,self.y
		self.mago = images[self.color + self.direction]
		
	def moveleft(self):
		self.direction = "magoL"
		self.position = self.x, self.y = self.x-1,self.y
		self.mago = images[self.color + self.direction]
		
	def moveup(self):
		self.direction = "magoU"
		#self.position = self.x, self.y = self.x,self.y-2
		self.mago = images[self.color + self.direction]
		
	def movedown(self):
		self.direction = "magoD"
		#self.position = self.x, self.y = self.x,self.y+2
		self.mago = images[self.color + self.direction]
	
	def isdead(self):
		return self.life == 0
	def invisible(self, value):
		self.invisible = value	

	def update(self):
		# print chao.top
		self.chao = pygame.Rect(self.x, self.y+114, 45,10)
		self.position = self.x, self.y
		# Laterais possiveis
		self.chaoright = pygame.Rect(self.x+self.velocity, self.y+114, 45,10)
		self.chaoleft = pygame.Rect(self.x-self.velocity, self.y+114, 45,10)
		self.chaoup = pygame.Rect(self.x, self.y+114-self.velocity, 45,10)
		self.chaodown = pygame.Rect(self.x, self.y+114+self.velocity, 45,10)

		#self.chao.image = pygame.image.load("bola.png")
		"""Deixa o chão visível"""
		#pygame.draw.rect(self.screen, (255,255,255),self.chao)
		if self.fogo:		
			self.screen.blit(images["fogo"],(self.x-35,self.y+11))
		
		# Update of Mago 
		if not self.invisible:
			self.screen.blit(self.mago,(self.x,self.y))
		
		if self.show:


			#Update of Name
			textname = font_of_life.render(self.name, True, (255,255, 255)) #self.color_of_life) white default
			textRectname = self.x-4,self.y-24
			barraname = pygame.Rect(self.x+2, self.y+2, 36.0/100*self.life ,6)
			bordaname = pygame.Rect(self.x, self.y, 40,10)

			# Update of Life 	
			textlife = font_of_life.render("%.2f"%(self.life)+"%", True, (255,255, 255)) #self.color_of_life) white default
			textRectlife = self.x,self.y-12,self.x+20,self.y
			barralife = pygame.Rect(self.x+2, self.y+2, 36.0/100*self.life ,6)
			borda = pygame.Rect(self.x, self.y, 40,10)
			#sombra = pygame.Rect(self.x+2, self.y+2, 40,10)
			
			# Update of Mana 
			textmana = font_of_mana.render("%.2f"%(self.mana)+"%", True, (255,255, 255)) #self.color_of_life) white default
			textRectmana = self.x,self.y-22,self.x+20,self.y
			barramana = pygame.Rect(self.x+2, self.y-8, 36.0/100*self.mana ,6)
			borda_mana = pygame.Rect(self.x, self.y-10, 40,10)
			#sombra = pygame.Rect(self.x+2, self.y+2, 40,10)

			# Drawing the group of borda, bar of life and text of percent
			self.screen.blit(images['sombra'],(self.x-2, self.y-2))	
			pygame.draw.rect(self.screen, (255,255,255), borda)
			pygame.draw.rect(self.screen, self.color_of_life, barralife)
			#self.screen.blit(textlife, textRectlife)

			# Drawing the group of borda, bar of mana and text of percent
			self.screen.blit(images['sombra'],(self.x-2, self.y-12))	
			pygame.draw.rect(self.screen, (255,255,255), borda_mana)
			pygame.draw.rect(self.screen, self.color_of_mana, barramana)
			#self.screen.blit(textmana, textRectmana)
			self.screen.blit(textname, textRectname)
			#self.screen.blit(images["fototwitter"], (self.x-14,self.y-96))
		
	def primary_attack(self,destination):
		#self.fogo = True
		x,y = self.position
		if self.direction=="magoD":
			saidabala = x+5,y+100
		elif self.direction=="magoU":
			saidabala = x+5,y+80
		if self.direction=="magoR":
			saidabala = x+36,y+80
		elif self.direction=="magoL":
			saidabala = x-18,y+80
		attack = Projeteis(self.color+"ball", saidabala, destination, self.screen, self.direction, 2, self)
		projectiles.add(attack)
		
	def second_attack(self,	region, vivos):
		if self.mana >=20:
			self.lowermana(20)
			x,y = region
			for vivo in vivos:
				if vivo.chao.colliderect((x-90,y-40,170,80)):
					vivo.lower(50)
			drops.add( Drop((x-20,y-10), self.screen)) 
			drops.add( Drop((x-40,y), self.screen))
			drops.add( Drop((x-30,y+10), self.screen))
			drops.add( Drop((x+40,y-10), self.screen))
			drops.add( Drop((x+10,y), self.screen))
			drops.add( Drop((x-50,y), self.screen))
			drops.add( Drop((x+30,y+30), self.screen))
			drops.add( Drop((x+60,y-30), self.screen))
			drops.add( Drop((x+70,y), self.screen))
		
