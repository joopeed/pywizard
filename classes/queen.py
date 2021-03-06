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

images["preo1"] = pygame.image.load("./images/queenpreo1.png").convert_alpha()
images["preo2"] = pygame.image.load("./images/queenpreo2.png").convert_alpha()
images["preo11"] = pygame.image.load("./images/queenpreo1with1.png").convert_alpha()
images["preo21"] = pygame.image.load("./images/queenpreo2with1.png").convert_alpha()
images["happy"] = pygame.image.load("./images/queenhappy.png").convert_alpha()
images["sombra"] = pygame.image.load("./images/sombra.png").convert_alpha()
images["fogo"] = pygame.image.load("./images/fogo.png").convert_alpha()
#images["fototwitter"] = pygame.image.load("foto.jpg").convert_alpha()

#Fonts
pygame.font.init()
font_of_life = pygame.font.Font(None, 17)
font_of_mana = pygame.font.Font(None, 17)
#End of Fonts


class Queen:
	"""
	Class to create Magos/Wizards
	"""
	def __init__(self, name, posInitial, screen, show_atributos):
		self.life = 100
		self.velocity = 1
		self.position = self.x, self.y = posInitial
		self.name = name # "Kindrug" 
		self.color_of_life = (0, 200,0)
		self.items = {"earrings":0}
		self.mago = images["preo1"]
		#self.chao = pygame.sprite.Sprite() .rect
		self.chao = pygame.Rect(self.x, self.y+84, 45,10)
		self.chaoget = pygame.Rect(self.x-40, self.y+40, 140,80)
		# Laterais possiveis
		self.chaoright = pygame.Rect(self.x+self.velocity, self.y+84, 45,10)
		self.chaoleft = pygame.Rect(self.x-self.velocity, self.y+84, 45,10)
		self.chaoup = pygame.Rect(self.x, self.y+84-self.velocity, 45,10)
		self.chaodown = pygame.Rect(self.x, self.y+84+self.velocity, 45,10)
		self.screen = screen
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


	def movement(self):
		if not self.items['earrings']:
			self.mago = images["preo1"]
		elif self.items['earrings']==1:
			self.mago = images["preo11"]
		else:
			self.mago = images["happy"]
	def unmovement(self):
		if not self.items['earrings']:
			self.mago = images["preo2"]
		elif self.items['earrings']==1:
			self.mago = images["preo21"]
		else:
			self.mago = images["happy"]
	
	def isdead(self):
		return self.life == 0
	def invisible(self, value):
		self.invisible = value	

	def update(self):
		# print chao.top
		self.chao = pygame.Rect(self.x, self.y+84, 45,10)
		self.chaoget = pygame.Rect(self.x-40, self.y+40, 140,80)
		# Laterais possiveis
		self.chaoright = pygame.Rect(self.x+self.velocity, self.y+84, 45,10)
		self.chaoleft = pygame.Rect(self.x-self.velocity, self.y+84, 45,10)
		self.chaoup = pygame.Rect(self.x, self.y+84-self.velocity, 45,10)
		self.chaodown = pygame.Rect(self.x, self.y+84+self.velocity, 45,10)

		#self.chao.image = pygame.image.load("bola.png")
		"""Deixa o chão visível"""
		#pygame.draw.rect(self.screen, (255,255,255),self.chao)
		#pygame.draw.rect(self.screen, (255,255,255),self.chaoget)
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
			textRectlife = self.x,self.y-22,self.x+20,self.y
			barralife = pygame.Rect(self.x+2, self.y-8, 36.0/100*self.life ,6)
			borda = pygame.Rect(self.x, self.y-10, 40,10)
			#sombra = pygame.Rect(self.x+2, self.y+2, 40,10)
			

			# Drawing the group of borda, bar of life and text of percent
			self.screen.blit(images['sombra'],(self.x-2, self.y-12))	
			pygame.draw.rect(self.screen, (255,255,255), borda)
			pygame.draw.rect(self.screen, self.color_of_life, barralife)
			#self.screen.blit(textlife, textRectlife)

		
			self.screen.blit(textname, textRectname)
			#self.screen.blit(images["fototwitter"], (self.x-14,self.y-96))
		
