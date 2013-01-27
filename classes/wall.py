# -*- coding: utf-8 -*-
import pygame

images = {}

images["parede1"] = pygame.image.load("./images/parede1.png").convert_alpha()
images["parede2"] = pygame.image.load("./images/parede.png").convert_alpha()
class Wall(pygame.sprite.Sprite):
	"""
	Class to create walls
	"""
	def __init__(self, posInitial, tipo, screen):
                pygame.sprite.Sprite.__init__(self)
		self.x,self.y = posInitial
		if tipo == "parede1":
			self.chao = pygame.Rect((self.x+6,self.y+84),(436,15))
		elif tipo == "parede2":
			self.chao = pygame.Rect((self.x,self.y+78),(150,61))
		self.tipo = tipo	
		self.screen = screen

	def update(self):
		if self.tipo == "parede1":
			self.chao = pygame.Rect((self.x+6,self.y+84),(436,15))
		elif self.tipo == "parede2":
			self.chao = pygame.Rect((self.x,self.y+78),(150,61))
		#pygame.draw.rect(self.screen, (255,100,255), self.chao) # if you want see the floor under the wall
		self.screen.blit(images[self.tipo],(self.x,self.y))
