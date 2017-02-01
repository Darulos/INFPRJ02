import datetime
import pygame

nowout = datetime.datetime.now()
nowout2 = datetime.time(nowout.hour, nowout.minute, nowout.second)

tout = str(nowout2)
(hout, mout, sout) = tout.split(':')
resultout = int(hout) * 3600 + int(mout) * 60 + int(sout)

timer = resultout + 50

class Timer:
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font

    def timerdraw(self, screen):
        now = datetime.datetime.now()
        now2 = datetime.time(now.hour, now.minute, now.second)

        t = str(now2)
        (h, m, s) = t.split(':')
        result = int(h) * 3600 + int(m) * 60 + int(s)

        show = timer - result
        strshow = str(show)
        blitshow = self.font.render(strshow, 1, (255, 255, 255))
        screen.blit(blitshow, (self.width/2, self.height/2))

# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False


# Main program logic
def program():
    width = 640
    height = 480
    size = (width, height)

    # Start PyGame
    pygame.init()

    # Set the resolution
    screen = pygame.display.set_mode(size)

    # Set up the default font
    font = pygame.font.SysFont("consolas", 30)

    # Create entity
    timertest = Timer(width, height, font)

    while not process_events():
        # Update entities

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the entities
        timertest.timerdraw(screen)

        # Flip the screen
        pygame.display.flip()


# Start the program
program()
