# -*- coding: utf-8 -*-
import pygame

images = {}

images["porta1"] = pygame.image.load("images/porta1.png")

class Gate(pygame.sprite.Sprite):
	"""
	Class to create gates
	"""
	def __init__(self, posInitial, tipo, screen):
                pygame.sprite.Sprite.__init__(self)
		self.x,self.y = posInitial
		self.chao = pygame.Rect((self.x+6,self.y+84),(244,15))
		# Possibles collisions 
		self.chaoright = pygame.Rect((self.x+8,self.y+84),(244,15))
		self.chaoleft = pygame.Rect((self.x+4,self.y+84),(244,15))
		self.chaoup = pygame.Rect((self.x+6,self.y+82),(244,15))
		self.chaodown = pygame.Rect((self.x+6,self.y+86),(244,15))
		self.tipo = tipo
		self.screen = screen

	def update(self):	
		self.chao = pygame.Rect((self.x+6,self.y+84),(244,15))
		# Possibles collisions 
		self.chaoright = pygame.Rect((self.x+8,self.y+84),(244,15))
		self.chaoleft = pygame.Rect((self.x+4,self.y+84),(244,15))
		self.chaoup = pygame.Rect((self.x+6,self.y+82),(244,15))
		self.chaodown = pygame.Rect((self.x+6,self.y+86),(244,15))
		#pygame.draw.rect(self.screen, (255,100,255), self.chao) # if you want see the floor under the gate
		self.screen.blit(images[self.tipo],(self.x,self.y))
