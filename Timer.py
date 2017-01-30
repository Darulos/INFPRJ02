import pygame, sys
import Variables

pygame.init()

size = (480 ,360)
screen = pygame.display.set_mode(size)
score_font = pygame.font.Font(None, 45)
clock = pygame.time.Clock()
clock.tick(60)
black = 0,0,0

class Gametimer:
    def __init__(self, time, counter):
        self.Time = time
        self.Counter = counter

    def Subtract(self):
        if self.Time > 0:
            if self.Counter%2000 == 0:
                self.Time-=1
                self.Counter = 0
        else:
            self.Time = 10

    def Count(self):
        self.Counter+=1

Timer = Gametimer(Variables.QuestionTimer, 0)

def TimerDraw():
    Timer.Subtract()
    Timer.Count()
    timer_display = "Tijd over: {}".format(Timer.Time)
    timer_block = score_font.render(timer_display, 1, (255, 255, 255))
    timer_rect = timer_block.get_rect(center=(240, 180))
    screen.blit(timer_block, timer_rect)

while True:
    if Timer.Time > 0:
        screen.fill(black)
        TimerDraw()
        # Timer.Subtract()
        # Timer.Count()
        # timer_display = "Tijd over: {}".format(Timer.Time)
        # timer_block = score_font.render(timer_display, 1, (255, 255, 255))
        # timer_rect = timer_block.get_rect(center=(240, 180))
        # screen.blit(timer_block, timer_rect)
        pygame.display.flip()
    else:
        sys.exit()

