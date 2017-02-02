# Check player positie ------
# Geef beweegknoppen weer, dan diceknop -------
# Geef vraag weer
# Check soort vraag
# Geef knoppen van soort vraag weer / inputbox
# Vraag goed beantwoord = bewegen
# Geef feedback terug


import os, sys, pygame, random, time

import Database, Variables
from pygame.locals import *


class Avatar:
    def __init__(self, id, x, y, image):
        self.id = id
        self.x = x
        self.y = y
        self.correct = 0
        self.wrong = 0

        # Initialise the image of the player
        self.image = pygame.image.load(image)

    # Function to draw the player at it's current position
    def draw(self, screen):
        # Draw the player
        self.rect = (self.x, self.y)
        screen.blit(self.image, self.rect)

    # Function to move the player to its new position according to the dice outcome
    def movement(self, number, direction):
        if Variables.dicecheck:
            # Setting the number of places to move
            if number == 1 or number == 2:
                movement = 1
            elif number == 3 or number == 4:
                movement = 2
            else:
                movement = 3

            # Move function, depending on which button is pressed
            if (Variables.answer == True) and (Variables.movement != ""):
                # Lower part of the board
                if self.y > 400:
                    if direction == "Left":
                        self.x -= 48 * movement
                        if self.x < 768:
                            self.x += 384
                    elif direction == "Right":
                        self.x += 48 * movement
                        if self.x > 1104:
                            self.x -= 384
                    elif direction == "Up":
                        self.y -= 48 * movement
                        # Check to see if you go to top part of board
                        if self.y < 400:
                            if self.x < 864:
                                self.x = 792
                            elif self.x < 960:
                                self.x = 888
                            elif self.x < 1056:
                                self.x = 984
                            elif self.x < 1104:
                                self.x = 1080
                    elif direction == "Down":
                        self.y += 48 * movement
                        # Check to see if you reach bottom of board
                        if self.y > 886:
                            self.y = 840

                # Top part of the board
                elif self.y < 400:
                    if direction == "Left":
                        self.x -= 96 * movement
                        if self.x < 792:
                            self.x += 384
                    elif direction == "Right":
                        self.x += 96 * movement
                        if self.x > 1080:
                            self.x -= 384
                    elif direction == "Up":
                        self.y -= 48 * movement
                        # Check for winning condition
                        if self.y < 168:
                            screen = Variables.game.screen#pygame.display.set_mode(size)
                            pygame.display.set_caption("end screen")
                            endscreen = pygame.image.load(os.path.join("Images", "Euromast_End.png"))
                            echtscherm = pygame.transform.scale(endscreen, (1920,1080))
                            other_width = 32*4
                            other_height = 32*4
                            othersize = (int(other_width), int(other_height))
                            ExitButton = Button((1920*0.96-other_width/2), (1080*0.07-other_height/2), os.path.join("Images", "Exit_Normal.png"), os.path.join("Images", "Exit_Pressed.png"), othersize, "Exit", True)
                            button_width = 64*6
                            button_height = 16*6
                            buttonsize = (int(button_width), int(button_height))
                            YesButton = Button((1920*0.5-button_width/2), (1080*0.7-button_height/2), os.path.join("Images", "Ja_Normal.png"), os.path.join("Images", "Ja_Pressed.png"), buttonsize, "Yes", True)
                            NoButton = Button((1920*0.5-button_width/2), (1080*0.8-button_height/2), os.path.join("Images", "Nee_Normal.png"), os.path.join("Images", "Nee_Pressed.png"), buttonsize, "No", True)
                            while Variables.gameloop:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        # Give the signal to quit
                                        sys.exit()
                                    ExitButton.eventhandler(event)
                                    YesButton.eventhandler(event)
                                    NoButton.eventhandler(event)
                                screen.blit(echtscherm, (0, 0))
                                if not Variables.exitcheck:
                                    ExitButton.draw(screen)
                                else:
                                    YesButton.draw(screen)
                                    NoButton.draw(screen)


                                    # Flip the screen to show contents
                                pygame.display.flip()

                            """Something something winning"""
                    elif direction == "Down":
                        self.y += 48 * movement
                        # Check to see if you go to top part of board
                        if self.y > 400:
                            if self.x < 793:
                                self.x = 816
                            elif self.x < 889:
                                self.x = 912
                            elif self.x < 985:
                                self.x = 1008
                            elif self.x < 1081:
                                self.x = 1104
            Variables.answer = False
            Variables.dicecheck = False
            Variables.movement = ""


