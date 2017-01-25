import pygame
import random
import Variables

def draw():

    Dice1 = pygame.image.load('Dice_1.png')
    Dice2 = pygame.image.load('Dice_2.png')
    Dice3 = pygame.image.load('Dice_3.png')
    Dice4 = pygame.image.load('Dice_4.png')
    Dice5 = pygame.image.load('Dice_5.png')
    Dice6 = pygame.image.load('Dice_6.png')

    number = random.randint(1, 6)

    if number == 1:
        Variables.game.screen.blit(Dice1, (200, 200))
    if number == 2:
        Variables.game.screen.blit(Dice2, (200, 200))
    if number == 3:
        Variables.game.screen.blit(Dice3, (200, 200))
    if number == 4:
        Variables.game.screen.blit(Dice4, (200, 200))
    if number == 5:
        Variables.game.screen.blit(Dice5, (200, 200))
    if number == 6:
        Variables.game.screen.blit(Dice6, (200, 200))
