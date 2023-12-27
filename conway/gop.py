import copy
import pygame
from pygame import *
import random
import time 


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
CAL = (111,222,178)
WINDOW_HEIGHT = 20
WINDOW_WIDTH = 20
SIZE = 20
BOX = 700



SHADOW = (192, 192, 192)
WHITE = (255, 255, 255)
LIGHTGREEN = (0, 255, 0 )
GREEN = (0, 200, 0 )
BLUE = (0, 0, 128)
LIGHTBLUE= (0, 0, 255)
RED= (200, 0, 0 )
LIGHTRED= (255, 100, 100)
PURPLE = (102, 0, 102)



rows, cols = (SIZE+1, SIZE+1) 
#arr = [[0]*cols]*rows 
arr = [[0 for i in range(cols)] for j in range(rows)] 
#arr[2][2]=1
#arr[3][6]=1
for a in range(0,190):
	x= random.randint(1,SIZE)
	y= random.randint(1,SIZE)
	arr[x][y]=1
 
#print(arr)
parr = [[0 for i in range(cols)] for j in range(rows)] 




def main():
    z=0
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((BOX, BOX))
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        z= z+1
        SCREEN.fill(BLACK)
       

        #drawGrid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 1==1:
                
                # This is the starting point
                    r= pygame.mouse.get_rel()
                    r= event.pos
                    arr[int(r[0]/30)][int(r[1]/30)] = 1
                    #text_surface1 = font.render(str(int(r[0]/30)), True, RED)
                    #text_surface2 = font.render(str(int(r[1]/30)), True, RED)
                    #SCREEN.blit(text_surface1, (r[0],r[1]))
                    #SCREEN.blit(text_surface2, (r[0]-50,r[1]))
                    
        drawGrid()
        text_surface = font.render("N= "+str(z), True, RED)
        SCREEN.blit(text_surface, (2,2))
        #####
        #text_surface = font.render(str(r[0],r[1]), True, RED)
        #SCREEN.blit(text_surface, (r[0],r[1]))
        
        pygame.display.update()
        time.sleep(0.1)


def drawGrid():
    blockSize = 30 #Set the size of the grid block
    for x in range(SIZE):
        for y in range(SIZE):
            l = arr[x][y]
            if l== 0:
            	col = BLACK
            elif l==1:
            	col= CAL
            elif l==2:
            	col = RED
            else:
            	col= GREEN 
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, col, rect, 0)
            new(x,y)
    for p in range(SIZE):
       for q in range (SIZE):
            if arr[p][q]==parr[p][q] and arr[p][q]>0:
            	arr[p][q]= arr[p][q]+1
            else:
                arr[p][q]= parr[p][q]


def new(x,y):
	
	if x==0 or y==0:
		return ;
	i=0
	
	
	
	if arr[x-1][y-1]!=0:
		i = i + 1; 
	if arr[x][y-1]!=0:
		i = i + 1; 
	if arr[x+1][y-1]!=0:
		i = i + 1; 
	if arr[x-1][y]!=0:
		i = i + 1; 
	if arr[x+1][y]!=0:
		i = i + 1; 
	if arr[x-1][y+1]!=0:
		i = i + 1; 
	if arr[x][y+1]!=0:
		i = i + 1; 
	if arr[x+1][y+1]!=0:
		i = i + 1; 
	
				
	if i <2 and arr[x][y]!= 0:
		parr[x][y]= 0
		n=2
	elif i>3 and arr[x][y]!= 0:
		parr[x][y]=0
	elif i==3 and arr[x][y]==0:
		parr[x][y]= 1
	else:
		parr[x][y]= arr[x][y]
		



main()