# -*- coding: utf-8 -*-
"""

Developing by
João Pedro Ferreira de Melo Leôncio
Hugo Nicodemos Brito

"""

import sys, pygame, random, os, urllib

# TESTE DE REDE
import select





import socket

HOST = 'joopeed.no-ip.org'
PORT = 15000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.setblocking(0)

# TESTE DE REDE



pygame.init()

size = wid, hei = 800, 600
back = 30, 150, 30
 
screen = pygame.display
screen.set_caption("WizardPy")
screen = screen.set_mode(size)


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
images["back2"] = pygame.image.load("images/back2.jpg").convert_alpha()
images["firepower1"] = pygame.image.load("images/firepower1.png").convert_alpha()
images["firepower2"] = pygame.image.load("images/firepower2.png").convert_alpha()
images["firepower3"] = pygame.image.load("images/firepower3.png").convert_alpha()
images["twig"] = pygame.image.load("images/twig.png").convert_alpha()
images["health"] = pygame.image.load("images/health.png").convert_alpha()
images["mana"] = pygame.image.load("images/mana.png").convert_alpha()
images["pot"] = pygame.image.load("images/potiongrande.png").convert_alpha()
images["circ"] = pygame.image.load("images/circ.png").convert_alpha()
images["janelinha"] = pygame.image.load("images/janelinha.png").convert_alpha()
#images["fototwitter"] = pygame.image.load("foto.jpg").convert_alpha()
# End of buffer image


# Information of powers
info = {}	
info["mensagempadrao"] = u'Hover the mouse on\nthe power to show\nmore information\n'
info["firepower1"] = u"Press 1 to choose this:\nLaunch fire balls\n(Cooldown)\n(Doesn't need mana)\n"
info["firepower2"] = u'Press 2 to choose this:\nZone Attack\nExplosion (Needs mana)\n'
info["firepower3"] = u'Press 3 to choose this:\nFire Wall\nwhile you walk (Needs mana)\n'
info["pot"] = u'The Great Pot:\nUse this item and\nrecover your\n fully health\n'
# End Information of powers
rect_powers = {}


# Names of Wizards
Wizard_colors = {"Myrkur":"black","    Vel":"white","  Kalt":"blue","  Eldur":"red" }

#pygame.display.set_icon(images["redWizardD"].convert())

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
			if direction == "right":	
				if quanto!=0  and verifynotcollision("right", monster, things)[0]:
					monster.moveright(vermei)
					anda_dragons[direction]-=1
					break
			if direction == "up":	
				if quanto!=0  and verifynotcollision("up", monster, things)[0]:
					monster.moveup(vermei)
					anda_dragons[direction]-=1
					break
			if direction == "down":	
				if quanto!=0  and verifynotcollision("down", monster, things)[0]:
					monster.movedown(vermei)
					anda_dragons[direction]-=1
					break

def powers(color, kind, Wizard, destination):
	if color=="red":
		if kind ==1:
			Wizard.primary_attack(destination)
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
	

"""
First, create the object here.
After, the object to list of things and to group of objects inside while.
"""

anda_back=0
anda_Gate=0
tempo = 0
attack = 1 #Default is 1
pontos=0
pottime=0


### Declaration of objects ###
## PS. All objects are declared with top-left coordinates...
wizards = []
wizards.append(Wizard("  Eldur", Wizard_colors["  Eldur"],(300,300), screen, True))
wizards.append(Wizard("  Kalt", Wizard_colors["  Kalt"],(400,400), screen, True))
# Dragons
dragons = Set()
dragons.add(Dragon((100,-200), screen))
dragons.add(Dragon((200,450), screen))
dragons.add(Dragon((400,-450), screen))

