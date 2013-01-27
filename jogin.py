# -*- coding: utf-8 -*-
"""

Development by
João Pedro Ferreira de Melo Leôncio
Hugo Nicodemos Brito

"""

import sys, pygame, random, os, urllib

# TESTE DE REDE
"""
import socket

HOST = ''
PORT = 15001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
# TESTE DE REDE

"""

pygame.init()

size = wid, hei = 800, 600
back = 30, 150, 30
 
screen = pygame.display 
screen.set_caption("WizardPy")
screen =pygame.display.set_mode(size,pygame.FULLSCREEN)
#screen = screen.set_mode( | pygame.FULLSCREEN)



from sets import Set
from time import sleep
sys.path.append('./classes')
from dragon import *
from wizard import *
from wall import *
from gate import *
from button import *
from tree import *
from bush import *
from items import *
from dropfire import *
from lago import *
from bridge import *
from port import *
from queen import *


# Buffer musics
pygame.mixer.music.load("musics/quebranozes.mp3")
pygame.mixer.music.play(1)    
pygame.mixer.music.queue('musics/hedwigstheme.mp3')
pygame.mixer.music.play(-1,4)
# End of buffer musics


# Fonts
pygame.font.init()
font_big = pygame.font.Font(None, 35)
font_medium = pygame.font.Font(None, 22)
font_small = pygame.font.Font(None, 15)
font_death = pygame.font.Font(None, 35)
font_of_life_top = pygame.font.Font(None, 20)
# End Fonts
"""
nick = raw_input()
s = urllib.urlopen('http://twitter.com/'+nick)
data = s.read()	
data = data.split()
for i in range(len(data)):
	if 'id="profile-image"' in data[i]:
		foto = data[i+1][5:-1]
		break
s = urllib.urlopen(foto)
data = s.read()
f = open('foto.jpg', 'wb')	
f.write(data)
f.close()
"""

# Buffer image
images = {}
images["logo"] = pygame.image.load("images/logo2.png").convert_alpha()
images["janela"] = pygame.image.load("images/janela.png").convert_alpha()
images["janela2"] = pygame.image.load("images/janela2.png").convert_alpha()
images["janela3"] = pygame.image.load("images/janela3.png").convert_alpha()
images["janela4"] = pygame.image.load("images/janela4.png").convert_alpha()
images["one"] = pygame.image.load("images/one.png").convert_alpha()
images["two"] = pygame.image.load("images/two.png").convert_alpha()
images["back2"] = pygame.image.load("images/back2.jpg").convert_alpha()
images["redpower1"] = pygame.image.load("images/firepower1.png").convert_alpha()
images["redpower2"] = pygame.image.load("images/firepower2.png").convert_alpha()
images["redpower3"] = pygame.image.load("images/firepower3.png").convert_alpha()
images["bluepower1"] = pygame.image.load("images/icepower1.png").convert_alpha()
images["bluepower2"] = pygame.image.load("images/icepower2.png").convert_alpha()
images["bluepower3"] = pygame.image.load("images/icepower3.png").convert_alpha()
images["twig"] = pygame.image.load("images/twig.png").convert_alpha()
images["health"] = pygame.image.load("images/health.png").convert_alpha()
images["mana"] = pygame.image.load("images/mana.png").convert_alpha()
images["potion2"] = pygame.image.load("images/potiongrande.png").convert_alpha()
images["potion3"] = pygame.image.load("images/manapotiongrande.png").convert_alpha()
images["earrings"] = pygame.image.load("images/earringsgrande.png").convert_alpha()
images["circ"] = pygame.image.load("images/circ.png").convert_alpha()
images["janelinha"] = pygame.image.load("images/janelinha.png").convert_alpha()
images["area"] = pygame.image.load("images/areaattack.png").convert_alpha()
#images["fototwitter"] = pygame.image.load("foto.jpg").convert_alpha()
# End of buffer image


