import pygame
import sys
import random
pygame.init()

screen = pygame.display.set_mode((650, 650))
pygame.display.set_icon(pygame.image.load('pygame/vietnam.png'))
pygame.display.set_caption('pygame custom event')
bg_color = 'black'


# create a event:

# syntax1: event_name = pygame.event.Event(pygame.USEREVENT + event_count)
# publish: pygame.event.post(event_name)
# check meet event: for event in pygame.event.get(): if event.type == event_name.type
event_count = 1
EXIT_GAME = pygame.event.Event(pygame.USEREVENT + event_count) # syntax1
event_count += 1

# syntax2: event_name = pygame.USEREVENT + event_count
# publish: pygame.event.post(pygame.event.Event(event_name))
# check: for event in pygame.event.get(): if event.type == event_name
CHANGE_POS = pygame.USEREVENT + event_count # syntax2
event_count += 1
change_bg_color = pygame.USEREVENT + event_count
event_count += 1
# post change_bg_color event at end of event queue every 500ms
pygame.time.set_timer(change_bg_color, 500) # for syntax2

# random an Integer in [start, end]
def rand_int(start, end):
    return random.randint(start, end)

# load a pumpkin
pump = pygame.image.load('pygame/pumpkin.png')
pump = pygame.transform.scale(pump, (64, 64))
# size of img
pump_size = pump.get_size()
# draw pumpkin
pumpX, pumpY = rand_int(0, 650 - pump_size[0]), rand_int(0, 650 - pump_size[1])
screen.blit(pump, (pumpX, pumpY))
pygame.display.flip()

# check if mouse pointer points to pumpkin
def mouse_at_pumpkin(x, y):
    if x < pumpX or x > (pumpX + pump.get_size()[0]):
        return False
    if y < pumpY or y > (pumpY + pump.get_size()[1]):
        return False
    return True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == EXIT_GAME.type:
            pygame.quit()
            sys.exit()

        # press esc to quit game:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # push userevent at end of event queue
                # syntax1
                pygame.event.post(EXIT_GAME)

        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = event.pos
            if (mouse_at_pumpkin(mouseX, mouseY)):
                # syntax2
                pygame.event.post(pygame.event.Event(CHANGE_POS))

        # change position of pumpkin 
        # dont allow user point to pumpkin :))
        if event.type == CHANGE_POS:
            x = rand_int(0, 650 - pump_size[0])
            while x == pumpX:
                x = rand_int(0, 650 - pump_size[0])
            pumpX = x
            y = rand_int(0, 650 - pump_size[1])
            while y == pumpY:
                y = rand_int(0, 650 - pump_size[1])
            pumpY = y

        # change bg color every 500ms
        if event.type == change_bg_color:
            bg_color = 'black' if bg_color == 'gray' else 'gray'

    screen.fill(bg_color)
    screen.blit(pump, (pumpX, pumpY))
    pygame.display.flip()

                    