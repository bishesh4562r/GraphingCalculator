import pygame
import pygame.font
import pygame_textinput
import math
import numpy as np
import threading
import time


pygame.init()
screen = pygame.display.set_mode((1500,720))
#DEFAULTS:
x_left,x_right=-10,10
y_left,y_right=-5,5

origin = (1000.5,360.5)
borders=(500,720)
clock=pygame.time.Clock()
running = True
scale=100
num_font = pygame.font.SysFont("Arial",int(12*100/scale))
equation_font = pygame.font.Font(None,32)
text_color = (255, 255, 255)


curves =[['blue','y=math.sin(1/x)'],['red','y=math.exp(x)'],['black','y=math.sqrt(1-x**2)'],['black','y=-math.sqrt(1-x**2)']]
xpts=[]
i=-50
while i<50:
    xpts.append(i)
    i=round(np.add(i,0.01),2)
    


def draw_text(text,font,text_col,pos):
    img = font.render(text,True,text_col)
    screen.blit(img,pos)
def transform(scale,X,Y):
    if scale*X+origin[0]>=borders[0]:
        return (scale*X+origin[0],-scale*Y+origin[1])
     
def transform_distance(scale,r):
    return scale*r


    
 

def naxis(s,e,x,n):
    if x:
        for each in np.arange(s,e,step=n*scale):
            position_number=(each,origin[1]-scale/2)
            number=int((each-s)/scale)
            pygame.draw.line(screen,'black',(each,origin[1]+scale/4),(each,origin[1]-scale/4))
            draw_text(str(number),num_font,'black',position_number)
    else:
        for each in np.arange(s,e,step=n*scale):
            position_number=(origin[0]-scale/2,each)
            number=-int((each-s)/scale)
            pygame.draw.line(screen,'black',(origin[0]+scale/4,each),(origin[0]-scale/4,each))
            draw_text(str(number),num_font,'black',position_number)




while running:

    
    screen.fill('white')
    #bordering for input
    pygame.draw.line(screen,'black',(borders[0],0),(borders[0],720))
    pygame.draw.circle(screen,'blue',transform(scale,0,0),transform_distance(scale,0.1))
    #yaxis
    pygame.draw.line(screen,'black',(origin[0],720),(origin[0],0))
    #xaxis
    pygame.draw.line(screen,'black',(1500,origin[1]),(500,origin[1]))
    #numbering the  x axis
    naxis(origin[0],1500,True,1)
    naxis(origin[0],500,True,-1)
    #numbering the y axis
    naxis(origin[1],720,False,1)
    naxis(origin[1],0,False,-1)




    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEWHEEL:
            if scale<20:
                scale=20
            elif scale>500:
                scale = 500
            else:
                scale+=float(event.y)

    
    for entry in curves:
        color=entry[0]
        function=entry[1]
        for x in xpts:
            try:
                exec(function)

                pt=transform(scale,x,y)
                x+=0.01
                exec(function)
                pt_2=transform(scale,x,y)
                pygame.draw.line(screen,color,pt,pt_2)
                
            except Exception as e:
                if x==-1:
                    print(e)
                continue   
        
        

        
    

    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()