# Information of powers
info = {}	
info["mensagempadrao"] = u'Hover the mouse on\nthe power to show\nmore information\n'
info["redpower1"] = u"Press 1 to choose this:\nLaunch fire balls\n(Cooldown)\n(Doesn't need mana)\n"
info["redpower2"] = u'Press 2 to choose this:\nZone Attack\nExplosion (Needs mana)\n'
info["redpower3"] = u'Press 3 to choose this:\nFire Wall\nwhile you walk (Needs mana)\n'
info["bluepower1"] = u"Press 1 to choose this:\nLaunch ice cubes\n(Cooldown)\n(Doesn't need mana)\n"
info["bluepower2"] = u'Press 2 to choose this:\nMake it rain and your\nenemies left health\n(Needs mana)\n'
info["bluepower3"] = u'Press 3 to choose this:\nUndefined\n (Needs mana)\n'
info["potion2"] = u'The Great Pot:\nUse this item and\nrecover your\n fully health\n'
info["potion3"] = u'The Mana Pot:\nUse this item and\nrecover your\n fully mana\n'
info["earrings"] = u'The earrings \nof Queen:\nGive this item\n to the Queen\n'
# End Information of powers
rect_powers = {}


# Names of Wizards
Wizard_colors = {"Myrkur":"black","    Vel":"white","  Kalt":"blue","  Eldur":"red" }

def blitainfos(screen, info , pos ):
	x,y = pos
	mais = 0
	ultimo = 0
	for i in range(len(info)):
		if info[i]=='\n':		
			text_info = font_small.render(info[ultimo:i], True,(255,255, 255))
			screen.blit(text_info,(x, y+mais))
			mais +=10
			ultimo = i+1

def organize( group_objects, things, vivos):

	"""
	This function gets the group of objects is on screen and organize
	ordered by their Y coordinate
	"""
	group_objects2 = group_objects
	group_objects = []
	for theobject in group_objects2:
		group_objects.append([theobject])

	for theobject in group_objects:
		theobject.append(theobject[0].chao.top)

	ordered_objects = sorted(group_objects, key=lambda theobject: theobject[1])
	for theobject in ordered_objects:
		try:
			theobject[0].update(things, vivos)
		except:
			theobject[0].update()
			
	
			

def verifynotcollision(side, Wizard, objects):
	"""
	Gets side of you wish move the Wizard and all objects on screen
	This function verify if the Wizard is colliding with anything
	"""
	ok= [0]*len(objects)
	for objecto in range(len(objects)):
		if side =="left" and Wizard.chaoleft.colliderect(objects[objecto].chao):
			ok[objecto]=1
		elif side =="right" and Wizard.chaoright.colliderect(objects[objecto].chao):
			ok[objecto]=1
		elif side =="up" and Wizard.chaoup.colliderect(objects[objecto].chao):
			ok[objecto]=1
		elif side =="down" and Wizard.chaodown.colliderect(objects[objecto].chao):
			ok[objecto]=1
	for value in range(len(ok)):
		if ok[value]!=0:
			return False, objects[value]
	return True, 0

def movemonsters( anda_dragons , monster, things, vermei):
	if not monster.isdead():
		for direction, quanto in anda_dragons.items():
			if direction == "left":	
				if quanto!=0 and verifynotcollision("left", monster, things)[0]:
					monster.moveleft(vermei)
					anda_dragons[direction]-=1
				elif not verifynotcollision("left", monster, things)[0]:
					monster.moveright(vermei)
					anda_dragons["right"]-=1
					break
			elif direction == "right":	
				if quanto!=0  and verifynotcollision("right", monster, things)[0]:
					monster.moveright(vermei)
					anda_dragons[direction]-=1
					break
				elif not verifynotcollision("right", monster, things)[0]:
					monster.moveleft(vermei)
					anda_dragons["left"]-=1
					break
			elif direction == "up":	
				if quanto!=0  and verifynotcollision("up", monster, things)[0]:
					monster.moveup(vermei)
					anda_dragons[direction]-=1
					break
				elif not verifynotcollision("up", monster, things)[0]:
					monster.movedown(vermei)
					anda_dragons["down"]-=1
					break
			elif direction == "down":
				if quanto!=0  and verifynotcollision("down", monster, things)[0]:
					monster.movedown(vermei)
					anda_dragons[direction]-=1
					break
				elif not verifynotcollision("down", monster, things)[0]:
					monster.moveup(vermei)
					anda_dragons["up"]-=1
					break
		
