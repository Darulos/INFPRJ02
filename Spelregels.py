import Variables
import pygame

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
