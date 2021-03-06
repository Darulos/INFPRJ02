# Copyright 'We gaan voor een 10', 2017

import os, sys, pygame
from pygame.locals import *

import Input
import Variables
import Database
import Sounds


class Game:
    def __init__(self):
        self.running = True
        self.screen = None
        self.image = None

        # Start Pygame
        pygame.init()

        # Stating the size of the screen
        screenInfo = pygame.display.Info()
        self.width = screenInfo.current_w
        self.height = screenInfo.current_h
        size = (self.width, self.height)
        self.screen = pygame.display.set_mode(size, FULLSCREEN)

        # Setting the highscore menu
        hiscores = ""
        self.Score0 = Text(False, hiscores, (0, 0, 0), 960, 200)
        for i in range(0, 10):
            hiscores += str(Database.interact_database("SELECT Name FROM Score ORDER BY (Wins / (Losses + 1)) DESC LIMIT 1 OFFSET {};".format(i))[0][0])
            hiscores += "  Wins: "
            hiscores += str(Database.interact_database("SELECT Wins FROM Score ORDER BY (Wins / (Losses + 1)) DESC LIMIT 1 OFFSET {};".format(i))[0][0])
            hiscores += "  Losses: "
            hiscores += str(Database.interact_database("SELECT Losses FROM Score ORDER BY (Wins / (Losses + 1)) DESC LIMIT 1 OFFSET {};".format(i))[0][0])
            hiscores += "  W/L: "
            if 1 > int(Database.interact_database("SELECT Losses FROM Score ORDER BY (Wins / (Losses + 1)) DESC LIMIT 1 OFFSET {};".format(i))[0][0]):
                hiscores += str(int(Database.interact_database("SELECT Wins FROM Score ORDER BY (Wins / (Losses + 1)) DESC LIMIT 1 OFFSET {};".format(i))[0][0]))
            else:
                print("XD")
                hiscores += str(round(int(Database.interact_database("SELECT Wins FROM Score ORDER BY (Wins / (Losses + 1)) DESC LIMIT 1 OFFSET {};".format(i))[0][0]) / int(Database.interact_database("SELECT Losses FROM Score ORDER BY (Wins / (Losses + 1)) DESC LIMIT 1 OFFSET {};".format(i))[0][0]), 2))
            if i == 0:
                self.Score0 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            elif i == 1:
                self.Score1 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            elif i == 2:
                self.Score2 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            elif i == 3:
                self.Score3 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            elif i == 4:
                self.Score4 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            elif i == 5:
                self.Score5 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            elif i == 6:
                self.Score6 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            elif i == 7:
                self.Score7 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            elif i == 8:
                self.Score8 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            elif i == 9:
                self.Score9 = Text(False, hiscores, (255, 255, 255), self.width/2, 200 + (50*i))
            hiscores = ""

        # Plays Title Music
        Sounds.PlaySound.TitleScreen(self)

        # Setting the name of the window
        pygame.display.set_caption('Euromast')

        # Setting up other scenes
        self.scene = Input.Play(self.screen)

        # Setting up buttons in main menu
        button_width = 64*6
        button_height = 16*6
        buttonsize = (int(button_width), int(button_height))

        # Creating all the buttons
        self.Menu_button0 = Button((self.width*0.8-(button_width/2)), (self.height*0.30), os.path.join("Images", "Play_Button_Normal.png"), os.path.join("Images", "Play_Button_Pressed.png"), buttonsize, "Play", True)
        self.Menu_button1 = Button((self.width*0.8-(button_width/2)), (self.height*0.45), os.path.join("Images", "Uitleg_Button_Normal.png"), os.path.join("Images", "Uitleg_Button_Pressed.png"), buttonsize, "Visible", True)
        self.Menu_button4 = Button((self.width*0.8-(button_width/2)), (self.height*0.60), os.path.join("Images", "Hiscores_Button_Normal.png"), os.path.join("Images", "Hiscores_Button_Pressed.png"), buttonsize, "Score", True)
        self.Menu_button2 = Button((self.width*0.8-(button_width/2)), (self.height*0.75), os.path.join("Images", "Exit_Button_Normal.png"), os.path.join("Images", "Exit_Button_Pressed.png"), buttonsize, "Exit", True)
        self.Menu_button3 = Button((self.width*0.5-(button_width/2)), (self.height*0.70), os.path.join("Images", "Back_Button_Normal.png"), os.path.join("Images", "Back_Button_Pressed.png"), buttonsize, "VisibleExit", False)
        self.Menu_button5 = Button((self.width*0.5-(button_width/2)), (self.height*0.70), os.path.join("Images", "Back_Button_Normal.png"), os.path.join("Images", "Back_Button_Pressed.png"), buttonsize, "VisibleSExit", False)

        # Setting up various visual elements and text elements
        self.Rules = Image(0, 0, False, "Images", "Rules.png", 1)
        self.Background = Image(0, 0, True, "Images", "Menu_Background.png", 6)
        self.Title_Animation = Animation((self.width * 0.8 - 300), (self.height * 0.01), "Images", "Title_Animated.png", 6, True, 10, 4, 1)
        self.Blank = Image(0, 0, False, "Images", "Blank.png", 1)

    def draw(self):
        # Setting the framerate
        clock = pygame.time.Clock()
        clock.tick(60)

        # Fill the screen
        self.Background.draw(self.screen)

        # Set the menu text on top
        self.Title_Animation.draw(self.screen)

        # Set the image behind highscores
        self.Blank.draw(self.screen)

        # Add text of information
        self.Rules.draw(self.screen)
        # Add text of scores
        self.Score0.draw(self.screen)
        self.Score1.draw(self.screen)
        self.Score2.draw(self.screen)
        self.Score3.draw(self.screen)
        self.Score4.draw(self.screen)
        self.Score5.draw(self.screen)
        self.Score6.draw(self.screen)
        self.Score7.draw(self.screen)
        self.Score8.draw(self.screen)
        self.Score9.draw(self.screen)

        # Add image of a button
        self.Menu_button0.draw(self.screen)
        self.Menu_button1.draw(self.screen)
        self.Menu_button2.draw(self.screen)
        self.Menu_button3.draw(self.screen)
        self.Menu_button4.draw(self.screen)
        self.Menu_button5.draw(self.screen)

        # Flip the screen
        pygame.display.flip()

    def update(self):
        # Scene switching for the information
        if Variables.function == "Menu_info":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Menu_button4.update()
            self.Rules.update()
            self.Menu_button3.update()
            self.Title_Animation.update()

        if Variables.function == "Menu_scores":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Menu_button4.update()
            self.Blank.update()
            self.Score0.update()
            self.Score1.update()
            self.Score2.update()
            self.Score3.update()
            self.Score4.update()
            self.Score5.update()
            self.Score6.update()
            self.Score7.update()
            self.Score8.update()
            self.Score9.update()
            self.Menu_button5.update()
            self.Title_Animation.update()

        # Scene switching to the playing menu
        if Variables.function == "Play":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Menu_button4.update()
            self.Title_Animation.update()
            self.Background.update()
            self.scene.start()
            self.Background.update()
            self.Title_Animation.update()
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Menu_button4.update()

        # Scene switching to go back to the main menu from the playing menu
        if Variables.function == "Menu_return":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Menu_button4.update()
            self.Title_Animation.update()
            Variables.function = "Menu_info"

        if Variables.function == "Menu_s_return":
            self.Blank.update()
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Menu_button4.update()
            self.Title_Animation.update()
            Variables.function = "Menu_scores"

    def game_loop(self):
        a = True
        while a:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Give the signal to quit
                    a = False
                self.Menu_button0.eventhandler(event)
                self.Menu_button1.eventhandler(event)
                self.Menu_button2.eventhandler(event)
                self.Menu_button3.eventhandler(event)
                self.Menu_button4.eventhandler(event)
                self.Menu_button5.eventhandler(event)
            self.draw()