def powers(color, kind, Wizard, destination, vivos):
	if color=="red" or color=="blue":
		if kind ==1:
			Wizard.primary_attack(destination)
		elif kind ==2:
			Wizard.second_attack(destination, vivos)
def insertjungle( x,y , list_trees):
	#for i in range(len(list_trees)-1,-1,-1):
	#	list_trees.pop(i)
	list_trees.append(Tree((x+100,y+50), "tree2", screen))
	list_trees.append(Tree((x+200,y), "tree2", screen))
	list_trees.append(Tree((x,y), "tree2", screen))
	list_trees.append(Tree((x+30,y+25), "tree2", screen))
	list_trees.append(Tree((x+130,y+25), "tree2", screen))

def insertlineBushs(y , list_Bushs):
	for x in range(-20,800,120):
		list_Bushs.add(Bush((x,y), "arbusto", screen))
	for x in range(0,800,130):
		list_Bushs.add(Bush((x,y+20), "arbusto", screen))
def addtolist( lists , where ):
	for listy in lists:
		for element in listy:
			where.append(element)
def downthings( things ):
	for thing in things:
		for thingy in thing:
			thingy.y+=1
def upthings( things ):
	for thing in things:
		for thingy in thing:
			thingy.y-=1
def verifygatewithwizard(gate, wizards):
			for i in range(len(wizards)):
				if gate.chaoleft.colliderect(wizards[i].chao):
					return True
			return False

pygame.mouse.set_visible(False)
n=1000
while n>0:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
	if pygame.key.get_pressed()[pygame.K_SPACE]:
		break
	pygame.display.flip()
	screen.fill((n/10,n/10,n/10))
	screen.blit(images["logo"], (50,100))
	n-=1
magic_lagoon = [False, False]

"""
First, create the object here.
After, the object to list of things and to group of objects inside while.
"""

anda_back=0
anda_Gate=0
anda_tudo=0
tempo = 0
attack = 1 #Default is 1
pontos=0
pottime=0
magic_lagoon_time=0
vai=0
### Declaration of objects ###
## PS. All objects are declared with top-left coordinates...
wizards = []
wizards.append(Wizard("  Kalt", Wizard_colors["  Kalt"],(300,300), screen, True))
wizards.append(Wizard("  Eldur", Wizard_colors["  Eldur"],(400,400), screen, True))




queens = []
queens.append(Queen(" Queen",(500,-1300), screen, True))

# Dragons
dragons = []
dragons.append(Dragon((120,-220), screen))
dragons.append(Dragon((200,450), screen))
dragons.append(Dragon((400,-450), screen))
dragons.append(Dragon((100,-500), screen))
dragons.append(Dragon((200,-650), screen))
dragons.append(Dragon((400,-750), screen))
# Sequence of movimentation
anda_dragons = [{
"right":random.randint(20,100),
"down":random.randint(20,100),
"left":random.randint(20,100),
"up":random.randint(20,100)} 
for i in range(6)]

