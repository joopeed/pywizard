# -*- coding: utf-8 -*-
import pygame
from time import sleep
pygame.init()
images = {}

images["lago"] = pygame.image.load("./images/lago.png").convert_alpha()
images["lago2"] = pygame.image.load("./images/lago2.png").convert_alpha()
class Lagoon(pygame.sprite.Sprite):
	"""
	Class to create lagoons
	"""
	def __init__(self, posInitial, screen):
                pygame.sprite.Sprite.__init__(self)
		self.x,self.y = posInitial
		self.chao = pygame.Rect((self.x,self.y-30),(900,186))
		self.tipo = "lago"
		self.screen = screen

	def update(self):
		
		self.chao = pygame.Rect((self.x,self.y-30),(900,186))
		self.screen.blit(images[self.tipo],(self.x,self.y))
		#pygame.draw.rect(self.screen, (255,100,255), self.chao) # if you want see the floor under the tree
	def movement(self):
		self.tipo ="lago2"
	def unmovement(self):
		self.tipo ="lago"
