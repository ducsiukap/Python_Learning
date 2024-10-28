import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))


color = (255, 255, 0) 
screen.fill(color)
pygame.display.update()

pygame.display.set_caption('vduczz\'s game') 
icon = pygame.image.load('pygame/icon.png')
pygame.display.set_icon(icon)

''' 1280x720 screen:
(0, 0)                                       (1280, 0)
    O------------------------------------------> x
    |
    |           .(x0, y0)
    |       
    | 
    y (0, 720) 
'''
carImg = pygame.image.load('pygame/car.png')
# 64px img -> 64x64 pixels
x, y = 608, 720 - 64
def car():
    # blit: copy the pixels of one surface to another
    screen.blit(carImg, (x, y))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # change screen color =)))))))
    if color == "yellow": 
        color = "red"
    elif color == "red":
        color = "green"
    else: color = "yellow"
    screen.fill(color)
    x = (x + 5) % 1280 # change position of car 
    car()
    pygame.display.update()