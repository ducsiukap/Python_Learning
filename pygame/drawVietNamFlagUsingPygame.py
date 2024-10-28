import pygame
from math import *
pygame.init()


screen = pygame.display.set_mode((801, 601), pygame.RESIZABLE)
screen.fill((255, 255, 255)) # white

pygame.display.set_caption('Viet Nam top 1 server Trai Dat :))')
pygame.display.set_icon(pygame.image.load('vietnam.png'))
pygame.display.flip()

 # ve khung
x, y = 0, 0
pygame.display.update(
    pygame.draw.rect(screen, 'red', (x, y, 1, 1), 1)
)
x += 1
while (x != 0) or (y != 0):
    pygame.time.delay(1)
    pygame.display.update(
        pygame.draw.rect(screen, 'red', (x, y, 1, 1), 10)
    )
    if y == 0: 
        x += 1
        if (x == 801):
            x = 800
            y += 1
    elif y == 600: 
        x -= 1
        if (x == -1):
            x = 0
            y -= 1
    elif x == 800:
        y += 1
        if (y == 601):
            x -= 1
            y = 600
    else:
        y -= 1
    
# draw background
x1, y1 = 1, 1
x2, y2 = 1, 1
yJump = 15
xJump = 20
while x1 < 800:
    pygame.display.update(
        pygame.draw.rect(screen, 'red', (x1, y1, xJump, yJump))
    )
    pygame.display.update(
        pygame.draw.rect(screen, 'red', (x2, y2, xJump, yJump))
    )
    y1 += yJump
    if (y1 >= 600):
        x1 += xJump
        y1 = y2 + yJump
        
    x2 += xJump
    if (x2 >= 800):
        x2 = x1
        y2 = y1
    # print(x1,y1, x2, y2)
    pygame.time.delay(5)

pygame.time.delay(1000)

R = 120
phi = [13*pi/10, pi/2, 17*pi/10, 9*pi/10, pi/10]

while R > 0:
    points = []
    for p in phi:
        points.append((400 + R * cos(p), 300 - R * sin(p)))
    pygame.display.update(
        pygame.draw.lines(screen, 'yellow', True, points, 3)
    )
    R -= 1
    # print(points)
    pygame.time.delay(20)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
