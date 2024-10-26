import math
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600)) # surface

color = (255, 255, 255) # white
screen.fill(color)
pygame.display.update()

pygame.display.set_caption('vduczz\'s game') 
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# syntax: 
# pygame.draw.shape()
def drawRect(): # rectangle
    # pygame.draw.rect(surface, color, (x, y, width, height), width) 
    # width = 0 (default) for solid, else for line
    return pygame.draw.rect(screen, 'green', (200, 200, 200, 200)) # solid
def drawCircle():
    # pygame.draw.circle(surface, color, (x, y), radius, width)
    return pygame.draw.circle(screen, 'red', (300, 300), 200, 2) # line
def drawTriangle():
    # pygame.draw.polygon(surface, color, points_list, width)
    return pygame.draw.polygon(screen, 'blue', [(200, 200), (200, 400), (400, 200)])
def drawEllipse():
    # pygame.draw.ellipse(screen, color, (x, y, width, height), width)
    return pygame.draw.ellipse(screen, 'purple', (200, 200, 200, 200))
def drawArc():
    # pygame.draw.arc(surface, color, (x, y, width, height), start_angle, end_angle, width) 
    # stard_angle, end_angle -> radian
    return pygame.draw.arc(screen, 'pink', (200, 200, 200, 200), 0, math.pi, 2)
def drawLine():
    # pygame.draw.line(surface, color, start_pos, end_pos, width)
    return pygame.draw.line(screen, 'black', (200, 200), (400, 400), 3)
def drawLines():
    # pygame.draw.lines(surface, color, closed, points_list, width)
    # closed: connect first point and last point ? -> True/False
    return pygame.draw.lines(screen, 'red', True, [(200, 200), (300, 300), (200, 400), (300, 500)], 2)

def drawShapes(rectNo:int):
    rect = None
    if rectNo == 0:
        rect = drawRect()
    elif rectNo == 1:
        rect = drawCircle()
    elif rectNo == 2:
        rect = drawTriangle()
    elif rectNo == 3:
        rect = drawEllipse()
    elif rectNo == 4:
        rect = drawArc()
    elif rectNo == 5:
        rect = drawLine()
    else:
        rect = drawLines()
    pygame.display.update(rect)


rect = 0
run = True
position = []
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # to run this part, let comment #reset_display and #draw_a_shape part below
        elif event.type == MOUSEBUTTONDOWN:
            position.append(event.pos) # get mouse position

    # reset display
    color = (255, 255, 255) # white
    screen.fill(color)
    pygame.display.flip()
    
    # draw a shape
    drawShapes(rect)
    rect = (rect + 1) % 7

    # draw circle at any mouse click position
    for x, y in position:
        pygame.display.update(
            pygame.draw.rect(screen, 'yellow', (x, y, 200, 200), 3, 3)
        )
    pygame.time.delay(500)
