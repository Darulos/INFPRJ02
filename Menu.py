import os, sys, pygame
from pygame.locals import *


import Variables

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

        # Setting up the the font
        self.font_menu = pygame.font.Font(None, 48)

        # Setting up buttons in main menu
        buttonsize = (int(600/(self.width/150)), int(300/(self.height/150)))
        self.Menu_button1 = Button((self.width*0.5), (self.height*0.25), "Button_unpressed.png", "Button_pressed.png", buttonsize, "Visible", True)
        self.Menu_button2 = Button((self.width*0.5), (self.height*0.50), "Button_unpressed.png", "Button_pressed.png", buttonsize, "Exit", True)
        self.Menu_button3 = Button((self.width*0.5), (self.height*0.85), "Button_unpressed.png", "Button_pressed.png", buttonsize, "VisibleExit", False)

        # Setting up the information regarding the game
        self.Text = Info()

    def draw(self):
        # Setting the framerate
        clock = pygame.time.Clock()
        clock.tick(60)

        # Fill the screen
        self.screen.fill((0, 0, 0))

        # Set the menu text on top
        score_text = self.font_menu.render("Menu", 1, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(self.width/2, self.height*0.10))
        self.screen.blit(score_text, score_text_rect)

        # Add image of a button
        self.Menu_button1.draw(self.screen)
        self.Menu_button2.draw(self.screen)
        self.Menu_button3.draw(self.screen)

        # Add text of information
        self.Text.draw(self.screen)

        # Flip the screen
        pygame.display.flip()

    def update(self):
        self.Menu_button1.update()
        self.Menu_button2.update()
        self.switch()
        self.screen.fill((0, 0, 0))
        self.Menu_button3.update()
        self.Menu_button3.setSurfaces("Button_unpressed.png", "Button_pressed.png")
        self.Menu_button3.draw(self.screen)

    def switch(self):
        Variables.visibility_text = not Variables.visibility_text

    def game_loop(self):
        a = False
        while a == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Give the signal to quit
                    a = True
                self.Menu_button1.eventhandler(event)
                self.Menu_button2.eventhandler(event)
                self.Menu_button3.eventhandler(event)
            self.draw()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Give the signal to quit
                return True
            self.Menu_button1.eventhandler(event)
            self.Menu_button2.eventhandler(event)
            self.Menu_button3.eventhandler(event)
        return False

class Info:
    def draw(self, surface):
        if Variables.visibility_text:
            #draw spelregels text

            textheight = 20
            font_max = pygame.font.Font(None, 25)
            font_mid = pygame.font.Font(None, 20)
            font_mini = pygame.font.Font(None, 17)

            text = font_max.render("SPELREGELS", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=30

            text = font_mid.render("Voor het spelen van het spel:", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=21

            text = font_mini.render("+ Het spel kan gespeeld worden met 1 tot 4 spelers.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ Voor het beantwoorden van vragen krijgt de speler 50 seconden.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ Ieder nummer op de dobbelsteen heeft zijn eigen soort vraag:", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("            -- Cijfers 1, 3, en 5 zijn open vragen, 2, 4, en 6 zijn meerkeuzevragen", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ Er zijn vier verschillende categorieen vragen, elk met een eigen kleur:)", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("    -- Blauw = Sport           -- Groen = Geografie", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("    -- Rood = Entertainment           -- Geel = Geschiedenis", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ Elke speler krijgt een avatar toegewezen aan het begin van het spel.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ Het spel bepaalt willekeurig welke speler mag beginnen.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ De spelers kiezen in de aangegeven volgorde hun startcategorie.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=25

            text = font_mid.render("Tijdens het spel:", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=21

            text = font_mini.render("+ De speler kiest als eerste een richting (links, rechts, omhoog, omlaag).", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ Het aantal stappen in deze richting wordt bepaalt met de dobbelsteen:", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("    -- Cijfers 1 en 2 met de dobbelsteen: 1 stap in de gekozen richting.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("        -- Cijfers 3 en 4 met de dobbelsteen: 2 stappen in de gekozen richting.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("        -- Cijfers 5 en 6 met de dobbelsteen: 3 stappen in de gekozen richting.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ Als twee spelers op dezelfde positie komen, moet de speler die er stond", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("een dobbelsteen gooien, en het bijbehorende aantal stappen omlaag gaan.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ Als de speler een vraag goed beantwoordt:", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("-- Het gerolde aantal stappen mag worden gelopen door de speler", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("+ Als de speler een vraag fout beantwoordt:", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("-- De speler mag niet verplaatsen en zijn/haar beurt eindigt.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=18

            text = font_mini.render("-- Als er geen antwoord binnen de tijd wordt gegeven geldt dit ook als fout.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=21

            text = font_mid.render("Hoe win je het spel:", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)

            textheight+=19

            text = font_mini.render("Wanneer je als eerste de top haalt, ben je de winnaar van het spel!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Variables.game.width/2, textheight))
            surface.blit(text, text_rect)



class Button(object):
    def __init__(self, x, y, image_request, down, screensize, type, check, rect=None, highlight=None):
        self.size = screensize
        self.type = type
        self._rect = pygame.Rect(x, y, 0, 0)

        # Tracks the state of the button
        self.buttonDown = False # is the button currently pushed down?
        self.mouseOverButton = False # is the mouse currently hovering over the button?
        self.lastMouseDownOverButton = False # was the last mouse down event over the mouse button? (Used to track clicks.)
        self._visible = check # is the button visible
        self.customSurfaces = False # button starts as a text button instead of having custom images for each surface

        # Create the surfaces for a text button
        self.surfaceNormal = pygame.Surface(self._rect.size)
        self.surfaceDown = pygame.Surface(self._rect.size)
        self.surfaceHighlight = pygame.Surface(self._rect.size)
        self.update() # draw the initial button images

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
            self.customSurfaces = True
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

    def mouseClick(self, event):
        pass # This class is meant to be overridden.
    def mouseEnter(self, event):
        pass # This class is meant to be overridden.
    def mouseMove(self, event):
        pass # This class is meant to be overridden.
    def mouseExit(self, event):
        pass # This class is meant to be overridden.
    def mouseDown(self, event):
        pass # This class is meant to be overridden.
    def mouseUp(self, event):
        pass # This class is meant to be overridden.

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
            # if mouse has entered the button:
            self.mouseOverButton = True
            self.mouseEnter(eventObj)
            retVal.append('enter')
        elif self.mouseOverButton and not self._rect.collidepoint(eventObj.pos):
            # if mouse has exited the button:
            self.mouseOverButton = False
            hasExited = True # call mouseExit() later, since we want mouseMove() to be handled before mouseExit()

        if self._rect.collidepoint(eventObj.pos):
            # if mouse event happened over the button:
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
                # if an up/down happens off the button, then the next up won't cause mouseClick()
                self.lastMouseDownOverButton = False

        # mouse up is handled whether or not it was over the button
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

# def process_events():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             # Give the signal to quit
#             return True
#     return False

def program():
    Variables.game = Game()
    Variables.game.game_loop()

# Start the program
program()
