# -*- coding: utf-8 -*-
import pygame
import sys


images = {}

images["redball"] = pygame.image.load("./images/fireball.png").convert_alpha()
images["blueball"] = pygame.image.load("./images/iceball.png").convert_alpha()
def verifynotcollision(side, mago, objects, quem):
	"""
	Gets the side to where you wish move, the mago and all objects on screen
	This function verify if the mago is colliding with anything
	"""
	ok= [0]*len(objects)
	for objecto in range(len(objects)):
		if side =="left" and mago.chaoleft.colliderect(objects[objecto].chao):
			ok[objecto]=1
			try:
				if quem.color=="red":
					objects[objecto].burning()
			except: pass
		elif side =="right" and mago.chaoright.colliderect(objects[objecto].chao):
			ok[objecto]=1
			try:
				if quem.color=="red":
					objects[objecto].burning()
			except: pass
		elif side =="up" and mago.chaoup.colliderect(objects[objecto].chao):
			ok[objecto]=1
			try:
				if quem.color=="red":
					objects[objecto].burning()

			except: pass
		elif side =="down" and mago.chaodown.colliderect(objects[objecto].chao):
			ok[objecto]=1
			try:
				if quem.color=="red":
					objects[objecto].burning()
					
			except: pass
	for value in range(len(ok)):
		if ok[value]!=0:
			return False, objects[value]
	return True, 0

def verifyexplosion(self, direction, things, vivos, quanto, quem):
		"""
		This function verify if the projectile doesnt collide anything, then move it
		Else, if it collides, verify if this thing is colliding a live object, then do lower() and explod
		"""
		velocity=8 # 8 km/h vruuuuum
		if verifynotcollision(direction,self, things, quem)[0]: 
			self.position = self.x1, self.y1 = self.x1+self.cos*velocity, self.y1+self.sen*velocity
		else: 				
			colisao = verifynotcollision(direction,self, vivos, quem)
			if not colisao[0]:
				if quem.color=="blue":
					colisao[1].frozen = True
				else:
					colisao[1].lower(quanto)
					if colisao[1].frozen:
						colisao[1].lower(quanto*20)
				
			self.exploded =True
	



class Projeteis:
	"""
	Class to create Projetil/Projectile
	"""
	def __init__(self, projetil, posInitial, posFinal, screen, mago_direction, quanto, quem): 
		x,y = posInitial
		self.x1,self.y1 =posInitial
		self.x2,self.y2 =posFinal
		self.position = self.x, self.y = x+5, y+30
		self.projetil = images[projetil]
		self.screen = screen
		self.exploded = False
		self.chao = pygame.Rect(self.x+5, self.y+30, 20,10)
		self.direction = mago_direction
		self.quanto = quanto
		self.quem = quem
		self.cos = (float(self.x2-self.x1))/(((float(self.x2-self.x1))**2)+((float(self.y2-self.y1))**2))**0.5
		self.sen = (float(self.y2-self.y1))/(((float(self.x2-self.x1))**2)+((float(self.y2-self.y1))**2))**0.5
		# Laterais possiveis
		self.chaoright = pygame.Rect(self.x1+7, self.y1+30, 20,10)
		self.chaoleft = pygame.Rect(self.x1+3, self.y1+30, 20,10)
		self.chaoup = pygame.Rect(self.x1+5, self.y1+28, 20,10)
		self.chaodown = pygame.Rect(self.x1+5, self.y1+32, 20,10)
		
		
	def update(self, things, vivos): 
		
		# This verify if the figure direction is the same of the projecttile
		if   self.direction == "magoR" and self.cos>=0 and abs(self.sen)<=0.9:
			verifyexplosion(self, "right", things, vivos, self.quanto, self.quem)
		elif self.direction == "magoL" and self.cos<=0 and abs(self.sen)<=0.9:
			verifyexplosion(self, "left", things, vivos, self.quanto, self.quem)
		elif self.direction == "magoD" and self.sen>=0 and abs(self.cos)<=0.9:
			verifyexplosion(self, "down", things, vivos, self.quanto, self.quem)
		elif self.direction == "magoU" and self.sen<=0 and abs(self.cos)<=0.9:
			verifyexplosion(self, "up", things, vivos, self.quanto, self.quem)
		else:
			#This else not is a good idea, but i havent another
			self.position = self.x1, self.y1 = 1000,1000			
			self.exploded= True
			
		# print chao.top
		self.chao = pygame.Rect(self.x1+5, self.y1+30, 20,10)
		#pygame.draw.rect(self.screen, (255,255,255),self.chao)

		# Laterais possiveis
		self.chaoright = pygame.Rect(self.x1+7, self.y1+30, 20,10)
		self.chaoleft = pygame.Rect(self.x1+3, self.y1+30, 20,10)
		self.chaoup = pygame.Rect(self.x1+5, self.y1+28, 20,10)
		self.chaodown = pygame.Rect(self.x1+5, self.y1+32, 20,10)
	
		self.screen.blit(self.projetil, self.position)
		
