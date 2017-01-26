import pygame
import random
import Variables
import os

def draw():

    #Setting up textures for the dice
    Dice1 = pygame.image.load(os.path.join('Images', 'Dice1.png'))
    Dice2 = pygame.image.load(os.path.join('Images', 'Dice2.png'))
    Dice3 = pygame.image.load(os.path.join('Images', 'Dice3.png'))
    Dice4 = pygame.image.load(os.path.join('Images', 'Dice4.png'))
    Dice5 = pygame.image.load(os.path.join('Images', 'Dice5.png'))
    Dice6 = pygame.image.load(os.path.join('Images', 'Dice6.png'))

    #Creating random number for diceroll
    Variables.number = random.randint(1, 6)

    #Linking diceroll result to dice texture
    if Variables.number == 1:
        Variables.game.screen.blit(Dice1, (500,500))
    if Variables.number == 2:
        Variables.game.screen.blit(Dice2, (500,500))
    if Variables.number == 3:
        Variables.game.screen.blit(Dice3, (500,500))
    if Variables.number == 4:
        Variables.game.screen.blit(Dice4, (500,500))
    if Variables.number == 5:
        Variables.game.screen.blit(Dice5, (500,500))
    if Variables.number == 6:
        Variables.game.screen.blit(Dice6, (500,500))
