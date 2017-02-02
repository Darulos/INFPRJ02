import os, sys, pygame, random, Sounds

# Importing other modules
import Variables, Score, PlayGame
from pygame.locals import *

class Play:
    def __init__(self, screen):
        self.screen = screen
        self.PlayerName1 = ""
        self.PlayerName2 = ""
        self.PlayerName3 = ""
        self.PlayerName4 = ""
        self.Player1x = 0
        self.Player1y = 840
        self.Player2x = 0
        self.Player2y = 840
        self.Player3x = 0
        self.Player3y = 840
        self.Player4x = 0
        self.Player4y = 840
        self.player = ""
        self.count = 1
        self.StartingPlace = ""
        self.screenwidth, self.screenheight = self.screen.get_size()

        # Setting up the font
        self.font = pygame.font.SysFont("consolas", 40, True)

        # Setting up the background
        self.background = pygame.image.load(os.path.join("Images", "Play_Background.png"))
        self.backgroundoutput = pygame.transform.scale(self.background, (1920, 1080))

        # Setting up the first input question (name)
        name_display = "Wat is uw naam?"
        self.name_block = self.font.render(name_display, 1, (0, 255, 255))
        self.name_rect = self.name_block.get_rect(center=(self.screenwidth/2, self.screenheight*0.2))

        # Setting up the second input question (place)
        place_display = "Wilt u beginnen op rood, groen, geel of blauw?"
        self.place_block = self.font.render(place_display, 1, (0, 255, 255))
        self.place_rect = self.place_block.get_rect(center=(self.screenwidth/2, self.screenheight*0.2))

        # Setting up the number of players question (first menu)
        number_display = "Met hoeveel spelers wilt u spelen?"
        self.number_block = self.font.render(number_display, 1, (0, 255, 255))
        self.number_rect = self.number_block.get_rect(center=(self.screenwidth/2, self.screenheight*0.2))

        # The four buttons, indicating how many players
        button_width = 64*6
        button_height = 16*6
        buttonsize = (int(button_width), int(button_height))
        self.OneButton = Button((self.screenwidth*0.35-button_width/2), (self.screenheight*0.4-button_height/2), os.path.join("Images", "One_Normal.png"), os.path.join("Images", "One_Pressed.png"), buttonsize, "1", True, 1)
        self.TwoButton = Button((self.screenwidth*0.65-button_width/2), (self.screenheight*0.4-button_height/2), os.path.join("Images", "Two_Normal.png"), os.path.join("Images", "Two_Pressed.png"), buttonsize, "2", True, 2)
        self.ThreeButton = Button((self.screenwidth*0.35-button_width/2), (self.screenheight*0.6-button_height/2), os.path.join("Images", "Three_Normal.png"), os.path.join("Images", "Three_Pressed.png"), buttonsize, "3", True, 3)
        self.FourButton = Button((self.screenwidth*0.65-button_width/2), (self.screenheight*0.6-button_height/2), os.path.join("Images", "Four_Normal.png"), os.path.join("Images", "Four_Pressed.png"), buttonsize, "4", True, 4)

        # Setting up the avatar menu text (second menu)
        avatar_display1 = "Selecteer uw avatar door op de afbeeldingen te drukken en geef uw naam."
        #avatar_display2 = " te drukken en geef uw naam."
        self.avatar_block1 = self.font.render(avatar_display1, 1, (0, 255, 255))
        self.avatar_rect1 = self.avatar_block1.get_rect(center=(self.screenwidth/2, self.screenheight*0.2))
        #self.avatar_block2 = self.font.render(avatar_display2, 1, (0, 255, 255))
        #self.avatar_rect2 = self.avatar_block2.get_rect(center=(self.screenwidth/2, self.screenheight*0.25))

        # The four buttons for avatar selection
        avatar_width = 48*5
        avatar_height = 48*5
        avatarsize = (int(avatar_width), int(avatar_height))
        self.AvaOneButton = Button((self.screenwidth*0.2-avatar_width/2), (self.screenheight*0.5-avatar_height/2), os.path.join("Images", "P1.png"), None, avatarsize, "Avatar1", True, 1)
        self.AvaTwoButton = Button((self.screenwidth*0.4-avatar_width/2), (self.screenheight*0.5-avatar_height/2), os.path.join("Images", "P2.png"), None, avatarsize, "Avatar2", True, 2)
        self.AvaThreeButton = Button((self.screenwidth*0.6-avatar_width/2), (self.screenheight*0.5-avatar_height/2), os.path.join("Images", "P3.png"), None, avatarsize, "Avatar3", True, 3)
        self.AvaFourButton = Button((self.screenwidth*0.8-avatar_width/2), (self.screenheight*0.5-avatar_height/2), os.path.join("Images", "P4.png"), None, avatarsize, "Avatar4", True, 4)

    # Function to draw all the questions
    def draw(self):
        # Draw the background
        self.screen.blit(self.backgroundoutput, (0, 0))

        if Variables.inputpart == 1:
            # Drawing the question for how many players
            self.screen.blit(self.number_block, self.number_rect)

            # Drawing the four buttons
            self.OneButton.draw(self.screen)
            self.TwoButton.draw(self.screen)
            self.ThreeButton.draw(self.screen)
            self.FourButton.draw(self.screen)

            # Drawing the exit button
            """Something something exit button to go to main menu"""


        if Variables.inputpart == 2:
            # Drawing the avatar question menu
            self.screen.blit(self.avatar_block1, self.avatar_rect1)
            #self.screen.blit(self.avatar_block2, self.avatar_rect2)

            # Drawing the buttons for the avatar menu selection
            # 1 player
            if Variables.numbplayers == 1:
                self.AvaOneButton.draw(self.screen)

            # 2 players
            if Variables.numbplayers == 2:
                self.AvaOneButton.draw(self.screen)
                self.AvaTwoButton.draw(self.screen)

            # 3 players
            if Variables.numbplayers == 3:
                self.AvaOneButton.draw(self.screen)
                self.AvaTwoButton.draw(self.screen)
                self.AvaThreeButton.draw(self.screen)

            # 4 players
            if Variables.numbplayers == 4:
                self.AvaOneButton.draw(self.screen)
                self.AvaTwoButton.draw(self.screen)
                self.AvaThreeButton.draw(self.screen)
                self.AvaFourButton.draw(self.screen)

            # Draw the entered answers
            self.typedraw()

            # Drawing the exit button
            """Something something exit button to go to inputpart 1"""

        # Flip the screen
        pygame.display.flip()

    # Function to loop everything in this menu
    def loop(self):
        while Variables.inputloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Give the signal to quit
                    Variables.inputloop = False
                self.OneButton.eventhandler(event)
                self.TwoButton.eventhandler(event)
                self.ThreeButton.eventhandler(event)
                self.FourButton.eventhandler(event)
                self.AvaOneButton.eventhandler(event)
                self.AvaTwoButton.eventhandler(event)
                self.AvaThreeButton.eventhandler(event)
                self.AvaFourButton.eventhandler(event)
            self.draw()
            self.typen()

    # Function to reset the typed in answer
    def typereset(self):
        self.player = ""
        self.count += 1

    # Function to draw all the answers given
    def typedraw(self):
        if self.count == 1:
            block = self.font.render(self.player, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.2, self.screenheight*0.7))
            self.screen.blit(block, rect)

            if Variables.numbplayers >= 1:
                # Indication text
                block = self.font.render("Vul in", 1, (0, 255, 255))
                rect = block.get_rect(center=(self.screenwidth*0.2, self.screenheight*0.8))
                self.screen.blit(block, rect)

        elif self.count == 2:
            block = self.font.render(self.PlayerName1, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.2, self.screenheight*0.7))
            self.screen.blit(block, rect)

            block = self.font.render(self.player, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.4, self.screenheight*0.7))
            self.screen.blit(block, rect)

            if Variables.numbplayers >= 2:
                # Indication text
                block = self.font.render("Vul in", 1, (0, 255, 255))
                rect = block.get_rect(center=(self.screenwidth*0.4, self.screenheight*0.8))
                self.screen.blit(block, rect)

        elif self.count == 3:
            block = self.font.render(self.PlayerName1, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.2, self.screenheight*0.7))
            self.screen.blit(block, rect)

            block = self.font.render(self.PlayerName2, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.4, self.screenheight*0.7))
            self.screen.blit(block, rect)

            block = self.font.render(self.player, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.6, self.screenheight*0.7))
            self.screen.blit(block, rect)

            if Variables.numbplayers >= 3:
                # Indication text
                block = self.font.render("Vul in", 1, (0, 255, 255))
                rect = block.get_rect(center=(self.screenwidth*0.6, self.screenheight*0.8))
                self.screen.blit(block, rect)

        elif self.count == 4:
            block = self.font.render(self.PlayerName1, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.2, self.screenheight*0.7))
            self.screen.blit(block, rect)

            block = self.font.render(self.PlayerName2, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.4, self.screenheight*0.7))
            self.screen.blit(block, rect)

            block = self.font.render(self.PlayerName3, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.6, self.screenheight*0.7))
            self.screen.blit(block, rect)

            block = self.font.render(self.player, 1, (0, 255, 255))
            rect = block.get_rect(center=(self.screenwidth*0.8, self.screenheight*0.7))
            self.screen.blit(block, rect)

            if Variables.numbplayers == 4:
                # Indication text
                block = self.font.render("Vul in", 1, (0, 255, 255))
                rect = block.get_rect(center=(self.screenwidth*0.8, self.screenheight*0.8))
                self.screen.blit(block, rect)

    # Function to enable typing in the names (is on loop)
    def typen(self):
        if Variables.inputpart == 2:
            if self.count <= Variables.numbplayers:
                # Typing function
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        # For capital letters
                        if event.unicode.isalpha():
                            Sounds.PlaySound.KeyPress(self)
                            self.player += event.unicode

                        # For numbers
                        elif event.unicode.isdigit():
                            Sounds.PlaySound.KeyPress(self)
                            self.player += event.unicode

                        # For spaces
                        elif event.key == pygame.K_SPACE:
                            Sounds.PlaySound.KeySpace(self)
                            self.player += " "

                        # For dots
                        elif event.key == pygame.K_PERIOD:
                            Sounds.PlaySound.KeyPress(self)
                            self.player += "."

                        # Enables the function of a backspace
                        elif event.key == pygame.K_BACKSPACE:
                            Sounds.PlaySound.KeySpace()
                            self.player = self.player[:-1]

                        # Checks the given name with names in the databases and empties it if there's a copy
                        elif event.key == pygame.K_RETURN:
                            if not Score.interact_database("select name from score where name = %s", False, (self.player,)):
                                Score.interact_database("INSERT INTO Score VALUES(%s, %s)", True, (self.player, 0))
                            # Setting the next typing box
                            if self.count == 1:
                                self.PlayerName1 = self.player
                                if Variables.numbplayers == 1:
                                    self.positioning()
                            elif self.count == 2:
                                self.PlayerName2 = self.player
                                if Variables.numbplayers == 2:
                                    self.positioning()
                            elif self.count == 3:
                                self.PlayerName3 = self.player
                                if Variables.numbplayers == 3:
                                    self.positioning()
                            elif self.count == 4:
                                self.PlayerName4 = self.player
                                self.positioning()
                            self.typereset()

                    self.OneButton.draw(self.screen)
                    self.TwoButton.draw(self.screen)
                    self.ThreeButton.draw(self.screen)
                    self.FourButton.draw(self.screen)
                    self.AvaOneButton.eventhandler(event)
                    self.AvaTwoButton.eventhandler(event)
                    self.AvaThreeButton.eventhandler(event)
                    self.AvaFourButton.eventhandler(event)

    # Function to set the players to a certain location
    def positioning(self):
        list = []
        counting = []
        x = 0
        # Put numbers in the list and shuffle them
        for i in range (1, Variables.numbplayers+1):
            list.append(i)
            counting.append(i)
        random.shuffle(list)

        # To assign a position to a player
        for j in range (0, Variables.numbplayers):
            if counting[j] == 1:
                x = 768
            elif counting[j] == 2:
                x = 864
            elif counting[j] == 3:
                x = 960
            elif counting[j] == 4:
                x = 1056

            if list[j] == 1:
                self.Player1x = x
            elif list[j] == 2:
                self.Player2x = x
            elif list[j] == 3:
                self.Player3x = x
            elif list[j] == 4:
                self.Player4x = x

        # Opening the actual game
        PlayGame.begin(self.screen, pygame.font.SysFont("consolas", 30, True), self.Player1x, self.Player2x, self.Player3x, self.Player4x, self.AvaOneButton.image, self.AvaTwoButton.image, self.AvaThreeButton.image, self.AvaFourButton.image,)

    # Function to draw the questions and answers
    def drawInput(self, show, type):
        # Creating the background
        self.screen.blit(self.backgroundoutput, (0, 0))

        # If statement for the name input
        if type == "Name":
            # Showing the name question
            self.screen.blit(self.name_block, self.name_rect)

        # If statement for the position input
        if type == "Place":
            # Showing the place question
            self.screen.blit(self.place_block, self.place_rect)

        # Showing the entered answer
        block = self.font.render(show, 1, (0, 255, 255))
        rect = block.get_rect(center=(self.screenwidth/2, self.screenheight*0.4))
        self.screen.blit(block, rect)

        # Flip the screen to show contents
        pygame.display.flip()


