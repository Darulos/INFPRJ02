import pygame

def typen():
    #start pygame en creeer een scherm
    pygame.init()
    screen = pygame.display.set_mode((480, 620))
    #variable om het getypte antwoord op te slaan
    antwoord = ""
    #alvast font vaststellen
    font = pygame.font.Font(None, 30)
    #loop om het programma lopend te houden
    while True:
        #loopt alle events door op zoek naar een van de if's
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #zet de aangetikte letter/hoofdletter in antwoord
                if event.unicode.isalpha():
                    antwoord += event.unicode
                #zet de aangetikte cijfer in antwoord
                elif event.unicode.isdigit():
                    antwoord += event.unicode
                #zet de aangetikte spatie in antwoord
                elif event.key == pygame.K_SPACE:
                    antwoord += " "
                #maakt antwoord 1 lengte korter wanneer backspace wordt aangetikt
                elif event.key == pygame.K_BACKSPACE:
                    antwoord = antwoord[:-1]
                #checkt gegeven antwoord met het answer in de database en haalt antwoord leeg
                elif event.key == pygame.K_RETURN:
                    #if antwoord in answer, display correct, score +=
                    #haalt antwoord op uit database
                    if antwoord in answer(num):
                        antwoord = ""
            #eindig de loop/het programma
            elif event.type == pygame.QUIT:
                return
        screen.fill ((0, 0, 0))
        block = font.render(antwoord, 1, (255, 255, 255))
        rect = block.get_rect(center=(240, 310))
        screen.blit(block, rect)
        pygame.display.flip()

#haalt antwoord op uit database
def answer(number):
    return interact_database("SELECT Answers FROM questions WHERE Question_id = %s", (number,))[0][0]

typen()