# Sequence of movimentation
anda_dragon = {"right":150,"down":150,"left":150,"up":150}
# Bushs
list_Bushs = Set()
insertlineBushs(-300, list_Bushs)
burneds = Set()
# Items
list_items = Set()
list_items.add(Item((400,400), "potion2", screen))
list_items.add(Item((400,-400), "potion2", screen))
# Walls
list_walls = Set()
list_walls.add(Wall((-40,199), "parede1", screen))
list_walls.add(Wall((500,201), "parede1", screen))
list_walls.add(Wall((500,7), "parede2", screen))
list_walls.add(Wall((500,-50), "parede2", screen))
list_walls.add(Wall((-40,0), "parede1", screen))
# Trees
list_trees = []
insertjungle( -80,200, list_trees)
insertjungle( 500,350, list_trees)
insertjungle( 50,120, list_trees)
insertjungle( 500,-350, list_trees)
insertjungle( -80,-220, list_trees)
insertjungle( 0,-500, list_trees)
# Gates
list_gates = Set()
list_gates.add(Gate((367,200), "porta1", screen))
# Buttons
list_buttons = Set()
list_buttons.add(Button((600,330), "botao", screen))
list_buttons.add(Button((600,180), "botao", screen))

zera =  pygame.time.get_ticks()
inicio = pygame.time.get_ticks()


