#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


mesosPossibles = ["Gen", "Jan", "Feb", "Ene","Mar", "May", "Mai", "Jun", "Jul", "Aug", "Ago", "Set", "Sep", "Oct", "Nov", "Des", "Dic", "Abr", "Apr"] 
fileHandler = open ("/home/milax/dates.txt")
fileHandler.readline()

for line in fileHandler.readlines():
	print (line)

	#Eliminar espais repetits
	newline = ""
	first = True
	for i in range (len(line)):
		actualchar = line[len(line) -1 ]
		if actualchar.__eq__(" "):
			if first:
				newline = actualchar + newline 
				first = False
			else :
				pass
		else:
			newline = actualchar + newline
			first = True
		if len(line)-1>0:
			line = line[ 0:len(line)-1]
			print (line)
	#Elimina espais repetits
	print ("newline: " + newline)
	camps = newline.split(" ")
	mes = camps[0]
	dia = int(camps[1])
	temps = camps[2]
	tempsCamps = temps.split(":")
	hores = int(tempsCamps[0])
	minuts = int(tempsCamps[1])
	segons = int(tempsCamps[2])
	if mes not in mesosPossibles:
		print ("Mes incorrecte")
		continue
	if dia<1 | dia>31 :
		print ("Dia incorrecte")
		continue
	
	if hores<0 | hores>23:
		print ("Hora incorrecte")
		continue
	if minuts<0 | minuts>59:
		print ("Minuts incorrectes")
		continue
	if segons<0 | segons>59:
		print ("Segons incorrectes")
		continue



	

	
	

			

		


	
