import os, sys, pygame
from pygame.locals import *


import Variables
import Spelregels
import typen

class Game():
    def __init__(self):
        self.running = True
        self.screen = None
        self.image = None

        # Stating the size of the screen
        self.width = 480
        self.height = 640
        size = (self.width, self.height)

        # Start Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(size)

        # Setting the name of the window
        pygame.display.set_caption('Euromast')

        # Setting up the menu text on top
        self.Menu_text = Text(True, "Menu",(255, 255, 255), self.width/2, self.height*0.10)

        # Setting up buttons in main menu
        buttonsize = (int(600/(self.width/150)), int(300/(self.height/150)))
        self.Menu_button0 = Button((self.width*0.5), (self.height*0.30), "Button_unpressed.png", "Button_pressed.png", buttonsize, "Play", True)
        self.Menu_button1 = Button((self.width*0.5), (self.height*0.45), "Button_unpressed.png", "Button_pressed.png", buttonsize, "Visible", True)
        self.Menu_button2 = Button((self.width*0.5), (self.height*0.60), "Button_unpressed.png", "Button_pressed.png", buttonsize, "Exit", True)
        self.Menu_button3 = Button((self.width*0.5), (self.height*0.85), "Button_unpressed.png", "Button_pressed.png", buttonsize, "VisibleExit", False)

        # Setting up the information regarding the game
        self.Text = Spelregels.Info()

    def draw(self):
        # Setting the framerate
        clock = pygame.time.Clock()
        clock.tick(60)

        # Fill the screen
        self.screen.fill((0, 0, 0))

        # Set the menu text on top
        self.Menu_text.draw()

        # Add image of a button
        self.Menu_button0.draw(self.screen)
        self.Menu_button1.draw(self.screen)
        self.Menu_button2.draw(self.screen)
        self.Menu_button3.draw(self.screen)

        # Add text of information
        self.Text.draw(self.screen)

        # Flip the screen
        pygame.display.flip()

    def update(self):
        if Variables.function == "Menu_info":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.switch()
            self.screen.fill((0, 0, 0))
            self.Menu_button3.update()
            self.Menu_button3.setSurfaces("Button_unpressed.png", "Button_pressed.png")
            self.Menu_button3.draw(self.screen)
            self.Menu_text.update()

        if Variables.function == "Play":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Menu_text.update()
            typen.start()

        if Variables.function == "Menu_return":
            self.Menu_button0.update()
            self.Menu_button1.update()
            self.Menu_button2.update()
            self.Menu_text.update()
            Variables.function = "Menu_info"

    def switch(self):
        Variables.visibility_text = not Variables.visibility_text

    def game_loop(self):
        a = False
        while a == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Give the signal to quit
                    a = True
                self.Menu_button0.eventhandler(event)
                self.Menu_button1.eventhandler(event)
                self.Menu_button2.eventhandler(event)
                self.Menu_button3.eventhandler(event)
            self.draw()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Give the signal to quit
                return True
            self.Menu_button0.eventhandler(event)
            self.Menu_button1.eventhandler(event)
            self.Menu_button2.eventhandler(event)
            self.Menu_button3.eventhandler(event)
        return False

class Text:
    def __init__(self, check, text, color, width, height):
        self._visible = check
        self.font_menu = pygame.font.Font(None, 48)
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
            if self._visible == False:
                self._visible = True

            elif self._visible == True:
                self._visible = False


class Button(object):
    def __init__(self, x, y, image_request, down, screensize, type, check, rect=None, highlight=None):
        self.size = screensize
        self.type = type
        self._rect = pygame.Rect(x, y, 0, 0)

        # Tracks the state of the button
        self.buttonDown = False # Is the button currently pushed down?
        self.mouseOverButton = False # Is the mouse currently hovering over the button?
        self.lastMouseDownOverButton = False # Was the last mouse down event over the mouse button? (Used to track clicks.)
        self._visible = check # Is the button visible
        #self.customSurfaces = False # Button starts as a text button instead of having custom images for each surface

        # Create the surfaces for a text button
        self.surfaceNormal = pygame.Surface(self._rect.size)
        self.surfaceDown = pygame.Surface(self._rect.size)
        self.surfaceHighlight = pygame.Surface(self._rect.size)
        self.update() # Draw the initial button images

        # Calling the function
        self.setSurfaces(image_request, down, highlight)

    def setSurfaces(self, normalSurface, downSurface, highlightSurface=None):
        """Switch the button to a custom image type of button (rather than a
        text button). You can specify either a pygame.Surface object or a
        string of a filename to load for each of the three button appearance
        states."""
        if downSurface is None:
            downSurface = normalSurface
        if highlightSurface is None:
            highlightSurface = normalSurface

        # Setting up the textures of the button
        if self._visible:
            if type(normalSurface) == str:
                self.origSurfaceNormal = pygame.image.load(normalSurface)
            if type(downSurface) == str:
                self.origSurfaceDown = pygame.image.load(downSurface)
            if type(highlightSurface) == str:
                self.origSurfaceHighlight = pygame.image.load(highlightSurface)

            if self.origSurfaceNormal.get_size() != self.origSurfaceDown.get_size() != self.origSurfaceHighlight.get_size():
                raise Exception('foo')

            self.surfaceNormal = pygame.transform.scale(self.origSurfaceNormal, self.size)
            self.surfaceDown = pygame.transform.scale(self.origSurfaceDown, self.size)
            self.surfaceHighlight = pygame.transform.scale(self.origSurfaceHighlight, self.size)
            #self.customSurfaces = True
            self._rect = pygame.Rect((self._rect.left, self._rect.top, self.surfaceNormal.get_width(), self.surfaceNormal.get_height()))


    def draw(self, surfaceObj):
        """Blit the current button's appearance to the surface object."""
        if self._visible:
            if self.buttonDown:
                surfaceObj.blit(self.surfaceDown, self._rect)
            elif self.mouseOverButton:
                surfaceObj.blit(self.surfaceHighlight, self._rect)
            else:
                surfaceObj.blit(self.surfaceNormal, self._rect)

    def update(self):
        if Variables.init == 1:
            if self._visible == False:
                self._visible = True

            elif self._visible == True:
                self._visible = False

        """Redraw the button's Surface object. Call this method when the button has changed appearance."""
        # if self.customSurfaces:
        #     self.surfaceNormal    = pygame.transform.smoothscale(self.origSurfaceNormal, self.size)
        #     self.surfaceDown      = pygame.transform.smoothscale(self.origSurfaceDown, self.size)
        #     self.surfaceHighlight = pygame.transform.smoothscale(self.origSurfaceHighlight, self.size)
        #     return

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
