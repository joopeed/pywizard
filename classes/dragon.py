# -*- coding: utf-8 -*-
import pygame
pygame.init()
images = {}

images["dragonR"] = pygame.image.load("./images/dragonR.png").convert_alpha()
images["dragonL"] = pygame.image.load("./images/dragonL.png").convert_alpha()
images["dragonU"] = pygame.image.load("./images/dragonU.png").convert_alpha()
images["dragonD"] = pygame.image.load("./images/dragonD.png").convert_alpha()
images["sombra"] = pygame.image.load("./images/sombra.png").convert_alpha()

pygame.font.init()
font_of_life = pygame.font.Font(None, 17)

class Dragon:
	"""
	Class to create Dragões/Dragons
	"""
	def __init__(self, posInitial,screen):
		self.life = 200
		self.position = self.x, self.y = posInitial
		self.color_of_life = (0, 200,200)
		self.dragon= images["dragonD"]
		self.screen = screen
		self.velocity = 1
		self.tipo = "Dragon"
		#self.chao = pygame.sprite.Sprite() .rect
		self.chao = pygame.Rect(self.x+60, self.y+114, 45,10)
		# Angulo de visão do dragon
		self.visao = pygame.Rect(self.x+50, self.y+134, 60,60)
		# Laterais possiveis
		self.chaoright = pygame.Rect(self.x+60+self.velocity, self.y+114, 45,10)
		self.chaoleft = pygame.Rect(self.x+60-self.velocity, self.y+114, 45,10)
		self.chaoup = pygame.Rect(self.x+60, self.y+114-self.velocity, 45,10)
		self.chaodown = pygame.Rect(self.x+60, self.y+114+self.velocity, 45,10)
		self.frozen = False
		
		
	
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

	def moveright(self,mago):
	   if not self.frozen:
		self.position = self.x, self.y = self.x+self.velocity,self.y
		self.dragon = images["dragonR"]
		self.chao = pygame.Rect(self.x+60, self.y+114, 45,10)
		self.chaoright = pygame.Rect(self.x+60+self.velocity, self.y+114, 45,10)
		self.chaoleft = pygame.Rect(self.x+60-self.velocity, self.y+114, 45,10)
		self.chaoup = pygame.Rect(self.x+60, self.y+114-self.velocity, 45,10)
		self.chaodown = pygame.Rect(self.x+60, self.y+114+self.velocity, 45,10)
		self.visao = pygame.Rect(self.x+100, self.y+87, 60,60)
		if mago.chao.colliderect(self.visao) and not mago.invisible and not self.isdead():
			mago.lower(2)
	def moveleft(self,mago):
	   if not self.frozen:
		self.position = self.x, self.y = self.x-self.velocity,self.y
		self.dragon = images["dragonL"]
		self.chao = pygame.Rect(self.x+60, self.y+114,  45,10)
		self.chaoright = pygame.Rect(self.x+60+self.velocity, self.y+114, 45,10)
		self.chaoleft = pygame.Rect(self.x+60-self.velocity, self.y+114, 45,10)
		self.chaoup = pygame.Rect(self.x+60, self.y+114-self.velocity, 45,10)
		self.chaodown = pygame.Rect(self.x+60, self.y+114+self.velocity, 45,10)
		self.visao = pygame.Rect(self.x+20, self.y+87, 60,60)
		if mago.chao.colliderect(self.visao) and not mago.invisible and not self.isdead():
			mago.lower(2)
	def moveup(self,mago):
	   if not self.frozen:
		self.position = self.x, self.y = self.x,self.y-self.velocity
		self.dragon = images["dragonU"]
		self.chao = pygame.Rect(self.x+60, self.y+94, 45,45)
		self.chaoright = pygame.Rect(self.x+60+self.velocity, self.y+114, 45,10)
		self.chaoleft = pygame.Rect(self.x+60-self.velocity, self.y+114, 45,10)
		self.chaoup = pygame.Rect(self.x+60, self.y+114-self.velocity, 45,10)
		self.chaodown = pygame.Rect(self.x+60, self.y+114+self.velocity, 45,10)
		self.visao = pygame.Rect(self.x+50, self.y+20, 60,60)
		if mago.chao.colliderect(self.visao) and not mago.invisible and not self.isdead():
			mago.lower(2)
	def movedown(self,mago):
	   if not self.frozen:
		self.position = self.x, self.y = self.x,self.y+self.velocity
		self.dragon = images["dragonD"]
		self.chao = pygame.Rect(self.x+60, self.y+94, 45,45)
		self.chaoright = pygame.Rect(self.x+60+self.velocity, self.y+114, 45,10)
		self.chaoleft = pygame.Rect(self.x+60-self.velocity, self.y+114, 45,10)
		self.chaoup = pygame.Rect(self.x+60, self.y+114-self.velocity, 45,10)
		self.chaodown = pygame.Rect(self.x+60, self.y+114+self.velocity, 45,10)
		self.visao = pygame.Rect(self.x+50, self.y+134, 60,60)
		if mago.chao.colliderect(self.visao) and not mago.invisible and not self.isdead():
			mago.lower(2)
	
	def isdead(self):
		return self.life == 0
	def frozen(self):
		self.frozen = True
	def update(self):
		# print chao.top
		#self.chao = pygame.sprite.Sprite()  .rect
		#self.chao = pygame.Rect(self.x+60, self.y+114, 45,10)
		#self.chao.image = pygame.image.load("bola.png")
		
		# Laterais possiveis
		#self.chaoright = pygame.Rect(self.x+62, self.y+114, 45,10)
		#self.chaoleft = pygame.Rect(self.x+58, self.y+114, 45,10)
		#self.chaoup = pygame.Rect(self.x+60, self.y+112, 45,10)
		#self.chaodown = pygame.Rect(self.x+60, self.y+116, 45,10)
		self.position = self.x, self.y 
		self.chao = pygame.Rect(self.x+60, self.y+94, 45,45)
		"""Deixa o chão visível"""
		#pygame.draw.rect(self.screen, (255,255,255),self.chao) 
		#pygame.draw.rect(self.screen, (255,255,50),self.visao)
		# Update of Dragon 
		self.screen.blit(self.dragon,self.position)
		# Update of Life 
		textlife = font_of_life.render("%.2f"%(self.life)+"%", True,  (255,255, 255)) #self.color_of_life) white default
		textRectlife = self.x+60,self.y-22,self.x,self.y
		barralife = pygame.Rect(self.x+62, self.y-8, 36.0/200*self.life ,6)
		borda = pygame.Rect(self.x+60, self.y-10, 40,10)
		# Drawing the group of borda, bar of life and text of percent	
		self.screen.blit(images['sombra'],(self.x+58, self.y-12))		
		pygame.draw.rect(self.screen, (255,255,255), borda)
		pygame.draw.rect(self.screen, self.color_of_life, barralife)
		self.screen.blit(textlife, textRectlife)