num = raw_input()

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

	for dragon in dragons:
		if dragon.isdead():
			dragons-=Set([dragon])
			pontos+=200/(pygame.time.get_ticks()/20000. -(zera/20000.))
			zera = pygame.time.get_ticks()
			break
	# Remove the burneds Bushs and the dead dragons of the lists
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()



	
	""" Grid of possible things to the Wizard collide """
	things = []
	addtolist( [list_trees, list_Bushs, list_walls, list_gates, dragons ], things )
	"""Grid of things, unicluding the dragons, because it doesnt collide theirselves"""	
	things2 = []
	addtolist( [list_trees, list_Bushs, list_walls, list_items, list_gates, wizards], things2 )	
	""" Grid of possible things to organize """
	group_objects = []
	addtolist( [list_trees, list_Bushs, list_walls, list_gates, list_items, dragons, projectiles, wizards ], group_objects )
	""" Grid of possible things living """
	vivos = []
	addtolist( [dragons, wizards], vivos )

	

	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		#arquivo=open("/home/joopeed/Dropbox/Public/pontos.html",'a')
		#arquivo.write("%4i points com "%pontos+vermei.name+"</br>" )
		#arquivo.close()
		sys.exit()
	for i in [int(num)]:
		# If the Wizard pass on the item he gets it
		for item in list_items:
			if wizards[i].chao.colliderect(item.chao):
				wizards[i].items["pot"]+=1
				list_items-=Set([item])
				break
	
	
		# Move the Wizard before the screen, if thats possible
		if pygame.key.get_pressed()[pygame.K_a] and wizards[i].x > 7 and verifynotcollision("left",wizards[i], things)[0]:
			s.sendall(num+" L")
			#wizards[i].moveleft()
		if pygame.key.get_pressed()[pygame.K_d] and wizards[i].x < wid-45 and verifynotcollision("right",wizards[i], things)[0]: 
			s.sendall(num+" R")			
			#wizards[i].moveright()
	
	
		if pygame.key.get_pressed()[pygame.K_s] and wizards[i].y < hei-128 and verifynotcollision("down",wizards[i], things)[0]:
			s.sendall(num+" D")
			#wizards[i].movedown()
			
				
	
		if pygame.key.get_pressed()[pygame.K_w] and wizards[i].y > 12 and verifynotcollision("up",wizards[i], things)[0]: 
			s.sendall(num+" U")
			#wizards[i].moveup()	
			
		
		
		
	
		for dragon in dragons:
			movemonsters( anda_dragon, dragon, things2, wizards[i] )
			if sum(anda_dragon.values())==0:
				anda_dragon = {"right":150,"down":150,"left":150,"up":150}
	
		# if the Wizard is on the button, the gate opens
		ok=0
		for button in list_buttons:
			if button.chao.colliderect(wizards[i].chao) or pygame.key.get_pressed()[pygame.K_RIGHT]:
				ok+=1
		for gate in list_gates:
			#print button.chao.colliderect(wizards[i].chao) or pygame.key.get_pressed()[pygame.K_RIGHT]	
 			if ok>0:
				if gate.x<=500:		
					gate.x+=1
			elif not gate.chaoleft.colliderect(wizards[i].chao): # Verify the collision when the gate is closing
					if gate.x>=370:
						gate.x-=1
		
		
	
		if pygame.key.get_pressed()[pygame.K_LSHIFT] and pygame.key.get_pressed()[pygame.K_SPACE]:
			wizards[i].lower(1)
		if pygame.key.get_pressed()[pygame.K_LSHIFT] and pygame.key.get_pressed()[pygame.K_z]:
			wizards[i].upper(5)
	
	
	
	
		# Change the attack for mouse
		if pygame.key.get_pressed()[pygame.K_1]:
			attack = 1
		timeattack1= 50
		if pygame.mouse.get_pressed()[0] and tempo>timeattack1:
			powers(wizards[i].color, attack, wizards[i], pygame.mouse.get_pos())
			tempo = 0
		


		if wizards[i].isdead():
			# When the Wizard is dead, show a message on screen
			text_death = font_death.render(u'Oh! '+wizards[i].name+', The '+wizards[i].color.capitalize()+
			' Wizard morreu nas suas mãos!'.decode("utf8"), True,(255,255, 255))
			textRect_death = text_death.get_rect()
			textRect_death.centerx = screen.get_rect().centerx
			textRect_death.centery = screen.get_rect().centery
			screen.blit(text_death, textRect_death)
		else: 
			# Objects and their several floor/chãos
			
			
			"""Remove the exploded projectiles"""		
			projectilesexplodeds = Set()
			for projectile in projectiles:
				if projectile.exploded:
					projectilesexplodeds = projectilesexplodeds | Set([projectile])
			projectiles -= projectilesexplodeds
			"""Enf of Remove"""
	
			for button in list_buttons:
				button.update()
			# Blit on screen organized objects :D
				#Objects have life
	
			organize(group_objects, things, vivos)
			
			# MENU of Items
			# Press I to show the menu	
			if pygame.key.get_pressed()[pygame.K_i]:
				screen.blit(images["janela"], (50,10))
				text_titulo = font_big.render(u'Your items'.decode("utf8"), True,(255,255, 255))
				screen.blit(text_titulo, (130,80))
				if wizards[i].items["pot"]>0:
					screen.blit(images["pot"], (100,110))
					screen.blit(images["circ"], (190,230))
					text_titulo = font_medium.render(str(wizards[i].items["pot"]), True,(0,0, 0))
					screen.blit(text_titulo, (200,237))
					if pygame.Rect(150,180,70,80).collidepoint(pygame.mouse.get_pos()):
						if pygame.mouse.get_pressed()[0] and pottime>10:
							wizards[i].items["pot"]-=1
							wizards[i].upper(100)
							pottime =0
							
						else:
							screen.blit(images["janelinha"], (190,190))
							blitainfos( screen, info["pot"] , (210,200) )
			# End of MENU of Items
			
			# MENU of Powers
			# Press P to show the menu
	
			elif pygame.key.get_pressed()[pygame.K_p]:
			#else: #Uncomment and comment the other to fix
				screen.blit(images["janela2"], (-200,437))
				text_titulo = font_medium.render(u'Your powers'.decode("utf8"), True,(255,255, 255))
				screen.blit(text_titulo, (20,497))
				screen.blit(images["firepower1"], (35,523))
				screen.blit(images["firepower2"], (105,523))
				screen.blit(images["firepower3"], (175,523))
				rect_powers["firepower1"] = pygame.Rect(35,523,63,63)
				rect_powers["firepower2"] = pygame.Rect(105,523,63,63)
				rect_powers["firepower3"] = pygame.Rect(175,523,63,63)
				if rect_powers["firepower1"].collidepoint(pygame.mouse.get_pos()):
					blitainfos( screen, info["firepower1"] , (265,523) )
				elif rect_powers["firepower2"].collidepoint(pygame.mouse.get_pos()):
					blitainfos( screen, info["firepower2"] , (265,523) )
				elif rect_powers["firepower3"].collidepoint(pygame.mouse.get_pos()):
					blitainfos( screen, info["firepower3"] , (265,523) )
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
		screen.blit(images["twig"], (xmouse-8,ymouse-8))
		
	""" GETS DATAS FROM INTERNET """
	ready = select.select([s], [], [], 0)
	data = ""
	numo =3
	if ready[0]:
    		data = s.recv(1024)
		try: 
			numo, data = data.split()
			numo = int(numo)
		except: pass
		othermago = [0,1]
		othermago.remove(int(num))
		othermago = othermago[0]
		if numo==int(num):
			if data=="L":
				wizards[numo].moveleft()
			elif data=="R":
				wizards[numo].moveright()
			elif data=="D":
				wizards[numo].movedown()
				upthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])		
				for dragon in dragons:		
					if not dragon.isdead():			
						dragon.moveup(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back+=1
				wizards[othermago].y-=1
			elif data=="U":
				wizards[numo].moveup()
				downthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])
				for dragon in dragons:
					if not dragon.isdead():			
						dragon.movedown(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back-=1
				wizards[othermago].y+=1
			elif data=="RD":
				wizards[numo].moveright()
				wizards[numo].movedown()
				upthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])		
				for dragon in dragons:		
					if not dragon.isdead():			
						dragon.moveup(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back+=1
				wizards[othermago].y-=1
			elif data=="LD":
				wizards[numo].moveleft()
				wizards[numo].movedown()
				upthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])		
				for dragon in dragons:		
					if not dragon.isdead():			
						dragon.moveup(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back+=1
				wizards[othermago].y-=1
			elif data=="RU":
				wizards[numo].moveright()
				wizards[numo].moveup()
				downthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])
				for dragon in dragons:
					if not dragon.isdead():			
						dragon.movedown(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back-=1
				wizards[othermago].y+=1
			elif data=="LU":
				wizards[numo].moveleft()
				wizards[numo].moveup()
				downthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])
				for dragon in dragons:
					if not dragon.isdead():			
						dragon.movedown(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back-=1
				wizards[othermago].y+=1
			elif data=="DR":
				wizards[numo].moveright()
				wizards[numo].movedown()
				upthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])		
				for dragon in dragons:		
					if not dragon.isdead():			
						dragon.moveup(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back+=1
				wizards[othermago].y-=1
			elif data=="DL":
				wizards[numo].moveleft()
				wizards[numo].movedown()
				upthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])		
				for dragon in dragons:		
					if not dragon.isdead():			
						dragon.moveup(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back+=1
				wizards[othermago].y-=1
			elif data=="UR":
				wizards[numo].moveright()
				wizards[numo].moveup()
				downthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])
				for dragon in dragons:
					if not dragon.isdead():			
						dragon.movedown(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back-=1
				wizards[othermago].y+=1
			elif data=="UL":	
				wizards[numo].moveleft()
				wizards[numo].moveup()
				downthings([list_Bushs,list_walls,list_items,list_trees,list_gates,list_buttons, projectiles])
				for dragon in dragons:
					if not dragon.isdead():			
						dragon.movedown(wizards[numo])
					else:
						dragon = Dragon((-1000,-150), screen)
				anda_back-=1
				wizards[othermago].y+=1
		elif numo==othermago:
			if data=="L":
				wizards[othermago].moveleft()
			elif data=="R":
				wizards[othermago].moveright()
			elif data=="D":
				wizards[othermago].y+=1
				wizards[othermago].movedown()
			elif data=="U":
				wizards[othermago].y-=1
				wizards[othermago].moveup()
			elif data=="RD":
				wizards[othermago].moveright()
				wizards[othermago].y+=1
				wizards[othermago].movedown()
			elif data=="LD":
				wizards[othermago].moveleft()
				wizards[othermago].y+=1
				wizards[othermago].movedown()
			elif data=="RU":
				wizards[othermago].moveright()
				wizards[othermago].y-=1
				wizards[othermago].moveup()
			elif data=="LU":
				wizards[othermago].moveleft()
				wizards[othermago].y-=1
				wizards[othermago].moveup()
			elif data=="DR":
				wizards[othermago].moveright()
				wizards[othermago].y+=1
				wizards[othermago].movedown()
			elif data=="DL":
				wizards[othermago].moveleft()
				wizards[othermago].y+=1
				wizards[othermago].movedown()
			elif data=="UR":
				wizards[othermago].moveright()
				wizards[othermago].y-=1
				wizards[othermago].moveup()
			elif data=="UL":	
				wizards[othermago].moveleft()
				wizards[othermago].y-=1
				wizards[othermago].moveup()
	
	data = ""
	pottime+=1
	tempo+=1	
			

