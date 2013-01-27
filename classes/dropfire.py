# -*- coding: utf-8 -*-
import pygame
import sys


images = {}

images["drop"] = pygame.image.load("./images/drop.png").convert_alpha()

class Drop:
	"""
	Class to create Drops' fire
	"""
	def __init__(self, destino, screen): 
		
		self.to_x, self.to_y = destino
		x,y = destino
		destino = x-5,y-538
		self.x, self.y = destino
		self.tipo = images["drop"]
		self.screen = screen
		self.exploded = False
		self.chao = pygame.Rect(self.to_x, self.to_y, 20,10)
		
		
	def update(self): 			
		if self.y+38>self.to_y:		
			self.exploded= True
		#pygame.draw.rect(self.screen, (255,255,255),self.chao)
		self.screen.blit(self.tipo, (self.x,self.y))
		self.y+=18	