class Image:
    def __init__(self, x, y, check, path, image, scale):
        self._visible = check
        self.path = path
        self.image = image
        self.width = 0
        self.height = 0
        self.size = (0,0)
        self.scale = scale
        self._rect = pygame.Rect(x, y, 0, 0)
        self.output2 = pygame.Surface(self._rect.size)

        # Setting the image
        self.output = pygame.image.load(os.path.join(self.path, self.image))
        self.width = self.output.get_width()
        self.height = self.output.get_height()
        self.size = (int(self.width*self.scale), int(self.height*self.scale))
        self.output2 = pygame.transform.scale(self.output, self.size)
        self._rect = pygame.Rect((self._rect.left, self._rect.top, self.output2.get_width(), self.output2.get_height()))

    def draw(self, screen):
        if self._visible:
            screen.blit(self.output2, self._rect)

    def update(self):
        self._visible = not self._visible


class Text:
    pygame.init()
    def __init__(self, check, text, color, width, height):
        self._visible = check
        self.font_menu = pygame.font.SysFont("consolas", 48)
        self.text = text
        self.color = color
        self.width = width
        self.height = height

        # Setting the text
        self.score_text = self.font_menu.render(self.text, 1, self.color)
        self.score_text_rect = self.score_text.get_rect(center=(self.width, self.height))

    def draw(self, screen):
        if self._visible:
            screen.blit(self.score_text, self.score_text_rect)

    def update(self):
        if Variables.init == 1:
            self._visible = not self._visible


