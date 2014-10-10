#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

# 1. initialisation du tableau
# 	=> RANDOM
# 	=> formes définies
# 2. Boucle de calcul de grille 
# 	=> confrontation de chaque case avec les règles
#	=> établissement de la grille n+1

# 0: case vide / morte
# 1: case vivante

NB_OCCURENCES = 100
CLOSE_ENVIRONMENT_SIZE = 3 # >= 3

def getEmptyGrill(dimension):
	return [[0 for x in xrange(dimension)] for x in xrange(dimension)]

def printGrill(grill):
	for i in range(len(grill[0])):
		print grill[i]

def randomInitialisation(grill):
	for i in range(len(grill)):
		for j in range(len(grill)):
			grill[i][j] = randint(0,1)
	return grill

# en fonction des coordonées de la cellule, on va pouvoir en donner l'environnement proche
# le tableau est considéré comme un tableau de snake: les bords du hauts sont adjacents à 
# ceux du bas, de meme pour droite/gauche
def getCellCloseEnvironment(i,j,world):
	#if CLOSE_ENVIRONMENT_SIZE < 3: CLOSE_ENVIRONMENT_SIZE = 3

	environment = getEmptyGrill(CLOSE_ENVIRONMENT_SIZE)

	for x in range(CLOSE_ENVIRONMENT_SIZE):
		i = x - int(CLOSE_ENVIRONMENT_SIZE/2)
		for y in range(CLOSE_ENVIRONMENT_SIZE):
			j = y - int(CLOSE_ENVIRONMENT_SIZE/2)
			environment[x][y] = world[i][j]

	return environment

# l'environnement représente la grille d'étude autour de la cellule analysée
def liveDieRebornDecision(environment): 
	print "coucou"

def processNewGeneration(oldGrill):
	for i in range(len(oldGrill)):
		for j in range(oldGrill):
			print "coucou"

def main():
	global NB_OCCURENCES
	global CLOSE_ENVIRONMENT_SIZE

	grill = getEmptyGrill(50) 
	randomInitialisation(grill)
	#print "grill: " +str(grill)
	printGrill(grill)
	#for i in range(NB_OCCURENCES):
	#	processNewGeneration(grill)

	closeGrill = getCellCloseEnvironment(0,0,grill)
	printGrill(closeGrill)


if __name__ == "__main__":
    main()