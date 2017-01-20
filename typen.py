import pygame
import Questions
import Score
import sys
import Variables


def typen():
    # # start pygame en creeer een scherm
    # pygame.init()
    # screen = pygame.display.set_mode((480, 620))
    # variable om het getypte antwoord op te slaan
    loop = True
    antwoord = ""
    # alvast font vaststellen
    font = pygame.font.Font(None, 30)
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

                # maakt antwoord 1 lengte korter wanneer backspace wordt aangetikt
                elif event.key == pygame.K_BACKSPACE:
                    antwoord = antwoord[:-1]

                # checkt gegeven antwoord met het answer in de database en haalt antwoord leeg
                elif event.key == pygame.K_RETURN:
                    # if antwoord in answer, display correct, score +=
                    # haalt antwoord op uit database
                    if antwoord in Questions.answers(Variables.questionint):
                        antwoord = ""
                        print("Goed zo jongen")
                        Score.upload_score(int(Score.interact_database("SELECT MAX(Score) FROM score;", False)[0][0]), Variables.Player_Name)
                        Questions.begin()
                    else:
                        print("Game over! Goed antwoord:")
                        print(Questions.answers(Variables.questionint))
                        print("Alle scores:")
                        print(Score.download_score())
                        print(Score.download_highscore())
                        loop = False

            elif event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()
        Variables.game.screen.fill ((0, 0, 0))
        score_display = Score.download_highscore()
        score_block = font.render("score: {}".format(score_display), 1, (255, 255, 255))
        block = font.render(antwoord, 1, (255, 255, 255))
        rect = block.get_rect(center=(Variables.game.width/2, Variables.game.height/2))
        Variables.game.screen.blit(block, rect)
        Variables.game.screen.blit(score_block, (16, 16))
        pygame.display.flip()

    Variables.function = "Menu_return"
    Variables.game.update()

        #     # eindig de loop/het programma
        #     elif event.type is pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        # screen.fill ((0, 0, 0))
        # score_display = Score.download_highscore()
        # score_block = font.render("score: {}".format(score_display), 1, (255, 255, 255))
        # block = font.render(antwoord, 1, (255, 255, 255))
        # rect = block.get_rect(center=(240, 310))
        # screen.blit(block, rect)
        # screen.blit(score_block, (16, 16))
        # pygame.display.flip()

def start():
    # haalt antwoord op uit database
    Variables.Player_Name = input("Wat is uw naam?")
    Score.interact_database("DELETE FROM Score;", True,)
    Score.interact_database("INSERT INTO Score VALUES(%s, %s)", True, (Variables.Player_Name, 0))

    Questions.begin()
    typen()
