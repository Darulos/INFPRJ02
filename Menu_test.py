import os, sys, pygame, math
from pygame.locals import *

class Game:
    def __init__(self):
        width = 480
        height = 640
        size = (width, height)

        # Start PyGame
        pygame.init()

        # Set the resolution
        self.screen = pygame.display.set_mode(size)

        # Set the name of the window
        pygame.display.set_caption('Euromast')

        # Set up the default font
        self.font_menu = pygame.font.Font(None, 48)

        # Set up a button
        self.button = Button.load("Button_unpressed.png")
        self.button.pos = (width*0.3, height*0.3)

        # # Create an enemy
        # self.enemy = Enemy(width * 0.8, height * 0.5, width * 0.1)
        #
        # # Create the player
        # self.player = Player(width * 0.2, height * 0.5, width * 0.1)

    # Update game logic
    def update(self):
        # Update entities
        self.button.update()
    #     self.player.update()
    #     self.enemy.update(self.player)

    # Draw everything
    def draw(self):
        width = 480
        height = 640
        clock = pygame.time.Clock()
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Draw the entities
        self.button.draw(self.screen)
        # self.enemy.draw(self.screen)
        # self.player.draw(self.screen)
        self.screen.blit(self.button, (0,0))

        # Draw the score text
        score_text = self.font_menu.render("Menu", 1, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(width/2, height*0.10))
        self.screen.blit(score_text, score_text_rect)

        # Flip the screen
        pygame.display.flip()
        clock.tick(60)

    # The game loop
    def game_loop(self):
        while not process_events():
            # self.update()
            self.draw()


# class Player:
#     def __init__(self, x, y, r):
#         self.x = x
#         self.y = y
#         self.r = r
#
#     def update(self):
#         keys = pygame.key.get_pressed()
#
#         if keys[pygame.K_LEFT]:
#             self.x -= 1
#         elif keys[pygame.K_RIGHT]:
#             self.x += 1
#
#         if keys[pygame.K_UP]:
#             self.y -= 1
#         elif keys[pygame.K_DOWN]:
#             self.y += 1
#
#     def draw(self, screen):
#         pygame.draw.circle(screen, (0, 255, 0),
#                            (int(self.x), int(self.y)), int(self.r))
#
#
# class Enemy:
#     def __init__(self, x, y, r):
#         self.x = x
#         self.y = y
#         self.r = r
#         self.health = 255
#
#     def update(self, player):
#         # If this enemy is colliding with the player
#         if math.sqrt((player.x - self.x) ** 2 +
#                      (player.y - self.y) ** 2) < self.r + player.r:
#             self.health -= 1
#             if self.health == 0:
#                 self.health = 255
#
#     def draw(self, screen):
#         pygame.draw.circle(screen, (self.health, 0, 0),
#                            (int(self.x), int(self.y)), int(self.r))

class Button:
    def __init__(self, x, y):
        self.pos = (x,y)
        self.img = None

    def update(self):
        mouse = pygame.mouse.get_pressed()

    def load(self, filename):
        try:
            self.img = pygame.image.load(filename).convert()
        except:
            print('An error has occurred while the game was loading the image [%s]' % (filename))
            input('Press [ENTER] to exit')
            exit(0)
    def draw(self, screen):
        try:
            screen.blit(self.img, self.pos)
            pygame.display.flip()
        except:
            print('An error has occurred while the game was rendering the image.')
            input('Press [ENTER] to exit')
            exit(0)

# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False


# Main program logic
def program():
    game = Game()
    game.game_loop()


# Start the program
program()