class Question:
    def __init__(self):
        self.converter = ""
        self.check = True

    # Function to update the question to a new one
    def updatequestion(self):
        if self.check:
            self.converter = Database.question(self.questionint)

    # Function to update the possibilities according to the question
    def updateposs(self):
        if self.check:
            self.possibility1 = Database.possibilities1(self.questionint)
            self.possibility2 = Database.possibilities2(self.questionint)
            self.possibility3 = Database.possibilities3(self.questionint)

    # Function to draw the question and possibilities
    def draw(self, screen, font):
        # Setting the font and screen
        self.font = font
        self.screenwidth, self.screenheight = screen.get_size()

        # True if the dice has been rolled and the movement direction is set
        if (Variables.dicecheck == True) and (Variables.movement != ""):
            # Setting the question
            self.updatequestion()

            # Show the questions
            i = 0
            j = len(self.converter)
            x = 0
            # Show the questions
            if i+30 < j and self.converter[i+30] == " ":
                converteroutput = self.converter[i:i+30]
                i += 30
            else:
                x = i
                for i in range(x + 30):
                    if (x + 30)>= j:
                        converteroutput = self.converter[x:j]
                        i += 1000
                        break
                    elif self.converter[(x + 30) - i] == " ":
                        converteroutput = self.converter[x:(x + 30) - i]
                        i = x+30-i
                        break
            question_block = self.font.render(converteroutput, 1, (0, 255, 255))
            question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5))
            screen.blit(question_block, question_rect)

            if i+30 < j and self.converter[i+30] == " ":
                converteroutput = self.converter[i:i+30]
                i += 30
            else:
                x = i
                for i in range(x + 30):
                    if (x + 30)>= j:
                        converteroutput = self.converter[x:j]
                        i += 1000
                        break
                    elif self.converter[(x + 30) - i] == " ":
                        converteroutput = self.converter[x:(x + 30) - i]
                        i = x+30-i
                        break
            question_block = self.font.render(converteroutput, 1, (0, 255, 255))
            question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+50))
            screen.blit(question_block, question_rect)

            if i+30 < j and self.converter[i+30] == " ":
                converteroutput = self.converter[i:i+30]
                i += 30
            else:
                x = i
                for i in range(x + 30):
                    if (x + 30)>= j:
                        converteroutput = self.converter[x:j]
                        i += 1000
                        break
                    elif self.converter[(x + 30) - i] == " ":
                        converteroutput = self.converter[x:(x + 30) - i]
                        i = x+30-i
                        break
            question_block = self.font.render(converteroutput, 1, (0, 255, 255))
            question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+100))
            screen.blit(question_block, question_rect)

            if i+30 < j and self.converter[i+30] == " ":
                converteroutput = self.converter[i:i+30]
                i += 30
            else:
                x = i
                for i in range(x + 30):
                    if (x + 30)>= j:
                        converteroutput = self.converter[x:j]
                        i += 1000
                        break
                    elif self.converter[(x + 30) - i] == " ":
                        converteroutput = self.converter[x:(x + 30) - i]
                        i = x+30-i
                        break
            question_block = self.font.render(converteroutput, 1, (0, 255, 255))
            question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+150))
            screen.blit(question_block, question_rect)

            if i+30 < j and self.converter[i+30] == " ":
                converteroutput = self.converter[i:i+30]
                i += 30
            else:
                x = i
                for i in range(x + 30):
                    if (x + 30)>= j:
                        converteroutput = self.converter[x:j]
                        i += 1000
                        break
                    elif self.converter[(x + 30) - i] == " ":
                        converteroutput = self.converter[x:(x + 30) - i]
                        i = x+30-i
                        break
            question_block = self.font.render(converteroutput, 1, (0, 255, 255))
            question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+200))
            screen.blit(question_block, question_rect)

            if i+30 < j and self.converter[i+30] == " ":
                converteroutput = self.converter[i:i+30]
                i += 30
            else:
                x = i
                for i in range(x + 30):
                    if (x + 30)>= j:
                        converteroutput = self.converter[x:j]
                        i += 1000
                        break
                    elif self.converter[(x + 30) - i] == " ":
                        converteroutput = self.converter[x:(x + 30) - i]
                        i = x+30-i
                        break
            question_block = self.font.render(converteroutput, 1, (0, 255, 255))
            question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+250))
            screen.blit(question_block, question_rect)
            # Show the answers
            self.updateposs()
            self.check = False

            # Open question
            if self.possibility1 == "":
                Variables.questionType = 1

            # True/false question
            elif (self.possibility1 != "") and (self.possibility3 == ""):
                # Drawing the first possibility
                converteroutput = self.possibility1
                poss_blockA = self.font.render(converteroutput, 1, (0, 255, 255))
                poss_rectA = poss_blockA.get_rect(center=(self.screenwidth/5, self.screenheight/5+250))
                screen.blit(poss_blockA, poss_rectA)

                # Drawing the second possibility
                converteroutput = self.possibility2
                poss_blockB = self.font.render(converteroutput, 1, (0, 255, 255))
                poss_rectB = poss_blockB.get_rect(center=(self.screenwidth/5, self.screenheight/5+300))
                screen.blit(poss_blockB, poss_rectB)

                Variables.questionType = 2

            # Multiple choice question
            else:
                # Drawing the first possibility
                converteroutput = self.possibility1
                poss_blockA = self.font.render(converteroutput, 1, (0, 255, 255))
                poss_rectA = poss_blockA.get_rect(center=(self.screenwidth/5, self.screenheight/5+250))
                screen.blit(poss_blockA, poss_rectA)

                # Drawing the second possibility
                converteroutput = self.possibility2
                poss_blockB = self.font.render(converteroutput, 1, (0, 255, 255))
                poss_rectB = poss_blockB.get_rect(center=(self.screenwidth/5, self.screenheight/5+300))
                screen.blit(poss_blockB, poss_rectB)

                # Drawing the third possibility
                converteroutput = self.possibility3
                poss_blockC = self.font.render(converteroutput, 1, (0, 255, 255))
                poss_rectC = poss_blockC.get_rect(center=(self.screenwidth/5, self.screenheight/5+350))
                screen.blit(poss_blockC, poss_rectC)

                Variables.questionType = 3

    # Function to pull a question according to the position of the current player
    def pulling(self, player):
        # Setting the questiontype for the lower grid
        if player != None:
            if player.x < 864 and player.y > 400:
                self.color = "Rood"
            elif player.x < 960 and player.y > 400:
                self.color = "Geel"
            elif player.x < 1056 and player.y > 400:
                self.color = "Groen"
            elif player.x < 1152 and player.y > 400:
                self.color = "Blauw"

            # Setting the questiontype for the higher grid
            if player.x < 864 and player.y < 400:
                self.color = "Geel"
            elif player.x < 960 and player.y < 400:
                self.color = "Groen"
            elif player.x < 1056 and player.y < 400:
                self.color = "Blauw"
            elif player.x < 1152 and player.y < 400:
                self.color = "Rood"

    # Function to set the questiontype
    def pick_number(self, type):
        if type == "Geel":
            QuestionID = random.randint(1, 38)
        elif type == "Groen":
            QuestionID = random.randint(39, 60)
        elif type == "Rood":
            QuestionID = random.randint(61, 89)
        elif type == "Blauw":
            QuestionID = random.randint(90, 119)
        return QuestionID

    # Start of finding a question
    def begin(self):
        self.questionint = self.pick_number(self.color)
        Variables.questionint = self.questionint


