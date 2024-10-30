import pygame
import time
pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
pygame.display.flip()

# create font type
Aptos = pygame.font.SysFont('Aptos', 30)

# 
input_text = ''

# create textbox
text_box = pygame.Rect(50, 200, 400, 50)
active = False
color_active = 'lightskyblue3'
color_nonactive = 'chartreuse4'
box_color = color_nonactive
# check mouse pointer in text_box:
def in_box(x, y):
    if x < text_box[0] or x > text_box[0] + text_box[2]:
        return False
    if y < text_box[1] or y > text_box[1] + text_box[3]:
        return False
    return True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.QUIT)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if in_box(event.pos[0], event.pos[1]): # or
                # if text_box.collidepoint(event.pos):
                    active = True
                else: 
                    active = False
        
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                if len(input_text) > 0:
                    input_text = input_text[:-1] # delete last character
            elif event.key == pygame.K_RETURN: # enter
                active = False
            else:
                input_text += event.unicode

    # render text 
    text_sur = Aptos.render(input_text, True, 'white')
    text_rect = text_sur.get_rect()
    text_rect.topleft = (text_box[0] + 10, text_box[1] + 15)
    text_rect.right = min(text_box[0] + text_box[2] - 10, text_rect.right)

    # check active
    if active == True:
        box_color = color_active
        # display cursor every 5ms
    else: 
        box_color = color_nonactive

    # draw text_box
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, box_color, text_box, border_radius=5)
    screen.blit(text_sur, text_rect)

    # draw cursor every 0.5 sec
    if time.time() % 1 > 0.5 and active:
        cursor = pygame.Rect(text_rect.right + 1, text_rect.top, 1, text_rect.height)
        pygame.draw.rect(screen, 'black', cursor)
    
    pygame.display.flip()