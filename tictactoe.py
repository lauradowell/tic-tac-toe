import pygame
import sys
import numpy as np
pygame.init()

WIDTH = 600
HEIGHT = 600 
LINE_WIDTH = 15
#RGB
RED = (255, 0, 0)
BG_COLOUR = (196, 93, 133)
LINE_COLOUR = (181, 78, 117)
BOARD_ROWS= 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOUR = (252, 249, 192)
CROSS_WIDTH = 25
SPACE= 55
CROSS_COLOUR = (66, 66, 66)

screen = pygame.display.set_mode(  (WIDTH, HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOUR)
#board

board = np.zeros((BOARD_ROWS, BOARD_COLS))
#print(board)

#pygame.draw.line(screen, RED, (10, 10), (300, 300), 10)

def draw_lines():
    #1st horizontal line
    pygame.draw.line( screen, LINE_COLOUR, (0, 200), (600, 200), LINE_WIDTH)
    #2nd horizontal
    pygame.draw.line( screen, LINE_COLOUR, (0, 400), (600, 400), LINE_WIDTH)
    #1st vertical
    pygame.draw.line( screen, LINE_COLOUR, (200, 0), (200, 600), LINE_WIDTH)
    #2nd vertical
    pygame.draw.line( screen, LINE_COLOUR, (400, 0), (400, 600), LINE_WIDTH)
    
def draw_figures():
    for row in range (BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board [row][col] == 1:
                pygame.draw.circle ( screen , CIRCLE_COLOUR, (int ( col * 200 + 100), int ( row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board [row][col] == 2:
                 pygame.draw.line (screen, CROSS_COLOUR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col *200 +200- SPACE, row * 200 + SPACE), CROSS_WIDTH   )
                 pygame.draw.line(screen, CROSS_COLOUR, (col*200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board [row] [col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

     
draw_lines()

player = 1 
#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX= event.pos[0] #x
            mouseY= event.pos[1] #y
    
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
           
            
            if available_square (clicked_row, clicked_col) :
                if player == 1:
                     mark_square (clicked_row, clicked_col, 1)
                     player=2

                elif player == 2:
                    mark_square (clicked_row, clicked_col, 2)
                    player= 1
                
                draw_figures()
                

    pygame.display.update()