# Bushs
list_Bushs = Set()
insertlineBushs(-300, list_Bushs)
burneds = Set()
# Items
list_items = Set()
list_items.add(Item((400,400), "potion2", screen))
list_items.add(Item((400,-400), "potion2", screen))
list_items.add(Item((600,500), "potion3", screen))
list_items.add(Item((500,-420), "earrings", screen))
list_items.add(Item((500,320), "earrings", screen))
# Walls
list_walls = Set()
list_walls.add(Wall((-40,199), "parede1", screen))
list_walls.add(Wall((500,201), "parede1", screen))
#list_walls.add(Wall((500,7), "parede2", screen))
#list_walls.add(Wall((500,-50), "parede2", screen))
list_walls.add(Wall((-40,0), "parede1", screen))
list_walls.add(Wall((-40,-1401), "parede1", screen))
list_walls.add(Wall((500,-1399), "parede1", screen))
# Trees
list_trees = []
insertjungle( -80,200, list_trees)
insertjungle( 500,350, list_trees)
insertjungle( 50,120, list_trees)
insertjungle( 500,-350, list_trees)
insertjungle( -80,-220, list_trees)
insertjungle( 0,-500, list_trees)
insertjungle( -80,-220, list_trees)
insertjungle( 40,-820, list_trees)
insertjungle( 100,-620, list_trees)
insertjungle( -80,-920, list_trees)
# Gates
list_gates = Set()
list_gates.add(Gate((367,200), "porta1", screen))
list_gates.add(Port((272,-1506), "portao", screen))
# Buttons
list_buttons = Set()
list_buttons.add(Button((600,310), "botao", screen))
list_buttons.add(Button((600,160), "botao", screen))

list_lagoons = Set()
list_lagoons.add(Lagoon((-40,-1000), screen))

list_bridges = []

#list_bridges.append(Bridge((200,320), "chao", screen))
#list_bridges.append(Bridge((200,320), "left", screen))
#list_bridges.append(Bridge((200,320), "right", screen))
zera =  pygame.time.get_ticks()
inicio = pygame.time.get_ticks()
kill = [0,0,0]

