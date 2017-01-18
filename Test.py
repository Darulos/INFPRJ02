import pygame

class TextBox: #create class for textspace
    def __init__(self, x, y, width, height): #box dimensions
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen): #draw function for rectangle
        pygame.draw.rect(screen, (0, 0, 0), (int(self.x), int(self.y), int(self.width-self.x), int(self.height-self.y)))

class Border: #create class for textspace
    def __init__(self, x, y, width, height): #box dimensions
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen): #draw function for rectangle
        pygame.draw.rect(screen, (255, 255, 255), (int(self.x), int(self.y), int(self.width-self.x), int(self.height-self.y)))

#handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False

#main program logic
def program():

    width = 480
    height = 620
    size = (width, height)

    # Start PyGame
    pygame.init()

    # Set the resolution
    screen = pygame.display.set_mode(size)

    # Create the players
    border = Border(width-152, height-302, width, height)
    box = TextBox(width-150, height-300, width, height)

    while not process_events():
       #UPDATE HERE
        # Clear the screen
        screen.fill((0, 0, 0))

        #draw box
        border.draw(screen)
        box.draw(screen)

        #draw text
        font = pygame.font.Font(None, 25)
        text = font.render("TESTTESTTESTlajsfljasldflasjfljals", True, (255, 255, 255))
        text_rect = text.get_rect(center=(box.x+75, box.y+100))
        screen.blit(text, text_rect)
        #flip screen
        pygame.display.flip()

# Start the program
program()
