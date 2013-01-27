# -*- coding: utf-8 -*-
import pygame
pygame.init()
images = {}

images["potion1"] = pygame.image.load("./images/Potion-icon.png").convert_alpha()
images["potion2"] = pygame.image.load("./images/Magic-potion.png").convert_alpha()
images["potion3"] = pygame.image.load("./images/Magic-potion-mana.png").convert_alpha()
images["earrings"] = pygame.image.load("./images/earrings.png").convert_alpha()
class Item(pygame.sprite.Sprite):
	"""
	Class to create items
	"""
	def __init__(self, posInitial, tipo, screen):
                pygame.sprite.Sprite.__init__(self)
		self.x,self.y = posInitial
		self.chao = pygame.Rect((self.x+14,self.y+20),(14,20))
		self.tipo = tipo
		self.screen = screen
		self.burned = False

	def update(self):
		self.chao = pygame.Rect((self.x+14,self.y+20),(14,20))
		#pygame.draw.rect(self.screen, (255,100,255), self.chao) # if you want see the floor under the tree
		self.screen.blit(images[self.tipo],(self.x,self.y))

