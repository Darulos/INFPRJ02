import Variables
import pygame
import sys
import Score
import random
import psycopg2
import gameboard


def interact_database(command, params=None):
    connection = psycopg2.connect("dbname=INF1H_Project_2_Group_4 user=postgres password=INF1HGroup4")
    cursor = connection.cursor()
    cursor.execute(command, params)
    connection.commit()

    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        print("Connection failure.")
        pass

    cursor.close()
    connection.close()

    return results


def pick_number(type):
    if type == 'g':
        QuestionID = random.randint(1, 38)
    elif type == 'gr':
        QuestionID = random.randint(39, 60)
    elif type == 'r':
        QuestionID = random.randint(61, 89)
    elif type == 'b':
        QuestionID = random.randint(90, 119)
    else:
        QuestionID = random.randint(1, 119)
    return QuestionID


def question(number):
    return interact_database("SELECT Question FROM Questions WHERE Question_ID = %s", (number,))[0][0]


def possibilities(number):
    return interact_database("SELECT Possibilities FROM Questions WHERE Question_ID = %s", (number,))[0][0]


def answers(number):
    return interact_database("SELECT Answers FROM Questions WHERE Question_ID = %s", (number,))[0][0]


def begin():
    num = random.randint(1, 119)
    Variables.questionint = num

'''
def GameTimer():
    clock = pygame.time.Clock()
    clock.tick(1)
    clock_variable = 5
    if int(clock.get_fps() * 5) % 60 == 0:
        Variables.QuestionTimer -= 1
        if Variables.QuestionTimer == 0:
            Variables.Correct = False
            Variables.QuestionTimer = 10
'''


