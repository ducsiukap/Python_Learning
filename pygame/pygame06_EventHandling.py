import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))

player = pygame.image.load('pygame/player.png')
x, y = 268, 500
X_change, Y_change = 0, 0
screen.blit(player, (x, y))
pygame.display.flip()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # PRESS KEYBOARD EVENT
        # pygame.KEYDOWNT, pygame.KEYUP -> event.type
        # pygame.K_character -> event.key 
        # where character is any key on keyboard
        elif event.type == pygame.KEYDOWN:
            print('key pressed!')
            # if press a or LEFT
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                X_change = -0.1
            # if press d or RIGHT
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                X_change = 0.1
            # if press w or UP
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                Y_change = -0.1
            # if press s or DOWN
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                Y_change = 0.1
            # other key
            else: print(event.key) # ascii
        elif event.type == pygame.KEYUP:
            print('key has been released!')
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                X_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Y_change = 0
    
        # MOUSE EVENT
        # pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN -> event.type
        # event.button = 1 -> left mouse click
        #              = 2 -> wheel press
        #              = 3 -> right mouse click
        #              = 4 -> scroll up
        #              = 5 -> scroll down
        # event.pos -> (x, y)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('left mouse click')
            elif event.button == 2:
                print('wheel button pressed')
            elif event.button == 3:
                print('right mouse click')
            elif event.button == 4:
                print('scroll up')
            elif event.button == 5:
                print('scroll down')
        
        # pygame.MOUSEMOTTION -> event.type
        elif event.type == pygame.MOUSEMOTION:
            # event.buttons -> (left press, wheel press, right press)
            buttons = event.buttons 
            # print(f'left mouse press: {buttons[0]}')
            # print(f'wheel press: {buttons[1]}')
            # print(f'right mouse press: {buttons[2]}')

            # event.pos -> position of mouse (x, y)
            if (buttons[0]): # press left mouse and move
                #event.rel -> represents the relative position to the previous position
                # event.rel -> (x_cur - x_prev, y_cur - y_prev)
                rel = event.rel
                x += rel[0]
                y += rel[1]
                
    # update position when press key
    x += X_change
    x = max(x, 0)
    x = min(x, 535)
    y += Y_change
    y = max(0, y)
    y = min(y, 535)
    # update screen
    screen.fill('black')
    screen.blit(player, (x, y))
    pygame.display.flip()