class Board:
    def __init__(self, screen, font, player1, player2, player3, player4):
        # Setting the screen
        self.screen = screen
        self.screenwidth, self.screenheight = self.screen.get_size()

        # Setting the players
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4

        # List for playersystem
        self.list = []

        # Setting the win condition variable
        self.wingame = False

        # Initialising the dice
        self.Dice1 = pygame.image.load(os.path.join('Images', 'Dice1.png'))
        self.Dice2 = pygame.image.load(os.path.join('Images', 'Dice2.png'))
        self.Dice3 = pygame.image.load(os.path.join('Images', 'Dice3.png'))
        self.Dice4 = pygame.image.load(os.path.join('Images', 'Dice4.png'))
        self.Dice5 = pygame.image.load(os.path.join('Images', 'Dice5.png'))
        self.Dice6 = pygame.image.load(os.path.join('Images', 'Dice6.png'))

        # Initialising the font
        self.font = font

        # Initialising the background
        self.background = pygame.image.load(os.path.join("Images", "Play_Background.png"))
        self.backgroundoutput = pygame.transform.scale(self.background, (1920, 1080))

        # Initialising the gameboard
        self.gameboard = pygame.image.load(os.path.join("Images", "Gameboard.png"))
        self.gameboardoutput = pygame.transform.scale(self.gameboard, (1920, 1080))

        # Initialising the answer
        self.answer = ""

        # Initialising buttons
        dice_width = 35*6
        dice_height = 35*6
        dicesize = (int(dice_width), int(dice_height))
        self.DiceButton = Button((self.screenwidth*0.8-dice_width/2), (self.screenheight*0.5-dice_height/2), os.path.join("Images", "DiceRoll.png"), None, dicesize, "Dice", False)

        # Move buttons
        move_width = 32*5
        move_height = 32*5
        movesize = (int(move_width), int(move_height))
        self.LeftButton = Button((self.screenwidth*0.70-move_width/2), (self.screenheight*0.90-move_height/2), os.path.join("Images", "Left_Normal.png"), os.path.join("Images", "Left_Pressed.png"), movesize, "MovementLeft", True)
        self.UpButton = Button((self.screenwidth*0.80-move_width/2), (self.screenheight*0.72-move_height/2), os.path.join("Images", "Up_Normal.png"), os.path.join("Images", "Up_Pressed.png"), movesize, "MovementUp", True)
        self.RightButton = Button((self.screenwidth*0.90-move_width/2), (self.screenheight*0.90-move_height/2), os.path.join("Images", "Right_Normal.png"), os.path.join("Images", "Right_Pressed.png"), movesize, "MovementRight", True)
        self.DownButton = Button((self.screenwidth*0.80-move_width/2), (self.screenheight*0.90-move_height/2), os.path.join("Images", "Down_Normal.png"), os.path.join("Images", "Down_Pressed.png"), movesize, "MovementDown", True)

        # Questionbuttons
        self.Abutton = Button((self.screenwidth*0.1-move_width/2), (self.screenheight*0.9-move_height/2), os.path.join("Images", "A_Normal.png"), os.path.join("Images", "A_Pressed.png"), movesize, "A", False)
        self.Bbutton = Button((self.screenwidth*0.2-move_width/2), (self.screenheight*0.9-move_height/2), os.path.join("Images", "B_Normal.png"), os.path.join("Images", "B_Pressed.png"), movesize, "B", False)
        self.Cbutton = Button((self.screenwidth*0.3-move_width/2), (self.screenheight*0.9-move_height/2), os.path.join("Images", "C_Normal.png"), os.path.join("Images", "C_Pressed.png"), movesize, "C", False)

        # Exit button
        other_width = 32*4
        other_height = 32*4
        othersize = (int(other_width), int(other_height))
        self.ExitButton = Button((self.screenwidth*0.96-other_width/2), (self.screenheight*0.07-other_height/2), os.path.join("Images", "Exit_Normal.png"), os.path.join("Images", "Exit_Pressed.png"), othersize, "Exit", True)

        # Yes and no button
        button_width = 64*6
        button_height = 16*6
        buttonsize = (int(button_width), int(button_height))
        self.YesButton = Button((self.screenwidth*0.5-button_width/2), (self.screenheight*0.7-button_height/2), os.path.join("Images", "Ja_Normal.png"), os.path.join("Images", "Ja_Pressed.png"), buttonsize, "Yes", True)
        self.NoButton = Button((self.screenwidth*0.5-button_width/2), (self.screenheight*0.8-button_height/2), os.path.join("Images", "Nee_Normal.png"), os.path.join("Images", "Nee_Pressed.png"), buttonsize, "No", True)


    # Loop of the game itself
    def loop(self):
        Variables.gameloop = True
        while Variables.gameloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Give the signal to quit
                    sys.exit()
                self.DiceButton.eventhandler(event)
                self.LeftButton.eventhandler(event)
                self.UpButton.eventhandler(event)
                self.RightButton.eventhandler(event)
                self.DownButton.eventhandler(event)
                self.Abutton.eventhandler(event)
                self.Bbutton.eventhandler(event)
                self.Cbutton.eventhandler(event)
                self.ExitButton.eventhandler(event)
                self.YesButton.eventhandler(event)
                self.NoButton.eventhandler(event)
            # To set the first question right
            if Variables.gamestart:
                self.playersystem()
                question.pulling(Variables.playerturn)
                question.begin()
            self.draw()
            self.typen()
            self.button()
            self.playersystem()

    # Function to draw everything (is being looped)
    def draw(self):
        # Draw the background
        self.screen.blit(self.backgroundoutput, (0, 0))

        # Draws only when the player has not yet pressed the exit button
        if not Variables.exitcheck:
            # Draw the card background
            """Something something cardback"""

            # Draw the question
            question.draw(self.screen, self.font)

            # Draw the answer
            self.typedraw()

            # Draw the gameboard
            self.screen.blit(self.gameboardoutput, (0,0))

            # Draw the character(s)
            self.playerdraw()

            # Draw the dice
            self.Diceupdate()
            self.DiceButton.draw(self.screen)

            # Draw the movemenbuttons
            self.LeftButton.draw(self.screen)
            self.UpButton.draw(self.screen)
            self.RightButton.draw(self.screen)
            self.DownButton.draw(self.screen)

            # Draw the questionbuttons (function)
            self.qbuttondraw(self.screen)
            self.qbuttonupdate()

            # Draw the exit button
            self.ExitButton.draw(self.screen)

            # Draw the score
            self.scoredraw()


        # Draws when wanting to exit the play game part
        else:
            self.YesButton.draw(self.screen)
            self.NoButton.draw(self.screen)


        # Flip the screen to show contents
        pygame.display.flip()

    # Function to enable the playersystem
    def playersystem(self):
        if Variables.gamestart:
            for i in range (0, Variables.numbplayers):
                self.list.append(i)
            Variables.gamestart = False
            random.shuffle(self.list)

        if Variables.listcheck < Variables.numbplayers:
            if self.list[Variables.listcheck] == self.player1.id:
                Variables.playerturn = self.player1
            if self.player2 != None:
                if (self.list[Variables.listcheck] == self.player2.id):
                    Variables.playerturn = self.player2
            if self.player3 != None:
                if (self.list[Variables.listcheck] == self.player3.id):
                    Variables.playerturn = self.player3
            if self.player4 != None:
                if (self.list[Variables.listcheck] == self.player4.id):
                    Variables.playerturn = self.player4

    # Function to go to the next player, after a question is solved
    def playernext(self):
        if Variables.listcheck < Variables.numbplayers:
            Variables.listcheck += 1
        else:
            Variables.listcheck = 0

    # Function to draw a specific number of players
    def playerdraw(self):
        self.player1.draw(self.screen)
        if Variables.numbplayers == 2:
            self.player2.draw(self.screen)
        if Variables.numbplayers == 3:
            self.player2.draw(self.screen)
            self.player3.draw(self.screen)
        if Variables.numbplayers == 4:
            self.player2.draw(self.screen)
            self.player3.draw(self.screen)
            self.player4.draw(self.screen)

    # Function to show/hide the dice
    def Diceupdate(self):
        if Variables.dicevisible:
            self.DiceButton.update()
            Variables.dicevisible = False

    # Function to show/hide the answerbuttons
    def qbuttonupdate(self):
        if Variables.buttoncheck:
            # True/false question
            if Variables.questionType == 2:
                self.Abutton.update()
                self.Bbutton.update()
                Variables.buttoncheck = False

            #Multiple choice questions
            if Variables.questionType == 3:
                self.Abutton.update()
                self.Bbutton.update()
                self.Cbutton.update()
                Variables.buttoncheck = False

    # Function to draw the answerbuttons
    def qbuttondraw(self, screen):
        # True or false questions
        if Variables.questionType == 2:
            self.Abutton.draw(screen)
            self.Bbutton.draw(screen)

        # Multiple choice questions
        if Variables.questionType == 3:
            self.Abutton.draw(screen)
            self.Bbutton.draw(screen)
            self.Cbutton.draw(screen)

    # Function to draw the total answer correct and incorrect at the top
    def scoredraw(self):
        # Update the score
        self.correct_display = Variables.playerturn.correct
        self.correct_block = self.font.render("Questions correct: {}".format(self.correct_display), 1, (0, 255, 255))
        self.correct_rect = self.correct_block.get_rect(center=(self.screenwidth/2, self.screenwidth*0.05))
        self.wrong_display = Variables.playerturn.wrong
        self.wrong_block = self.font.render("Questions wrong: {}".format(self.wrong_display), 1, (0, 255, 255))
        self.wrong_rect = self.wrong_block.get_rect(center=(self.screenwidth/2, self.screenwidth*0.07))

        # Draw the score
        self.screen.blit(self.correct_block, self.correct_rect)
        self.screen.blit(self.wrong_block, self.wrong_rect)

    # Function to draw the updated answer when typing
    def typedraw(self):
        # Update the answer
        self.answer_display = self.font.render(self.answer, 1, (0, 255, 255))
        self.answer_block = self.answer_display.get_rect(center=(self.screenwidth/5 , self.screenheight*0.75))

        # Draw the answer
        self.screen.blit(self.answer_display, self.answer_block)

    # Function for the answerbuttons to work (is being looped)
    def button(self):
        if Variables.buttonanswer != "":
           # Making the buttons disappear
            self.qbuttonupdate()

            # True/False questions
            if Variables.questionType == 2:
                if Variables.buttonanswer == "A":
                    tempanswer = Database.possibilities1(Variables.questionint)
                elif Variables.buttonanswer == "B":
                    tempanswer = Database.possibilities2(Variables.questionint)

            # Multiple choice questions
            elif Variables.questionType == 3:
                if Variables.buttonanswer == "A":
                    tempanswer = Database.possibilities1(Variables.questionint)
                elif Variables.buttonanswer == "B":
                    tempanswer = Database.possibilities2(Variables.questionint)
                elif Variables.buttonanswer == "C":
                    tempanswer = Database.possibilities3(Variables.questionint)

            if tempanswer in Database.answers(Variables.questionint):
                Variables.playerturn.correct += 1
                Variables.answer = True
                Variables.questiondone = True
                Variables.dicevisible = True
                Variables.movecheck = True
                Variables.movedone = True
                self.playernext()

            else:
                Variables.playerturn.wrong += 1
                Variables.answer = False
                Variables.questiondone = True
                Variables.dicevisible = True
                Variables.movecheck = True
                Variables.movedone = True
                self.playernext()

            # New question
            Variables.playerturn.movement(Variables.dicenumber, Variables.movement)
            question.pulling(Variables.playerturn)
            question.begin()
            question.check = True

            # Resetting the dice
            self.DiceButton.dicereset()

            # Resetting global variables
            Variables.buttonanswer = ""
            Variables.questionType = 0

    # Function to enable the typing (is being looped)
    def typen(self):
        if Variables.questionType == 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # For capital letters
                    if event.unicode.isalpha():
                        self.answer += event.unicode
                        loop = False

                    # For numbers
                    elif event.unicode.isdigit():
                        self.answer += event.unicode
                        loop = False

                    # For spaces
                    elif event.key == pygame.K_SPACE:
                        self.answer += " "
                        loop = False

                    # For dots
                    elif event.key == pygame.K_PERIOD:
                        self.answer += "."
                        loop = False

                    # Enables the function of a backspace
                    elif event.key == pygame.K_BACKSPACE:
                        self.answer = self.answer[:-1]
                        loop = False

                    # When pressing enter, it checks the answer with the database
                    elif event.key == pygame.K_RETURN:
                        tempanswer = self.answer.upper()
                        numbcheck = self.numbcheck(tempanswer)
                        # When the answer is correct en een woord
                        if (tempanswer in Database.answers(Variables.questionint).upper()) and (tempanswer != "") and (len(tempanswer) >= 4):
                            Variables.playerturn.correct += 1
                            Variables.answer = True
                            Variables.playerturn.movement(Variables.dicenumber, Variables.movement)
                            question.pulling(Variables.playerturn)
                            question.begin()
                            self.answer = ""
                            question.check = True
                            Variables.questionType = 0
                            Variables.questiondone = True
                            Variables.dicevisible = True
                            Variables.movecheck = True
                            Variables.movedone = True
                            self.playernext()

                            # Resetting the dice
                            self.DiceButton.dicereset()

                        elif (tempanswer in Database.answers(Variables.questionint).upper()) and (tempanswer != "") and numbcheck :
                            Variables.playerturn.correct += 1
                            Variables.answer = True
                            Variables.playerturn.movement(Variables.dicenumber, Variables.movement)
                            question.pulling(Variables.playerturn)
                            question.begin()
                            self.answer = ""
                            question.check = True
                            Variables.questionType = 0
                            Variables.questiondone = True
                            Variables.dicevisible = True
                            Variables.movecheck = True
                            Variables.movedone = True
                            self.playernext()

                            # Resetting the dice
                            self.DiceButton.dicereset()

                        # When the answer is wrong
                        else:
                            Variables.playerturn.wrong += 1
                            Variables.answer = False
                            Variables.playerturn.movement(Variables.dicenumber, Variables.movement)
                            question.pulling(Variables.playerturn)
                            question.begin()
                            self.answer = ""
                            question.check = True
                            Variables.questionType = 0
                            Variables.questiondone = True
                            Variables.dicevisible = True
                            Variables.movecheck = True
                            Variables.movedone = True
                            self.playernext()

                            # Resetting the dice
                            self.DiceButton.dicereset()

                self.DiceButton.eventhandler(event)
                self.LeftButton.eventhandler(event)
                self.UpButton.eventhandler(event)
                self.RightButton.eventhandler(event)
                self.DownButton.eventhandler(event)
                self.ExitButton.eventhandler(event)
                self.YesButton.eventhandler(event)
                self.NoButton.eventhandler(event)

                if event.type == pygame.QUIT:
                    # Give the signal to quit
                    sys.exit()

    # Function to check the filled in string at typen
    def numbcheck(self, number):
        if "1" in number or "2" in number or "3" in number or "4" in number or "5" in number or "6" in number or "7" in number or "8" in number or "9" in number or "0" in number:
            return True
        else:
            return False


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
        # self.update() # Draw the initial button images

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
        self._visible = not self._visible

    # Functions for the dice throw
    def dice(self):
        # Throwing a random number for the dice
        """Something something check to make sure it can only be rolled once"""
        throw = random.randint(1,6)
        if throw == 1:
            image = os.path.join("Images", "Dice1.png")
            Variables.dicenumber = 1
        elif throw == 2:
            image = os.path.join("Images", "Dice2.png")
            Variables.dicenumber = 2
        elif throw == 3:
            image = os.path.join("Images", "Dice3.png")
            Variables.dicenumber = 3
        elif throw == 4:
            image = os.path.join("Images", "Dice4.png")
            Variables.dicenumber = 4
        elif throw == 5:
            image = os.path.join("Images", "Dice5.png")
            Variables.dicenumber = 5
        else:
            image = os.path.join("Images", "Dice6.png")
            Variables.dicenumber = 6
        # Enabling movement of the avatar
        Variables.dicecheck = True
        # Disabling to change the direction
        Variables.movecheck = False
        # Calling the image load function
        self.diceload(image)

    # Function to load the image of the dice
    def diceload(self, image):
        # Loading the image on the button itself
        self.origSurfaceNormal = pygame.image.load(image)
        self.surfaceDown = pygame.transform.scale(self.origSurfaceNormal, self.size)
        self.surfaceNormal = pygame.transform.scale(self.origSurfaceNormal, self.size)
        self.surfaceHighlight = pygame.transform.scale(self.origSurfaceNormal, self.size)

    # Function to reset the dice
    def dicereset(self):
        self.origSurfaceNormal = pygame.image.load(os.path.join("Images", "DiceRoll.png"))
        self.surfaceDown = pygame.transform.scale(self.origSurfaceNormal, self.size)
        self.surfaceNormal = pygame.transform.scale(self.origSurfaceNormal, self.size)
        self.surfaceHighlight = pygame.transform.scale(self.origSurfaceNormal, self.size)

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
            if self.lastMouseDownOverButton:
                doMouseClick = True
            self.lastMouseDownOverButton = False

            if self.buttonDown and self.type == "Exit":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.exitcheck = True

            elif self.buttonDown and self.type == "Yes":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.gameloop = False

            elif self.buttonDown and self.type == "No":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.exitcheck = False

            elif self.buttonDown and (self.type == "Visible" or self.type == "VisibleExit"):
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.function = "Menu_info"
                self._propSetVisible()

            elif self.buttonDown and self.type == "Dice":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                if Variables.diceroll:
                    self.dice()
                    Variables.buttoncheck = True
                    Variables.diceroll = False

            elif self.buttonDown and self.type == "MovementLeft":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                if Variables.movecheck:
                    Variables.movement = "Left"
                if Variables.questiondone:
                    Variables.diceroll = True
                    Variables.dicevisible = True
                    Variables.questiondone = False

            elif self.buttonDown and self.type == "MovementUp":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                if Variables.movecheck:
                    Variables.movement = "Up"
                if Variables.questiondone:
                    Variables.diceroll = True
                    Variables.dicevisible = True
                    Variables.questiondone = False

            elif self.buttonDown and self.type == "MovementRight":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                if Variables.movecheck:
                    Variables.movement = "Right"
                if Variables.questiondone:
                    Variables.diceroll = True
                    Variables.dicevisible = True
                    Variables.questiondone = False

            elif self.buttonDown and self.type == "MovementDown":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                if Variables.movecheck:
                    Variables.movement = "Down"
                if Variables.questiondone:
                    Variables.diceroll = True
                    Variables.dicevisible = True
                    Variables.questiondone = False

            elif self.buttonDown and self.type == "A":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.buttonanswer = "A"
                Variables.buttoncheck = True

            elif self.buttonDown and self.type == "B":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.buttonanswer = "B"
                Variables.buttoncheck = True

            elif self.buttonDown and self.type == "C":
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
                Variables.buttonanswer = "C"
                Variables.buttoncheck = True

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


