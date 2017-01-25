import os, sys, pygame
from pygame.locals import *


import Variables
import typen

class Game():
    def __init__(self):
        self.running = True
        self.screen = None
        self.image = None

        # Stating the size of the screen
        self.width = 1920
        self.height = 1080
        size = (self.width, self.height)

        # Start Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(size, FULLSCREEN)

        # Setting the name of the window
        pygame.display.set_caption('Euromast')

        # Setting up buttons in main menu
        button_width = 64*6
        button_height = 16*6
        buttonsize = (int(button_width), int(button_height))

        # Creating all the buttons
        self.Menu_button0 = Button((self.width*0.8-(button_width/2)), (self.height*0.30), os.path.join("Images", "Play_Button_Normal.png"), os.path.join("Images", "Play_Button_Pressed.png"), buttonsize, "Play", True)
        self.Menu_button1 = Button((self.width*0.8-(button_width/2)), (self.height*0.45), os.path.join("Images", "Uitleg_Button_Normal.png"), os.path.join("Images", "Uitleg_Button_Pressed.png"), buttonsize, "Visible", True)
        self.Menu_button2 = Button((self.width*0.8-(button_width/2)), (self.height*0.60), os.path.join("Images", "Exit_Button_Normal.png"), os.path.join("Images", "Exit_Button_Pressed.png"), buttonsize, "Exit", True)
        self.Menu_button3 = Button((self.width*0.5-(button_width/2)), (self.height*0.70), os.path.join("Images", "Back_Button_Normal.png"), os.path.join("Images", "Back_Button_Pressed.png"), buttonsize, "VisibleExit", False)

        # Setting up various visual elements and text elements
        self.Rules = Image(0, 0, False, "Images", "Rules.png", 1920, 1080, 1)
        self.Background = Image(0, 0, True, "Images", "Menu_Background.png", 320, 180, 6)
        self.Title = Image((self.width*0.8-300), (self.height*0.01), True, "Images", "Title.png",100, 50, 6)

    def draw(self):
        # Setting the framerate
        clock = pygame.time.Clock()
        clock.tick(60)

        # Fill the screen
        self.Background.draw()

        # Set the menu text on top
        self.Title.draw()

        # Add image of a button
        self.Menu_button0.draw(self.screen)
        self.Menu_button1.draw(self.screen)
        self.Menu_button2.draw(self.screen)
        self.Menu_button3.draw(self.screen)

        # Add text of information
        self.Rules.draw()

        # Flip the screen
        pygame.display.flip()

    def update(self):
        # Scene switching for the information
        if Variables.function == "Menu_info":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Background.draw()
            self.Rules.update()
            self.Menu_button3.update()
            self.Title.update()

        # Scene switching to the playing menu
        if Variables.function == "Play":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Title.update()
            typen.start()

        # Scene switching to go back to the main menu from the playing menu
        if Variables.function == "Menu_return":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Title.update()
            Variables.function = "Menu_info"

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
            self.draw()

class Image:
    def __init__(self, x, y, check, path, image, width, height, scale):
        self._visible = check
        self.path = path
        self.image = image
        self.width = width
        self.height = height
        self.size = (int(width*scale), int(height*scale))
        self._rect = pygame.Rect(x, y, 0, 0)
        self.output2 = pygame.Surface(self._rect.size)

    def draw(self):
        if self._visible:
            self.output = pygame.image.load(os.path.join(self.path, self.image))
            self.output2 = pygame.transform.scale(self.output, self.size)
            self._rect = pygame.Rect((self._rect.left, self._rect.top, self.output2.get_width(), self.output2.get_height()))
            Variables.game.screen.blit(self.output2, self._rect)

    def update(self):
        self._visible = not self._visible

class Text:
    def __init__(self, check, text, color, width, height):
        self._visible = check
        self.font_menu = pygame.font.SysFont("consolas", 48)
        self.text = text
        self.color = color
        self.width = width
        self.height = height

    def draw(self):
        if self._visible:
            score_text = self.font_menu.render(self.text, 1, self.color)
            score_text_rect = score_text.get_rect(center=(self.width, self.height))
            Variables.game.screen.blit(score_text, score_text_rect)

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

    def draw(self, surfaceObj):
        if self._visible:
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
                Variables.function = "Menu_info"
                self._propSetVisible()

            elif self.buttonDown and self.type == "Play":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.function = "Play"
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