class Button(object):
    def __init__(self, x, y, normal, down, screensize, type, check, count, highlight=None):
        self.size = screensize
        self.type = type
        self._rect = pygame.Rect(x, y, 0, 0)
        self.count = count

        # Tracks the state of the button
        self.buttonDown = False # Is the button currently pushed down?
        self.mouseOverButton = False # Is the mouse currently hovering over the button?
        self.lastMouseDownOverButton = False # Was the last mouse down event over the mouse button? (Used to track clicks.)
        self._visible = check # Is the button visible

        # Create the surfaces for a text button
        self.surfaceNormal = pygame.Surface(self._rect.size)
        self.surfaceDown = pygame.Surface(self._rect.size)
        self.surfaceHighlight = pygame.Surface(self._rect.size)
        # self.update() # Draw the initial button images

        # Setting the surfaces of the buttons
        self.normal = normal
        self.down = down
        self.highlight = highlight
        self.image = normal

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
        self._visible = not self._visible

    def avatarload(self):
        # Setting the next image
        if self.count == 1:
            image = os.path.join("Images", "P2.png")
        elif self.count == 2:
            image = os.path.join("Images", "P3.png")
        elif self.count == 3:
            image = os.path.join("Images", "P4.png")
        elif self.count == 4:
            image = os.path.join("Images", "P1.png")

        # Loading the new image on the button itself
        self.image = image
        self.origSurfaceNormal = pygame.image.load(image)
        self.surfaceDown = pygame.transform.scale(self.origSurfaceNormal, self.size)
        self.surfaceNormal = pygame.transform.scale(self.origSurfaceNormal, self.size)
        self.surfaceHighlight = pygame.transform.scale(self.origSurfaceNormal, self.size)

        # Cycling through images and resetting otherwise
        if self.count <= 3:
            self.count += 1
        else:
            self.count = 1

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
        return 0

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
            Sounds.PlaySound.MouseClick(self)
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

            # Functions for the number of players buttons
            elif self.buttonDown and self.type == "1":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.numbplayers = 1
                Variables.inputpart = 2

            elif self.buttonDown and self.type == "2":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.numbplayers = 2
                Variables.inputpart = 2

            elif self.buttonDown and self.type == "3":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.numbplayers = 3
                Variables.inputpart = 2

            elif self.buttonDown and self.type == "4":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.numbplayers = 4
                Variables.inputpart = 2

            elif self.buttonDown and self.type == "Avatar1":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                # Function to change the image
                self.avatarload()

            elif self.buttonDown and self.type == "Avatar2":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                # Function to change the image
                self.avatarload()

            elif self.buttonDown and self.type == "Avatar3":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                # Function to change the image
                self.avatarload()

            elif self.buttonDown and self.type == "Avatar4":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                # Function to change the image
                self.avatarload()

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
