import pygame
import random
from math import *
import numpy as np
# Pygame initialization
pygame.init()

# Constants
SCREEN_SIZE = (700, 700)
# how many points ? 
global p 


#only change this section
p = int(1);### which to which coordinate (CHANGE1 )
p =100

NUMBER_OF_POINTS= 100000
def provide_fun(z):
    #return np.sin(z)-1
    #return z**50 - 1
    #return z**3-1; 
    #return z**6 + z**3 - 1
    return (z-1)*(z-2)*(z-3)
    return z**3-1



COORDINATE_RANGE = p
# that means -50 to +50 coordinate
CELL_SIZE =  SCREEN_SIZE[0] / (2 * p ); 

CO_CENTER_X = SCREEN_SIZE[0] // 2
CO_CENTER_Y = SCREEN_SIZE[1] // 2

CO_X= 0
CO_Y= 0
def graph_to_pygame_corordinate(x,y):
    x = x - CO_X
    y = y - CO_Y
    #coord = (x * CELL_SIZE + SCREEN_SIZE[0] // 2, -y * CELL_SIZE + SCREEN_SIZE[1] // 2)
    coord = (x * CELL_SIZE + CO_CENTER_X, -y * CELL_SIZE + CO_CENTER_Y)
    return coord;

#def pygame_to_graph_coordinate(x,y):
#   coord = ( (x / CELL_SIZE) -CO_CENTER_X //  CELL_SIZE, - (y / CELL_SIZE) + CO_CENTER_Y // ( CELL_SIZE))
#    return coord;

#print(graph_to_pygame_corordinate(0,0))
#print(graph_to_pygame_corordinate(0,-2))
#print(pygame_to_graph_coordinate(350,350))
#print(pygame_to_graph_coordinate(700,700))
#print(pygame_to_graph_coordinate(350,700))

def coordinate_to_color(x, y,b=100):
    p =COORDINATE_RANGE
    #print(p)
    #p =  30
    #p = 2
    #p = COORDINATE_RANGE
    # Normalize x and y to be in the range of 0 to 1
    normalized_x = (x + p) / (2 * p)
    normalized_y = (y + p) / (2 * p)

    # Map normalized coordinates to RGB values (0-255)
    #r = int(normalized_x * 255)
    #if r >255:
    #   r = 255
    #elif r<0 :
    #    r =0
    #g = int(normalized_y * 255)
    #if g > 255:
    #    g = 255
    #elif g<0:
    #    g= 0
     # Constant blue value
    r = min(max(int(normalized_x * 255), 0), 255)
    g = min(max(int(normalized_y * 255), 0), 255)
    return r, g, b  # Return the RGB color tuple



# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create a window
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
step = 1
points = []  # Store points' initial positions



