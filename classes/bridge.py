# -*- coding: utf-8 -*-
import pygame

images = {}

images["left"] = pygame.image.load("images/paredeponteleft.png").convert_alpha()
images["right"] = pygame.image.load("images/paredeponteright.png").convert_alpha()
images["chao"] = pygame.image.load("images/chaoponte.png").convert_alpha()

class Bridge(pygame.sprite.Sprite):
	"""
	Class to create bridges
	"""
	def __init__(self, posInitial, tipo, screen):
                pygame.sprite.Sprite.__init__(self)
		self.x,self.y = posInitial
		self.tipo = tipo
		self.screen = screen
		if self.tipo=="chao":
			self.chaotowalk = []
			b=0
			for i in range(0,57, 2):
				if i<18:
					b-=3
				else:
					b+=5			
				self.chaotowalk.append((pygame.Rect((self.x+160-i*3+b,self.y-11+i*4),(110,7))))
				self.chaotowalk.append((pygame.Rect((self.x+160-i*3+b,self.y-11+i*4+6),(110,7))))
				self.chaotowalk.append((pygame.Rect((self.x+160-i*3+b,self.y-11+i*4+12),(110,7))))
			self.chao = pygame.Rect((self.x-1000,self.y-10),(190,20))
			for chao in self.chaotowalk:	
				pygame.draw.rect(self.screen, (255,100,100), chao)
		elif self.tipo=="left":
			self.x,self.y = posInitial
			self.x-=30
			self.y-=55
			self.chao = pygame.Rect((self.x,self.y+250),(100,10))
		elif self.tipo=="right":
			self.x,self.y = posInitial
			self.x+=185
			self.y-=30
			self.chao = pygame.Rect((self.x+20,self.y+250),(100,10))
			

	def update(self):
		self.screen.blit(images[self.tipo],(self.x,self.y))
		if self.tipo=="chao":
			self.chaotowalk = []
			b=0
			for i in range(0,57, 2):
				if i<18:
					b-=3
				else:
					b+=5			
				self.chaotowalk.append((pygame.Rect((self.x+160-i*3+b,self.y-11+i*4),(110,7))))
				self.chaotowalk.append((pygame.Rect((self.x+160-i*3+b,self.y-11+i*4+6),(110,7))))
				self.chaotowalk.append((pygame.Rect((self.x+160-i*3+b,self.y-11+i*4+12),(110,7))))
			self.chao = pygame.Rect((self.x-1000,self.y-10),(190,20))
			#for chao in self.chaotowalk:
			#	pygame.draw.rect(self.screen, (255,100,100), chao)
		elif self.tipo=="left":
			self.chao = pygame.Rect((self.x,self.y+50),(100,10))
		elif self.tipo=="right":
			self.chao = pygame.Rect((self.x,self.y+250),(100,10))
		
		#pygame.draw.rect(self.screen, (255,100,255), self.chao) # if you want see the floor under the tree
		