class Animation:
    def __init__(self, x, y, path, image, scale, visible, framerate, horizontal, vertical):
        self.path = path
        self.image = image
        self.x = x
        self.y = y
        self.scale = scale
        self._visible = visible
        self._rect = pygame.Rect(x, y, 0, 0)
        self.cell_position = 0
        self.timed = 0
        self.cell_list = []
        self.rate = framerate
        self.horizontal = horizontal
        self.vertical = vertical

        # Loading image and scaling it
        self.mainsheet = pygame.image.load(os.path.join(self.path, self.image))
        self.size = (int(pygame.Surface.get_width(self.mainsheet)*self.scale), int(pygame.Surface.get_height(self.mainsheet)*self.scale))
        self.output = pygame.transform.scale(self.mainsheet, self.size)
        self._rect = pygame.Rect((self._rect.left, self._rect.top, self.output.get_width(), self.output.get_height()))

        # Setting the cell sizes for the animation
        self.sheet_size = (self.output.get_width(),self.output.get_height())
        self.horiz_cell = self.horizontal
        self.vert_cells = self.vertical
        self.cell_width = int(self.sheet_size[0] / self.horiz_cell)
        self.cell_height = int(self.sheet_size[1] / self.vert_cells)

    def draw(self, screen):
        if self._visible:
            # Loop of the animation
            for y in range (0, self.sheet_size[1], self.cell_height):
                for x in range (0, self.sheet_size[0], self.cell_width):
                    surface = pygame.Surface((self.cell_width, self.cell_height), SRCALPHA)
                    surface.blit(self.output, (0,0), (x, y, self.cell_width, self.cell_height))
                    self.cell_list.append(surface)

            # Set the timed divided value to adjust animation speed
            self.timed += 1
            if self.timed % self.rate == 0:
                if self.cell_position < len(self.cell_list) - 1:
                    self.cell_position += 1
                else:
                    self.cell_position = 0
                    #self.timed = 0

            # Blit the images to the screen
            screen.blit(self.cell_list[self.cell_position], (self.x, self.y))

    def update(self):
        if Variables.init == 1:
            self._visible = not self._visible