def display_text(screen, text, position, font_size=24, color=(255, 0, 0)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
def display_multiline_text(screen, text, position, font_size=24, color=(255, 0, 0)):
    font = pygame.font.Font(None, font_size)
    lines = text.split("\n")  # Split text into lines based on newline character

    # Render each line of text
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_position = (position[0], position[1] + i * font_size)  # Adjust Y position for each line
        screen.blit(text_surface, text_position)


def draw_c(x, y, radius):
    # Since each cell in the grid is CELL_SIZE, simply multiply the coordinate by CELL_SIZE
    # and add the screen center offset to get the correct pixel position
    #coord = (x * CELL_SIZE + SCREEN_SIZE[0] // 2, -y * CELL_SIZE + SCREEN_SIZE[1] // 2)
    coord =graph_to_pygame_corordinate (x,y) 
    pygame.draw.circle(screen, BLACK, coord, radius)
def draw_with_color(x, y, radius):
    #coord = (x * CELL_SIZE + SCREEN_SIZE[0] // 2, -y * CELL_SIZE + SCREEN_SIZE[1] // 2)
    coord =graph_to_pygame_corordinate (x,y) 
    pygame.draw.circle(screen, coordinate_to_color(x,y), coord, radius)
def draw_with_colorr_back_to_inital(x, y,p,q, radius):
    #coord = (x * CELL_SIZE + SCREEN_SIZE[0] // 2, -y * CELL_SIZE + SCREEN_SIZE[1] // 2)
    coord =graph_to_pygame_corordinate (x,y) 
    pygame.draw.circle(screen, coordinate_to_color(p,q), coord, radius)


def derive(z):
    eps= 0.001
    d=  (provide_fun(z+eps)-provide_fun(z))/eps

    
    if abs(d) < eps:
        return eps
    else:
        return d

def newrph(p, q):
    z = complex(p, q)
    if z == 0:  # Check if z is zero to avoid division by zero
        return z
    else:
        # here will be the equation
        #result = z - (z**5 - 16) / (5 * z**4)
       
        #result = z - (z**3 - 1) / (3 * z**2)
        # a=0
        #b=-2
        #c= 3
        #result = z - (z**3 - (a+b+c)* z**2 + (a*b+b*c+c*a)* z +a*b*c ) / (3*z**2 - 2*(a+b+c)* z + (a*b+b*c+c*a) )
        #result = z - (z**3-1)/  (3*z**2)
        if abs(derive(z)) > 0.01:
            result = z - provide_fun(z) / derive(z)
            return result
        return z

 
for _ in range(NUMBER_OF_POINTS):  # Generate  random points
        COORDINATE_RANGE = COORDINATE_RANGE ; 
        x = random.uniform(-COORDINATE_RANGE, COORDINATE_RANGE)
        y = random.uniform(-COORDINATE_RANGE, COORDINATE_RANGE)
        color = 1; 
        points.append((x, y,x,y))

#points = [(i, j,i,j) for i in range(-50, 50, 2) for j in range(-50, 50, 2)]
#points  = [(6,7,6,7)]
itarate= 0 
m=1
j=0;
#p =0;
reset = 0;


while running:
    screen.fill(WHITE)
    # Inside your main loop, after drawing everything else on the screen:
    text_print= "Press N to next \n"
    text_print = text_print + "Press B to back \n"
    text_print = text_print + "Step : " + str(step) + "\n"
    text_print += "Press q,w to zoom in or out/ \n" 
    text_print += "mouse click to select a point \n"
    text_print += "Press e to center align \n"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            step += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            itarate += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            step -= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset =1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_j:
            j +=10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            CO_CENTER_X = SCREEN_SIZE[0] // 2
            CO_CENTER_Y = SCREEN_SIZE[1] // 2
            CO_X , CO_Y = 0,0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            
            COORDINATE_RANGE +=COORDINATE_RANGE *2
          
            CELL_SIZE =  SCREEN_SIZE[0] / (2 * COORDINATE_RANGE )
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:  
            #if(COORDINATE_RANGE ) >1.99:
            #    COORDINATE_RANGE -=1
            #elif(COORDINATE_RANGE>0.19):
            #    COORDINATE_RANGE -= 0.1
            #el
            #b= SCREEN_SIZE[0]/2 + CO_CENTER_X/CELL_SIZE
            #print (SCREEN_SIZE[0]/2- CO_CENTER_X )
            if(COORDINATE_RANGE>0.00002):
                COORDINATE_RANGE = COORDINATE_RANGE/2;

            

           
            CELL_SIZE =  SCREEN_SIZE[0] / (2 * COORDINATE_RANGE ) 

            #CO_CENTER_X = SCREEN_SIZE[0]/2 - b / CELL_SIZE
        #elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
        #    if p==0:
        #        p=1
        #    elif p==1:
        #        p=0
        #
        if event.type == pygame.MOUSEBUTTONDOWN:
            a ,b  = pygame.mouse.get_pos()

            #CO_X , CO_Y = pygame_to_graph_coordinate(a,b)
            #i,o = graph_to_pygame_corordinate(0,0)
            #CO_X =   a-i
            #CO_Y = o-b
            CO_CENTER_X +=  (SCREEN_SIZE[0]/2) -a 
            CO_CENTER_Y +=  (SCREEN_SIZE[1]/2) -b
            #CO_CENTER_Y = - (SCREEN_SIZE[1] / (2) ) +b

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                CO_CENTER_X -= 100
            if event.key == pygame.K_LEFT:
                CO_CENTER_X += 100
            if event.key == pygame.K_UP:
               CO_CENTER_Y += 100
            if event.key == pygame.K_DOWN:
               CO_CENTER_Y -=100


                
        # Get the mouse coordinates
    #mouse_x, mouse_y = pygame.mouse.get_pos()
    # Convert mouse coordinates to grid coordinates if needed
    # For example:
    #grid_x = (mouse_x - SCREEN_SIZE[0] // 2) / CELL_SIZE
    #grid_y = -(mouse_y - SCREEN_SIZE[1] // 2) / CELL_SIZE
    #    # Append the mouse coordinates to text_print
    #text_print += f"Last Mouse: ({mouse_x}, {mouse_y}) \n"
    #text_print += f"Last Mouse grid at: ({grid_x}, {grid_y}) \n"


    #print("step :")
    #print(step)
    if step == 1:
      
        #print(points)
        #for point in points:
        #    draw_c(point[0], point[1], 3)
        for point in points:
            draw_c(point[0], point[1], 2)

        # Draw x and y axis lines
        #pygame.draw.line(screen, BLACK, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
        #pygame.draw.line(screen, RED, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)
        step = 1
        
    elif step == 2:
        #if p==0:
        
        for point in points:
            draw_c(point[0], point[1], 2)
        #elif p==1:
        #   draw_with_colorr_back_to_inital(point[0], point[1],point[2], point[3], 2)
        #print(p)

        # Draw x and y axis lines
        #pygame.draw.line(screen, RED, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
        #pygame.draw.line(screen, RED, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)
        
        #please disable it 

        if j>0:
            itarate= 1; 
            j = j-1;
            print(j)
        text_print += "Press i to itarate \n"
        text_print += "Press j to itarate +10 time \n"
        text_print += "Press N to assign color \n"
        if  itarate  ==1:
            itarate = 0 ; 
            i = 0; 
            for point in points:

                ita = newrph(point[0],point[1])
                nx = ita.real 
                ny = ita.imag
                points[i] = (nx,ny , point[2],point[3])
                #print(i)
                i+= 1 
            

    elif step ==3:
        #pygame.draw.line(screen, RED, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
        #pygame.draw.line(screen, RED, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)
        text_print += "Press n to make the color back to initial position \n"
        for point in points:
            draw_with_color(point[0], point[1], 2)

    elif step==4:
        #pygame.draw.line(screen, RED, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
        #pygame.draw.line(screen, RED, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)
        for point in points:
            draw_with_colorr_back_to_inital(point[2], point[3],point[0], point[1], 2)
        #print(points)
        text_print += "Press n to reassign \n"    

            
    elif step==5:
        #reset but with ini value 
        reset=1
        if reset==1:
            q=0;
            #point(currentlocaton, original)
            for point in points:
                #points[q] = (point[2],point[3] , point[0],point[1])
                #draw_c(point[0], point[1], 2)
                draw_with_colorr_back_to_inital(point[2],point[3],point[0],point[1], 2)

                q+= 1
                #print(point)
            reset = 0
            #print("reset done")
            #p = 1;
            j =0
            #step = 6
        text_print += "Reassign okay, Press N to initiating \n"
    elif step == 6:
        text_print += "Press i to itarate \n"
        text_print += "Press j to itarate +10 time \n"
        #draw_c(point[2], point[3], 2)
        for point in points:
            draw_with_colorr_back_to_inital(point[2],point[3],point[0],point[1], 2)
        
        # Draw x and y axis lines
        #pygame.draw.line(screen, RED, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
        #pygame.draw.line(screen, RED, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)
        
        #please disable it 

        if j>0:
            itarate= 1; 
            j = j-1;
            print(j)
        
        if  itarate  ==1:
            itarate = 0 ; 
            i = 0; 
            for point in points:

                ita = newrph(point[2],point[3])
                nx = ita.real 
                ny = ita.imag
                points[i] = ( point[0],point[1],nx,ny)
                #print(i)
                i+= 1 
            
          
    pygame.draw.line(screen, RED, graph_to_pygame_corordinate(-10,0), graph_to_pygame_corordinate(+10,0), 2)
    pygame.draw.line(screen, RED, graph_to_pygame_corordinate(0,10), graph_to_pygame_corordinate(0,-10), 2)
                  

    display_multiline_text(screen, text_print, (50, 50) )    
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
