#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import time

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
		i = i- x - int(CLOSE_ENVIRONMENT_SIZE/2)
		for y in range(CLOSE_ENVIRONMENT_SIZE):
			j = j - y - int(CLOSE_ENVIRONMENT_SIZE/2)
			environment[x][y] = world[i][j]

	return environment

# l'environnement représente la grille d'étude autour de la cellule analysée
# 	state: état de la cellule analysée
# 	neighborCounter: nb de voisins, obtenu avec la fonction neighborCounter()
def liveDieRebornDecision(state, nbNeighbor): 
	newState = 0
	if state == 0 and nbNeighbor == 3:
		newState = 1
	elif state == 1 and (nbNeighbor == 2 or nbNeighbor == 3): 
		newState = 1

	return newState

# def processNewGeneration(oldGrill):
# 	for i in range(len(oldGrill)):
# 		for j in range(oldGrill):
# 			print "coucou"

def neighborCounter(closeEnvironment):
	# la cellule analysée est au milieu de la cellule
	index = int(len(closeEnvironment[1])/2)
	counter = 0

	for i in range(len(closeEnvironment)):
		for j in range(len(closeEnvironment)):
			if not(i == index and j == index):
				counter += closeEnvironment[i][j]

	return counter



def main():
	global NB_OCCURENCES
	global CLOSE_ENVIRONMENT_SIZE

	world = getEmptyGrill(20)
	newWorld = getEmptyGrill(20)

	randomInitialisation(world)
	printGrill(world)

	for index in range(5):
		for i in range(len(world)):
			for j in range(len(world)):
				closeEnvironment = getCellCloseEnvironment(i,j,world)
				nbNeighbor = neighborCounter(closeEnvironment)
				newState = liveDieRebornDecision(world[i][j], nbNeighbor)
				newWorld[i][j] = newState
		world = newWorld
		newWorld = getEmptyGrill(20)

		print "\n****************************************\n"
		printGrill(world)

if __name__ == "__main__":
    main()