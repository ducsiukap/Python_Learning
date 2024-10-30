import pygame
import sys

pygame.init()
pygame.font.init() # Font module Initialization
# pygame.font.get_init() -> True/False check whether the font has been initialized or not

screen = pygame.display.set_mode((600, 600))

# create a font object: pygame.font.Sysfont('font_name', size)
Aptos = pygame.font.SysFont('Aptos', 30)
Arial = pygame.font.SysFont('Arial', 40)

# render text surface object: font_name.render('string', antialias, color, bgcolor)
mess = Arial.render('Hello World', True, 'yellow', 'red')
# create rectangular object for text surface 
text_rect = mess.get_rect() # (x, y, width, height)
# set position of rectangular object : top, topleft, topright, center, bottom, .... 
text_rect.center = (300, 300)

# publish on screen
# screen.blit(text_surface, text_rect)
screen.blit(mess, text_rect)

text2 = Aptos.render('vduczz', True, 'white')
text2_rect = mess.get_rect()
text2_rect.topleft = (400, 400)
screen.blit(text2, text2_rect)
pygame.display.flip()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()