def typen():
    tempantwoord = None
    Variables.Playerscore = 0
    highscore = str(interact_database("SELECT MAX(Score) FROM score;",)[0][0])
    # variable om het getypte antwoord op te slaan
    boardloop = True
    loop = True
    antwoord = ""
    # alvast font vaststellen
    font = pygame.font.Font(None, 30)
    score_font = pygame.font.Font(None, 60)
    # loop om het programma lopend te houden
    while loop:
        # loopt alle events door op zoek naar een van de if's
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # zet de aangetikte letter/hoofdletter in antwoord
                if event.unicode.isalpha():
                    antwoord += event.unicode

                # zet de aangetikte cijfer in antwoord
                elif event.unicode.isdigit():
                    antwoord += event.unicode

                # zet de aangetikte spatie in antwoord
                elif event.key == pygame.K_SPACE:
                    antwoord += " "

                # zet de aangetikte punt in antwoord
                elif event.key == pygame.K_PERIOD:
                    antwoord += "."

                # maakt antwoord 1 lengte korter wanneer backspace wordt aangetikt
                elif event.key == pygame.K_BACKSPACE:
                    antwoord = antwoord[:-1]

                elif Variables.Correct is False:
                    print("Game over! Goed antwoord:")
                    # print het goede antwoord op de vraag
                    print(answers(Variables.questionint))
                    print("Hoogste score:")
                    # geeft alleen de hoogste score weer
                    print(interact_database("SELECT MAX(Score) FROM score;")[0][0])
                    # geeft de speler de kans om nog even te kijken als dit in de pygame screen wordt weergegeven
                    pygame.quit()
                    sys.exit()

                # checkt gegeven antwoord met het answer in de database en haalt antwoord leeg
                elif event.key == pygame.K_RETURN:
                    # if antwoord in answer, display correct, score +=
                    # haalt antwoord op uit database
                    tempantwoord = antwoord.upper()
                    if tempantwoord.upper() in answers(Variables.questionint).upper():  # and antwoord is not "":
                        Variables.Correct = True
                    else:
                        Variables.Correct = False
                    if Variables.Correct is True:
                        # antwoord is leeg zodat deze voor de volgende vraag hergebruikt kan worden
                        antwoord = ""
                        print("Goed zo jongen")
                        # update de huidige score
                        Variables.PlayerScore += 10
                        # als je huidige score hoger is dan die in de database onder de ingevoerde naam wordt het geupdate
                        BlijkbaarIsDitNodig = interact_database("SELECT Score, Name FROM score WHERE Name = %s", (Variables.Player_Name,))[0][0]
                        if Variables.PlayerScore > BlijkbaarIsDitNodig:
                            Score.upload_score(Variables.PlayerScore, Variables.Player_Name)
                        Variables.QuestionTimer = 50
                        loop = False
                        while boardloop is True:
                            Variables.player1 = gameboard.avatars(1, Variables.player1x, Variables.player1y)
                            gameboard.board.draw(Variables.game.screen)
                            Variables.player1.update()
                            Variables.player1.draw(Variables.game.screen)
                            pygame.display.flip()
                            boardloop = False

                    elif Variables.Correct is False:
                        print("Game over! Goed antwoord:")
                        # print het goede antwoord op de vraag
                        print(answers(Variables.questionint))
                        print("Hoogste score:")
                        # geeft alleen de hoogste score weer
                        print(interact_database("SELECT MAX(Score) FROM score;")[0][0])
                        # geeft de speler de kans om nog even te kijken als dit in de pygame screen wordt weergegeven
                        # game gaat verder maar de speler mag niet bewegen
                        while boardloop is True:
                            Variables.player1 = gameboard.avatars(1, Variables.player1x, Variables.player1y)
                            gameboard.board.draw(Variables.game.screen)
                            Variables.player1.update()
                            Variables.player1.draw(Variables.game.screen)
                            pygame.display.flip()
                            boardloop = False

            elif event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()
        # vult het scherm zwart
        Variables.game.screen.fill((0, 0, 0))
        # zorgt ervoor dat Number.PlayerScore wordt weergegeven. KNK
        score_display = Variables.Playerscore
        # geeft de score tekst weer
        score_block = score_font.render("score: {}".format(score_display), 1, (255, 255, 255))
        # zegt wat question is
        question_display = question(Variables.questionint)
        # maakt een vakje voor question
        question_block = font.render(question_display, 1, (255, 255, 255))
        question_rect = question_block.get_rect(center=(640, 300))

        poss_display = possibilities(Variables.questionint)
        poss_block = font.render(poss_display, 1, (255, 255, 255))
        poss_rect = poss_block.get_rect(center=(640, 350))

        hi_display = highscore
        hi_block = font.render(hi_display, 1, (255, 255, 255))
        hi_rect = hi_block.get_rect(center=(640, 250))
        Variables.game.screen.blit(hi_block, hi_rect)
        '''
        GameTimer()
        timer_display = "Tijd over: {}".format(Variables.QuestionTimer)
        timer_block = score_font.render(timer_display, 1, (255, 255, 255))
        timer_rect = timer_block.get_rect(center=(1150, 690))
        Variables.game.screen.blit(timer_block, timer_rect)
        '''
        # geeft question weer
        Variables.game.screen.blit(question_block, question_rect)
        # geeft poss weer
        Variables.game.screen.blit(poss_block, poss_rect)
        # geeft het antwoord weer
        block = font.render(antwoord, 1, (255, 255, 255))
        # positie antwoord
        rect = block.get_rect(center=(640, 400))
        # geeft antwoord weer
        Variables.game.screen.blit(block, rect)
        # geeft de score weer
        Variables.game.screen.blit(score_block, (1400, 16))
        # geeft de hoogste score weer
        # geeft answer weer

        if not Variables.Correct:
            answer_display = answers(Variables.questionint)
            answer_block = font.render(answer_display, 1, (255, 255, 255))
            answer_rect = answer_block.get_rect(center=(640, 450))
            Variables.game.screen.blit(answer_block, answer_rect)

        # flipt de screens zodat deze info zichtbaar wordt
        pygame.display.flip()

    Variables.function = "Menu_return"
    Variables.game.update()
    begin()