class Button(object):
    def __init__(self, x, y, normal, down, screensize, type, check, highlight=None):
        self.size = screensize
        self.type = type
        self._rect = pygame.Rect(x, y, 0, 0)

        # Tracks the state of the button
        self.buttonDown = False # Is the button currently pushed down?
        self.mouseOverButton = False # Is the mouse currently hovering over the button?
        self.lastMouseDownOverButton = False # Was the last mouse down event over the mouse button? (Used to track clicks.)
        self._visible = check # Is the button visible

        # Create the surfaces for a text button
        self.surfaceNormal = pygame.Surface(self._rect.size)
        self.surfaceDown = pygame.Surface(self._rect.size)
        self.surfaceHighlight = pygame.Surface(self._rect.size)
        self.update() # Draw the initial button images

        # Setting the surfaces of the buttons
        self.normal = normal
        self.down = down
        self.highlight = highlight

        # Error prevention
        if self.down is None:
            self.down = self.normal
        if self.highlight is None:
            self.highlight = self.normal

        # Setting the textures of the button
        self.origSurfaceNormal = pygame.image.load(self.normal)
        self.origSurfaceDown = pygame.image.load(self.down)
        self.origSurfaceHighlight = pygame.image.load(self.highlight)

        # Scale the buttons to the appropiate size
        self.surfaceNormal = pygame.transform.scale(self.origSurfaceNormal, self.size)
        self.surfaceDown = pygame.transform.scale(self.origSurfaceDown, self.size)
        self.surfaceHighlight = pygame.transform.scale(self.origSurfaceHighlight, self.size)
        self._rect = pygame.Rect((self._rect.left, self._rect.top, self.surfaceNormal.get_width(), self.surfaceNormal.get_height()))

    def draw(self, surfaceObj):
        if self._visible:
            # Blit the buttons to the surface
            if self.buttonDown:
                surfaceObj.blit(self.surfaceDown, self._rect)
            elif self.mouseOverButton:
                surfaceObj.blit(self.surfaceHighlight, self._rect)
            else:
                surfaceObj.blit(self.surfaceNormal, self._rect)

    def update(self):
        if Variables.init == 1:
            self._visible = not self._visible

    # Classes meant to be overridden
    def mouseClick(self, event):
        pass
    def mouseEnter(self, event):
        pass
    def mouseMove(self, event):
        pass
    def mouseExit(self, event):
        pass
    def mouseDown(self, event):
        pass
    def mouseUp(self, event):
        pass

    # Function to trigger update of buttons
    def _propSetVisible(self):
        Variables.init = 1
        Variables.game.update()

    def eventhandler(self, eventObj):
        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN) or not self._visible:
            # The button only cares bout mouse-related events (or no events, if it is invisible)
            return []

        retVal = []

        hasExited = False
        if not self.mouseOverButton and self._rect.collidepoint(eventObj.pos):
            # If mouse has entered the button:
            self.mouseOverButton = True
            self.mouseEnter(eventObj)
            retVal.append('enter')
        elif self.mouseOverButton and not self._rect.collidepoint(eventObj.pos):
            # If mouse has exited the button:
            self.mouseOverButton = False
            hasExited = True # Call mouseExit() later, since we want mouseMove() to be handled before mouseExit()

        if self._rect.collidepoint(eventObj.pos):
            # If mouse event happened over the button:
            if eventObj.type == MOUSEMOTION:
                self.mouseMove(eventObj)
                retVal.append('move')
            elif eventObj.type == MOUSEBUTTONDOWN:
                self.buttonDown = True
                self.lastMouseDownOverButton = True
                self.mouseDown(eventObj)
                retVal.append('down')
        else:
            if eventObj.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
                # If an up/down happens off the button, then the next up won't cause mouseClick()
                self.lastMouseDownOverButton = False

        # Mouse up is handled whether or not it was over the button
        doMouseClick = False
        if eventObj.type == MOUSEBUTTONUP:
            if self.lastMouseDownOverButton:
                doMouseClick = True
            self.lastMouseDownOverButton = False

            if self.buttonDown and self.type == "Exit":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                sys.exit()

            elif self.buttonDown and (self.type == "Visible" or self.type == "VisibleExit"):
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                #Plays Click sound upon releasing
                Sounds.PlaySound.MouseClick(self)
                Variables.function = "Menu_info"
                self._propSetVisible()

            elif self.buttonDown and self.type == "Play":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                #Plays Click sound upon releasing
                Sounds.PlaySound.MouseClick(self)
                Variables.function = "Play"
                self._propSetVisible()

            elif self.buttonDown and (self.type == "Score" or self.type == "VisibleSExit"):
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                #Plays Click sound upon releasing
                Sounds.PlaySound.MouseClick(self)
                Variables.function = "Menu_scores"
                self._propSetVisible()

            elif self.buttonDown:
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')

            if doMouseClick:
                self.buttonDown = False
                self.mouseClick(eventObj)
                retVal.append('click')

        if hasExited:
            self.mouseExit(eventObj)
            retVal.append('exit')

        return retVal


def program():
    Variables.game = Game()
    Variables.game.game_loop()

# Start the program
program()
