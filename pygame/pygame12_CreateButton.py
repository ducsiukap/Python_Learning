import pygame
from pygame import mixer
import random
import math

pygame.init()
mixer.init()

screen = pygame.display.set_mode((700, 700))
screen.fill('lightskyblue3')
# create music list
song_list = []
released = []
for i in range(5):
    song_list.append(f'pygame/music/song{i}.mp3')
    released.append(True)

name_list = [['Cam Giac Luc Ay Se Ra Sao',  'Lou Hoang'],
             ['Dan Choi Sao Phai Khoc', 'Andree Right Hand ft Ryder'],
             ['Dung Lam Trai Tim Anh Dau' , 'Son Tung MTP'],
             ['ID Thang May', 'W/n ft 267'], 
             ['FLVR - Tlinh', 'Lowg']]

song_name_font = pygame.font.SysFont('trebuchetms', 25, True)
singer_name_font = pygame.font.SysFont('couriernew', 18)
print(pygame.font.get_fonts())
def song_detail(index):
    song_name = song_name_font.render(name_list[index][0], True, (0, 0, 0))
    song_name_rect = song_name.get_rect(topleft=(100, 250))

    singer_name = singer_name_font.render(name_list[index][1], True, (0, 0, 0))
    singer_name_rect = singer_name.get_rect(topleft=(100, 300))

    screen.blit(song_name, song_name_rect)
    screen.blit(singer_name, singer_name_rect)


def next_song(index, mixxing):
    global released, song_list
    if sum(released) == len(song_list):
        released = [False for _ in range(len(song_list))]
    next_index = (index + 1) % len(song_list)
    if mixxing:
        next_index = random.randint(0, len(song_list) - 1)
        while released[next_index]:
            next_index = (next_index + 1) % len(song_list)
    released[next_index] = True
    return next_index

# button_list = [cd disk, unmix, mix, prev song, pause, play, next song]
button_list = [pygame.transform.scale(pygame.image.load('pygame/cd.png'), (200, 200)),
               pygame.transform.scale(pygame.image.load('pygame/mix.png'), (32, 32)),
               pygame.transform.scale(pygame.image.load('pygame/mixxing.png'), (32, 32)),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load('pygame/next.png'), (32, 32)), 1, 0),
               pygame.transform.scale(pygame.image.load('pygame/pause.png'), (32, 32)),
               pygame.transform.scale(pygame.image.load('pygame/play.png'), (32, 32)),
               pygame.transform.scale(pygame.image.load('pygame/next.png'), (32, 32))]
button_pos_list = [(520, 300), (184, 500), (184, 500),  (284, 500), 
                   (384, 500), (384, 500),  (484, 500)]
button_rect_list = []

for i in range(7): 
    button_rect_list.append(button_list[i].get_rect(topleft=button_pos_list[i]))


# status = 1 -> playing
#       = 0 -> pause
cd_angle = 0
def draw_button(status, mixxing):
    global cd_angle
    # draw cd disk
    cd_rotate = pygame.transform.rotate(button_list[0], cd_angle)
    cd_rect = cd_rotate.get_rect(center=button_pos_list[0])
    screen.blit(cd_rotate, cd_rect)

    mix = 1 if mixxing else 2
    cont = 4 if status == 0 else 5
    for i in range(1, 7):
        if i == mix or i == cont:
            continue
        screen.blit(button_list[i], button_pos_list[i])
    cd_angle -= status
    cd_angle %= 360


# create text, index, font
index = 0
last_index = []
mixxing = False
status = 1 # playing

SONG_END = pygame.USEREVENT + 1
mixer.music.set_volume(0.2)
def play_song(index):
    mixer.music.stop()
    pygame.time.delay(1000)
    mixer.music.load(song_list[index])
    mixer.music.play()
    released[index] = True


draw_button(status, mixxing)
play_song(index)
song_detail(index)
pygame.draw.rect(screen, (0, 0, 0), (150, 450, 400, 2))
pygame.display.flip()

while True: 
    pygame.time.Clock().tick(60) # fps
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button_rect_list[1].collidepoint(event.pos): # mix / unmix
                    mixxing = not mixxing
                elif button_rect_list[4].collidepoint(event.pos): # pause / play
                    status = (status + 1) % 2
                    if mixer.music.get_busy():
                        mixer.music.pause()
                    else: mixer.music.unpause()
                elif button_rect_list[3].collidepoint(event.pos): # previous song
                    if len(last_index):
                        released[index] = False
                        index = last_index[-1]
                        last_index.pop()

                        mixer.music.stop()
                        pygame.time.delay(1000)
                        play_song(index)
                        status = 1 # playing

                elif button_rect_list[6].collidepoint(event.pos): # next_song
                    pygame.event.post(pygame.event.Event(SONG_END))

        if event.type == SONG_END:
            last_index.append(index)
            if len(last_index) > len(song_list):
                last_index.pop(0)
            index = next_song(index, mixxing)
            # released[index] = True
            pygame.time.delay(1000)
            status = 1 # playing
            play_song(index)

    if mixer.music.get_busy() == False and status == 1:
        pygame.event.post(pygame.event.Event(SONG_END))

    
    #update screen
    screen.fill('lightskyblue3')
    song_detail(index)
    pygame.draw.rect(screen, (0, 0, 0), (150, 450, 400, 2))
    draw_button(status, mixxing)
    pygame.display.flip()
    