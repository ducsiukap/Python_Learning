import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))


color = (255, 255, 0) 
screen.fill(color)
pygame.display.update()

pygame.display.set_caption('vduczz\'s game') 
icon = pygame.image.load('icon.png')
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
    # python.time 
    # delay screen
    pygame.time.delay(500) # delay 2s 
    # pygame.time.wait(2000)

    print(f'time executed: {pygame.time.get_ticks()}') # tra ve tgian da chay ctr

    clock = pygame.time.Clock() # create a clock to keep track of time
    clock.tick(10) # maximum fps is 10
    print(f'time between two tick() is {clock.get_time()}') # time between 2 tick 1000/10 -> 100ms 
    print(f'fps is {clock.get_fps()}') # return fps 
    print('------------------')