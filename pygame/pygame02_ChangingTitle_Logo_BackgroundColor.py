import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
# screen.get_size() # return (width, height)

# changing background color:
color = (255, 255, 0) # (R, G, B)
screen.fill(color) # fill the entire screen with color
# or color = "yellow"
pygame.display.update() # refresh entire display to show any changes
# display.update(rect_list) -> update a portion or entire display surface
# display.flip() -> replace entire display surface

# change the pygame window title
pygame.display.set_caption('vduczz\'s game') # 

# change the pygame window icon
icon = pygame.image.load('pygame/icon.png')  # load image from a file into a surface object (icon)
pygame.display.set_icon(icon)


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
    pygame.display.update()