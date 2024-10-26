import pygame 

# initialize all imported module
pygame.init()

# create a window to display
screen_width = 720
screen_height = 720
pygame.display.set_mode((screen_width, screen_height)) 
# pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE) # allowing resizing windows

# game loop
run = True # flag
while run: 

    # pygame.event.get() -> get the list of events from the event queue.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