while True:
	"""
	Main loop :) 
	Its not messy anymore :)
	"""
	

	# Dynamic background #
	pygame.display.flip()	
	#screen.fill(back)
	for i in range(-2000,2000,109):
		screen.blit(images["back2"], (0,i-anda_back))
		screen.blit(images["back2"], (598,i-anda_back))
	# Dynamic background #

	# Remove the burneds Bushs and the dead dragons of the lists
	for bush in list_Bushs:
		if bush.burned and bush not in burneds:
			burneds = burneds | Set([bush])
	list_Bushs -=burneds	

	for i in range(len(dragons)-1,-1,-1):
		if dragons[i].isdead():
			dragons.pop(i)
			pontos+=200/(pygame.time.get_ticks()/20000. -(zera/20000.))
			zera = pygame.time.get_ticks()
			break
	# Remove the burneds Bushs and the dead dragons of the lists
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()

	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		#arquivo=open("/home/joopeed/Dropbox/Public/pontos.html",'a')
		#arquivo.write("%4i points com "%pontos+vermei.name+"</br>" )
		#arquivo.close()
		sys.exit()
	for i in range(len(wizards)):
		""" Grid of possible things to the Wizard collide """
		things = []
		addtolist( [list_trees, list_Bushs, list_walls, list_gates, list_lagoons, list_bridges, dragons, queens, [wizards[list(Set(range(len(wizards)))-Set([i]))[0]] ] ], things )
		"""Grid of things, unicluding the dragons, because it doesnt collide theirselves"""	
		things2 = []
		addtolist( [list_trees, list_Bushs, list_walls, list_items, list_gates, list_lagoons,list_bridges, queens, wizards], things2 )	
		""" Grid of possible things to organize """
		group_objects = []
		addtolist( [list_trees, list_Bushs, list_walls, list_gates, list_items, list_lagoons,list_bridges, dragons, queens, projectiles, drops, wizards ], group_objects )
		""" Grid of possible things living """
		vivos = []
		addtolist( [dragons, wizards], vivos )






		# If the Wizard pass on the item he gets it
		for item in list_items:
			if wizards[i].chao.colliderect(item.chao):
				wizards[i].items[item.tipo]+=1
				list_items-=Set([item])
				break
	

		def collidechaotowalk(chaos,indice, wizardchao):
			if chaos:
				for chao in chaos[indice].chaotowalk:
					if chao.colliderect(wizardchao):
						return True
			return False
		
		if i==1:
			# Move the Wizard before the screen, if thats possible
			if pygame.key.get_pressed()[pygame.K_a] and wizards[i].x > 7 and (verifynotcollision("left",wizards[i], things)[0] or collidechaotowalk(list_bridges, 0,wizards[i].chaoleft)):
				wizards[i].moveleft()
				#conn.sendall("L")
			if pygame.key.get_pressed()[pygame.K_d] and wizards[i].x < wid-45 and (verifynotcollision("right",wizards[i], things)[0] or collidechaotowalk(list_bridges, 0,wizards[i].chaoright)): 
				wizards[i].moveright()
				#conn.sendall("R")
		
		
			if pygame.key.get_pressed()[pygame.K_s] and wizards[i].y < hei-128 and (verifynotcollision("down",wizards[i], things)[0]  or collidechaotowalk(list_bridges, 0,wizards[i].chaodown)):
				#conn.sendall("D")
				wizards[i].movedown()
				anda_tudo+=1
	
				if anda_tudo <0 and anda_tudo>-1640:				
					
					wizards[0].y-=1
					upthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons,queens,list_lagoons,list_bridges, projectiles,dragons])		
					#for dragon in dragons:		
						#if not dragon.isdead():			
						#	dragon.moveup(wizards[i])
						#else:
						#	dragon = Dragon((-1000,-150), screen)
					anda_back+=1
				else:
					wizards[i].y+=1
		
			if pygame.key.get_pressed()[pygame.K_w] and wizards[i].y > 12 and (verifynotcollision("up",wizards[i], things)[0]  or collidechaotowalk(list_bridges, 0,wizards[i].chaoup)): 
				#conn.sendall("U")
				wizards[i].moveup()
				anda_tudo-=1
				if anda_tudo <0 and anda_tudo>-1640:
					wizards[0].y+=1	
					downthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, queens, list_lagoons,list_bridges,projectiles, dragons])
					#for dragon in dragons:
						#if not dragon.isdead():			
						#	dragon.movedown(wizards[i])
						#else:
						#	dragon = Dragon((-1000,-150), screen)
					anda_back-=1
				else:
					wizards[i].y-=1
				
		if pygame.mouse.get_pressed()[0] and tempo>timeattack1:
			powers(wizards[vai].color, attack, wizards[vai], pygame.mouse.get_pos(), vivos)
			tempo = 0
			if vai:
				vai=0
			else:
				vai=1
	
		if i==0:
			# Move the Wizard before the screen, if thats possible
			if pygame.key.get_pressed()[pygame.K_LEFT] and wizards[i].x > 7 and (verifynotcollision("left",wizards[i], things)[0]   or collidechaotowalk(list_bridges, 0,wizards[i].chaoleft)):
				wizards[i].moveleft()
			if pygame.key.get_pressed()[pygame.K_RIGHT] and wizards[i].x < wid-45 and (verifynotcollision("right",wizards[i], things)[0]   or collidechaotowalk(list_bridges, 0,wizards[i].chaoright)):
				wizards[i].moveright()
			if pygame.key.get_pressed()[pygame.K_DOWN] and wizards[i].y < hei-128 and (verifynotcollision("down",wizards[i], things)[0]  or collidechaotowalk(list_bridges, 0,wizards[i].chaodown)):
				wizards[i].movedown()
				wizards[i].y+=1
			if pygame.key.get_pressed()[pygame.K_UP] and wizards[i].y > 12 and (verifynotcollision("up",wizards[i], things)[0]   or collidechaotowalk(list_bridges, 0,wizards[i].chaoup)): 
				wizards[i].moveup()
				wizards[i].y-=1	

				
	
	
		for j in range(len(dragons)):
			movemonsters( anda_dragons[j], dragons[j], things2, wizards[i] )
			if sum(anda_dragons[j].values())==0	:
				anda_dragons[j] = {"right":random.randint(20,100),"down":random.randint(20,100),"left":random.randint(20,100),"up":random.randint(20,100)}
				
		# if the Wizard is on the button, the gate opens
		ok=0
		for button in list_buttons:
			if button.chao.colliderect(wizards[0].chao) or (pygame.key.get_pressed()[pygame.K_SPACE] and not pygame.key.get_pressed()[pygame.K_LSHIFT]):
				ok+=1
		
		for gate in list_gates:
			#print button.chao.colliderect(wizards[i].chao) or pygame.key.get_pressed()[pygame.K_RIGHT]	
 			if ok>0 and gate.tipo!="portao":
				if gate.x<=500:		
					gate.x+=1
			elif not verifygatewithwizard(gate, wizards) and gate.tipo!="portao": # Verify the collision when the gate is closing
					if gate.x>=370:
						gate.x-=1
		
		
	
		if pygame.key.get_pressed()[pygame.K_LSHIFT] and pygame.key.get_pressed()[pygame.K_SPACE]:
			wizards[i].lower(1)
		if pygame.key.get_pressed()[pygame.K_LSHIFT] and pygame.key.get_pressed()[pygame.K_z]:
			wizards[i].upper(5)
	
	
		# Recover mana
		if ((pygame.time.get_ticks()-inicio)/60)%5==0:
			for lag in list_lagoons:
				lag.unmovement()
		else:
			for lag in list_lagoons:
				lag.movement()

		if ((pygame.time.get_ticks()-inicio)/600)%5==0:
			wizards[i].uppermana(1)
			for queen in queens:
				queen.unmovement()
		else:
			
			for queen in queens:
				queen.movement()

		# Change the attack for mouse
		if pygame.key.get_pressed()[pygame.K_1]:
			attack = 1
		timeattack1= 50
		if pygame.key.get_pressed()[pygame.K_2]:
			attack = 2
		
		if pygame.key.get_pressed()[pygame.K_k]:
			kill[0]=1
		if pygame.key.get_pressed()[pygame.K_i]:
			kill[1]=1
		if pygame.key.get_pressed()[pygame.K_l]:
			kill[2]=1
		if kill==[1,1,1]:
			for dragao in dragons:
				dragao.life=0
		win = pygame.Rect(390, 350, 80 ,13)
		
		
		if anda_tudo <-1800 and wizards[1].chao.colliderect(win) and wizards[0].chao.colliderect(win):
			#and wizards[1].x>322 and wizards[1].x<462 and wizards[1].y<230 and wizards[0].x>322 and wizards[0].x<462 and wizards[0].y<230:
			# When the Wizard is dead, show a message on screen
			text_death = font_death.render(u'Oh! You win!'.decode("utf8"), True,(255,255, 255))
			textRect_death = text_death.get_rect()
			textRect_death.centerx = screen.get_rect().centerx
			textRect_death.centery = screen.get_rect().centery
			screen.blit(text_death, textRect_death)
		elif wizards[i].isdead() and i==1:
			# When the Wizard is dead, show a message on screen
			text_death = font_death.render(u'Oh! '+wizards[i].name.strip()+', The '+wizards[i].color.capitalize()+
			' Wizard is dead, you bastard!'.decode("utf8"), True,(255,255, 255))
			textRect_death = text_death.get_rect()
			textRect_death.centerx = screen.get_rect().centerx
			textRect_death.centery = screen.get_rect().centery
			screen.blit(text_death, textRect_death)
		elif i==1: 
			# Objects and their several floor/chãos
			
			
			"""Remove the exploded projectiles"""		
			projectilesexplodeds = Set()
			for projectile in projectiles:
				if projectile.exploded:
					projectilesexplodeds = projectilesexplodeds | Set([projectile])
			projectiles -= projectilesexplodeds
			"""Enf of Remove"""
			"""Remove the exploded drops"""		
			dropsexplodeds = Set()
			for drop in drops:
				if drop.exploded:
					dropsexplodeds = dropsexplodeds | Set([drop])
			drops -= dropsexplodeds
			"""Enf of Remove"""
			for button in list_buttons:
				button.update()
				# Blit on screen organized objects :D
					#Objects have life
			
			organize(group_objects, things, vivos)
			
			# MENU of Items
			# Press I to show the menu
			if wizards[i].chao.colliderect(queens[0].chaoget) and wizards[i].items['earrings']:
				screen.blit(images["janela4"], (-100,200))
				text_titulo = font_big.render(u'Give the earring to Queen. Press G'.decode("utf8"), True,(255,255, 255))
				screen.blit(text_titulo, (130,280))
				if pygame.key.get_pressed()[pygame.K_g]:
					wizards[i].items['earrings']-=1
					queens[0].items['earrings']+=1
			if anda_tudo <-1000 and magic_lagoon_time < 150:
				screen.blit(images["janela4"], (-100,200))
				if pygame.key.get_pressed()[pygame.K_o]:
					if magic_lagoon[0]:
						magic_lagoon[1]=True
					else:
						magic_lagoon[0]=True
				if magic_lagoon	== [False, False]:
					text_titulo = font_big.render(u'The Two players has press O'.decode("utf8"), True,(255,255, 255))
					screen.blit(text_titulo, (130,280))
				else:
					if magic_lagoon[0]:
						screen.blit(images["one"], (80,190))
						text_titulo = font_big.render(u'Player 1 pressed'.decode("utf8"), True,(255,255, 255))
						screen.blit(text_titulo, (80,280))
					else:
						text_titulo = font_big.render(u"Player 1 doesn't yet".decode("utf8"), True,(255,255, 255))
						screen.blit(text_titulo, (80,280))
					if magic_lagoon[1]:
						screen.blit(images["two"], (380,190))
						text_titulo = font_big.render(u'Player 2 pressed'.decode("utf8"), True,(255,255, 255))
						screen.blit(text_titulo, (380,280))
					else:
						text_titulo = font_big.render(u"Player 2 doesn't yet".decode("utf8"), True,(255,255, 255))
						screen.blit(text_titulo, (380,280))

			if magic_lagoon[0] and magic_lagoon[1] and magic_lagoon_time < 150:
				if list_bridges==[]:	
					list_bridges.append(Bridge((230,-1019-anda_tudo), "chao", screen))
					list_bridges.append(Bridge((230,-1019-anda_tudo), "left", screen))
					list_bridges.append(Bridge((230,-1019-anda_tudo), "right", screen))
				magic_lagoon_time+=1			
	
			elif pygame.key.get_pressed()[pygame.K_i]:
				screen.blit(images["janela"], (50,10))
				text_titulo = font_big.render(u'Your items'.decode("utf8"), True,(255,255, 255))
				screen.blit(text_titulo, (130,80))
				items = wizards[i].items.keys()
				for it in range(len(items)):
					if wizards[i].items[items[it]]>0:
						screen.blit(images[items[it]], (100+it*110,110))
						screen.blit(images["circ"], (190+it*110,230))
						text_titulo = font_medium.render(str(wizards[i].items[items[it]]), True,(0,0, 0))
						screen.blit(text_titulo, (200+it*110,237))
						if pygame.Rect(150+it*110,180,70,80).collidepoint(pygame.mouse.get_pos()):
							if pygame.mouse.get_pressed()[0] and pottime>10:
								wizards[i].items[items[it]]-=1
								if items[it]=="potion2":
									wizards[i].upper(100)
								elif items[it]=="potion3":	
									wizards[i].uppermana(100)
								pottime =0
							
							else:
								screen.blit(images["janelinha"], (110+it*110,280))
								blitainfos( screen, info[items[it]] ,(130+it*110,290))
			# End of MENU of Items
			
			# MENU of Powers
			# Press P to show the menu
	
			elif pygame.key.get_pressed()[pygame.K_p]:
			#else: #Uncomment and comment the other to fix
				screen.blit(images["janela2"], (-200,437))
				text_titulo = font_medium.render(u'Your powers'.decode("utf8"), True,(255,255, 255))
				screen.blit(text_titulo, (20,497))
				screen.blit(images[wizards[i].color+"power1"], (35,523))
				screen.blit(images[wizards[i].color+"power2"], (105,523))
				screen.blit(images[wizards[i].color+"power3"], (175,523))
				rect_powers["power1"] = pygame.Rect(35,523,63,63)
				rect_powers["power2"] = pygame.Rect(105,523,63,63)
				rect_powers["power3"] = pygame.Rect(175,523,63,63)
				if rect_powers["power1"].collidepoint(pygame.mouse.get_pos()):
					blitainfos( screen, info[wizards[i].color+"power1"] , (265,523) )
				elif rect_powers["power2"].collidepoint(pygame.mouse.get_pos()):
					blitainfos( screen, info[wizards[i].color+"power2"] , (265,523) )
				elif rect_powers["power3"].collidepoint(pygame.mouse.get_pos()):
					blitainfos( screen, info[wizards[i].color+"power3"] , (265,523) )
				else:
					blitainfos( screen, info["mensagempadrao"] , (265,523) )
			# End of Menu of powers
			timetotal = pygame.time.get_ticks()
			if (pygame.time.get_ticks())/1000 < 60:
				minutos = 0
				segundos = (pygame.time.get_ticks()-inicio)/1000
				time = "0:%02i"%(segundos)
			elif (pygame.time.get_ticks()-inicio)/1000 < 3600:
				minutos = (pygame.time.get_ticks()-inicio)/60000
				segundos = (pygame.time.get_ticks()-inicio)/1000
				while segundos >=60:
					segundos-=60
				time = "%02i:%02i"%(minutos, segundos)
			# Life bar
			screen.blit(images["janela3"], (-330,-70))
			screen.blit(images["janela3"], (510,-70))	
			textlife = font_of_life_top.render("%.2f"%(wizards[i].life)+"% of health", True, (255,255,255)) 
			textmana = font_of_life_top.render("%.2f"%(wizards[i].mana)+"% of mana", True, (255,255,255)) 
			textpoints = font_big.render("%4.f Points" %(pontos), True, (255,255,255)) 
			texttime = font_big.render(time, True, (255,255,255))
			barralife = pygame.Rect(17, 14, 144.0/100*wizards[i].life ,8)
			borda = pygame.Rect(13, 10, 152,15)
			barramana = pygame.Rect(17, 31, 144.0/100*wizards[i].mana ,8)
			bordamana = pygame.Rect(13, 27, 152,15)	
			pygame.draw.rect(screen, (255,255,255), borda)
			pygame.draw.rect(screen, wizards[i].color_of_life, barralife)
			pygame.draw.rect(screen, (255,255,255), bordamana)
			pygame.draw.rect(screen, wizards[i].color_of_mana, barramana)
			screen.blit(textlife, (177,10))
			screen.blit(textmana, (177,27))
			screen.blit(textpoints, (657,10))
			screen.blit(texttime, (587,10))
			screen.blit(images["health"], (13, 8))
			screen.blit(images["mana"], (10, 23))
			
			# End of Life bar
			arc = pygame.Rect(760, 60, 30,30)
			if tempo <25:
				pygame.draw.arc(screen, (255,255,255), arc, 0, 6.28/timeattack1*tempo, 10)
			else:
				pygame.draw.arc(screen, (255,255,255), arc, 0, 6.28*2, 10)
			if tempo>=25:
				textready = font_small.render("Ready!", True, (255,255,255)) 
				textRectready = 757,93
				screen.blit(textready, textRectready)
	
		
		# Blit a new image of mouse		
		xmouse,ymouse = pygame.mouse.get_pos()
		if attack!=2:
			screen.blit(images["twig"], (xmouse,ymouse))
		else:
			screen.blit(images["area"], (xmouse-130,ymouse-68))

		
	pottime+=1
	tempo+=1

			

