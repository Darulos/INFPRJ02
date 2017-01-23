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
                if i > 5:
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

