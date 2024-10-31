import pygame
import sys
from pygame import mixer # for music

pygame.init()

screen = pygame.display.set_mode((700, 700))

# load img
bg_img = pygame.transform.scale(pygame.image.load('pygame/bg_img.jpg'), screen.get_size()) # game backgound
player = pygame.image.load('pygame/player.png') # player
alien = pygame.image.load('pygame/alien.png')
bullet = pygame.transform.scale(pygame.image.load('pygame/bullet.png'), (24, 24))
# put img on screen
screen.blit(bg_img, (0, 0))
screen.blit(alien, (318, 80))
screen.blit(player, (318, 600))
pygame.display.flip()

# multiple bullet
Bullets = [] # list of bullet
bullet_speed = -1

# draw bullet:
def draw_bullet(Bullet):
    screen.blit(bullet, (Bullet[0], Bullet[1]))
    # if y <= 80 + 64 - 20:
    #     Bullets.pop(0)

# load a music file 
# syntax: mixer.music.load('path_to_music_file')
fight_sound = mixer.music.load('pygame/fight_sound.mp3')
# set_volume()
mixer.music.set_volume(0.1)
# play() can play only one music file 
mixer.music.play(-1) # play(-1) -> replay after end
# stop(), pause(), unpause(), rewind() 
# get_busy() -> check if music is playing

# load a sound
# syntax: sound_name = mixer.play()
shoot_effect_sound = mixer.Sound('pygame/piuuu.mp3')
# stop(), set_volume(), fadeout(), get_length()
shoot_effect_sound.set_volume(0.2)
shooting = False

woo = mixer.Sound('pygame/woo.mp3')
woo.set_volume(0.2)

last_shot_time = 0
while True:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shooting = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shooting = False
    if shooting and current_time - last_shot_time > 200:
        shoot_effect_sound.play(maxtime=700)
        Bullets.append([338, 600])
        last_shot_time = current_time


    screen.blit(bg_img, (0, 0))
    for Bullet in Bullets[:]:
        Bullet[1] += bullet_speed
        draw_bullet(Bullet)
        if Bullet[1] <= 144:
            woo.play(maxtime=500)
            Bullets.remove(Bullet)
             
    screen.blit(alien, (318, 80))
    screen.blit(player, (318, 600))
    pygame.display.flip()

