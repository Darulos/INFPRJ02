import random
import pygame


class board:
    def draw(screen):
        #setting the standard width of a square
        w = 48
        #setting values for the x,y axis
        x,y = 0,0
        #loop for the y axis of the grid
        for i in range(15):
            #loop for the x axis of the grid
            for j in range(8):
                #the board is 15 high but is 8 wide untill it gets to the top 5 and since its drawn from top to bottom
                # the first 5 rows are only 4 wide and need a special if
                if i > 4:
                    #draws a black square behind every coloured square to give it better contrast
                    pygame.draw.rect(screen, (0,0,0), (x, y, w, w))
                    #for loop that draws 42 lines in slighty darker colour to create a gradient square
                    for k in range(42):
                        if j == 0 or j == 1:
                            color = (255-k,0,0)
                            pygame.draw.line(screen, color, (x+k+3, y+3), (x+k+3, y+45))
                        elif j == 2 or j == 3:
                            color = (0,255-k,0)
                            pygame.draw.line(screen, color, (x+k+3, y+3), (x+k+3, y+45))
                        elif j == 4 or j == 5:
                            color = (255-k,255-k,0)
                            pygame.draw.line(screen, color, (x+k+3, y+3), (x+k+3, y+45))
                        elif j == 6 or j == 7:
                            color = (0,0,255-k)
                            pygame.draw.line(screen, color, (x+k+3, y+3), (x+k+3, y+45))
                else:
                    #draws a black square behind every coloured square to give it better contrast but because these rows
                    #are only 4 wide they need half the black squares
                    if j % 2 ==0:
                        pygame.draw.rect(screen, (0,0,0), (x+24, y, w,w))
                    #for loop that draws 42 lines in slighty darker colour to create a gradient square but because these
                    #rows are only 4 wide they need half the coloured squares therefore they only draw when j is even
                    for k in range(42):
                        if j == 0:
                            color = (0,255-k,0)
                            pygame.draw.line(screen, color, (x+k+27, y+3), (x+k+27, y+45))
                        elif j == 2:
                            color = (255-k,255-k,0)
                            pygame.draw.line(screen, color, (x+k+27, y+3), (x+k+27, y+45))
                        elif j == 4:
                            color = (0,0,255-k)
                            pygame.draw.line(screen, color, (x+k+27, y+3), (x+k+27, y+45))
                        elif j == 6:
                            color = (255-k,0,0)
                            pygame.draw.line(screen, color, (x+k+27, y+3), (x+k+27, y+45))
                #increase the value of the x axis by w so that the next square thats created is to the right of the
                #previous one and not on top
                x = x + w
            #increase the value of the y axis by w so that the next square thats created is below the previous and not
            #on top
            y = y + w
            #reset the value of the x axis so that the next row starts at same spot as the previous row
            x = 0



#class to keep track of the different avatars and their positions
#id dfferentiates between the different avatars and x,y are the coordinates
class avatars:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    #function to update the the position of a a player
    def update(self):
        #loops through the button presses to check what direction the player wants to go to
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #checks if the left arrow key has been pressed and changes the x value to move the avatar
                if event.key == pygame.K_LEFT:
                    #throw dice
                    if self.y < 240:
                        self.x -= 96 #* random.randint(1,3)
                        #if the avatar is moved outside the bord it gets placed on the right of the board because its
                        #supposed to be circular
                        if self.x < 24:
                            self.x += 384
                    else:
                        self.x -= 48 #* random.randint(1,3)#* dice throw
                        #if the avatar is moved outside the bord it gets placed on the right of the board because its
                        #supposed to be circular 48 144 240 336
                        if self.x < 24:
                            self.x += 384
                #checks if the right arrow key has been pressed and changes the x value to move the avatar
                elif event.key == pygame.K_RIGHT:
                    #throw dice
                    if self.y < 240:
                        self.x += 96 #* random.randint(1,3)
                        #if the avatar is moved outside the bord it gets placed on the left of the board because its
                        #supposed to be circular
                        if self.x > 360:
                            self.x -= 384
                    else:
                        self.x += 48 #* random.randint(1,3)#* dice throw
                        #if the avatar is moved outside the bord it gets placed on the left of the board because its
                        #supposed to be circular
                        if self.x > 360:
                            self.x -= 384
                #checks if the up arrow key has been pressed and changes the y value to move the avatar
                elif event.key == pygame.K_UP:
                    tempy = self.y
                    #throw dice
                    self.y -= 48 #* random.randint(1,3)#* dice throw
                    if tempy > 216 and self.y <= 216:
                        if self.x == 24:
                            self.x += 24
                        elif self.x == 72:
                            self.x -= 24
                        elif self.x == 120:
                            self.x += 24
                        elif self.x == 168:
                            self.x -= 24
                        elif self.x == 216:
                            self.x += 24
                        elif self.x == 264:
                            self.x -= 24
                        elif self.x == 312:
                            self.x += 24
                        elif self.x == 360:
                            self.x -= 24
                        #if the avatar is moved above the board it gets placed on top of the board and the player wins
                    if self.y < 24:
                        self.y = 24
                        #winnaar!!!!!!!
                #checks if the down arrow key has been pressed and changes the y value to move the avatar
                elif event.key == pygame.K_DOWN:
                    tempy = self.y
                    #throw dice
                    self.y += 48 #* random.randint(1,3)#* dice throw
                    if tempy <= 216 and self.y > 216:
                        if self.x == 48:
                            self.x += 24
                        elif self.x == 144:
                            self.x += 24
                        elif self.x == 240:
                            self.x += 24
                        elif self.x == 336:
                            self.x += 24
                    #if the avatar is moved underneath the board it gets placed on at the bottom of the board
                    if self.y > 696:
                        self.y = 696

    def draw(self, screen):
        #load and draw the avatars(right now only 1 is drawn)
        img=pygame.image.load("1.png")
        rect = img.get_rect(center=(player1.x, player1.y))
        screen.blit(img,rect)



player1 = avatars(1, 48, 24)
screen = pygame.display.set_mode((1280, 720))

while True:
    screen.fill((0,0,0))
    board.draw(screen)
    player1.update()
    player1.draw(screen)
    pygame.display.flip()
