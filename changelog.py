# -*- coding: utf-8 -*-

# Modificador Changelog

from datetime import datetime
import sys, locale

locale.setlocale(locale.LC_ALL, '')

while True:
	log = raw_input("Digite a modificacao ou nada para fechar o programa: ")
	
	if log == "": break
	
	f = open('changelog.txt', 'a')

	hoje = datetime.today()
	
	f.write(hoje.strftime("%A").capitalize()[:3]+ ", " + str(hoje) + "\n" + log + "\n")

	f.close()


sys.exit()