# Setting all variables
gameset = True
question = Question()

def reset():
    Variables.dicenumber = 0
    Variables.dicecheck = False
    Variables.movement = ""
    Variables.answer = False
    Variables.questionType = 0
    Variables.buttonanswer = ""
    Variables.questionint = 0
    Variables.buttoncheck = False
    Variables.diceroll = True
    Variables.dicevisible = False
    Variables.questiondone = True
    Variables.movecheck = True
    Variables.gameloop = True
    Variables.exitcheck = False


def begin(screen, font, player1x, player2x, player3x, player4x, image1, image2, image3, image4):
    # Enabling loop
    reset()
    if Variables.numbplayers == 1:
        player1 = Avatar(0, player1x, 840, image1)
        board = Board(screen, font, player1, None, None, None)
    elif Variables.numbplayers == 2:
        player1 = Avatar(0, player1x, 840, image1)
        player2 = Avatar(1, player2x, 840, image2)
        board = Board(screen, font, player1, player2, None, None)
    elif Variables.numbplayers == 3:
        player1 = Avatar(0, player1x, 840, image1)
        player2 = Avatar(1, player2x, 840, image2)
        player3 = Avatar(2, player3x, 840, image3)
        board = Board(screen, font, player1, player2, player3, None)
    elif Variables.numbplayers == 4:
        player1 = Avatar(0, player1x, 840, image1)
        player2 = Avatar(1, player2x, 840, image2)
        player3 = Avatar(2, player3x, 840, image3)
        player4 = Avatar(3, player4x, 840, image4)
        board = Board(screen, font, player1, player2, player3, player4)
    board.loop()
