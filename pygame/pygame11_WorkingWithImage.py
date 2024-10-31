import pygame

pygame.init()

screen = pygame.display.set_mode((900, 600))

# loading img
bg_Img = pygame.image.load('pygame/bg_img2.jpg') # background
car = pygame.image.load('pygame/car.png')

# get size of img
width, height = bg_Img.get_size() # (width, height)
# or bg_Img.get_width(), bg_Img.get_height()
img_rect = bg_Img.get_rect() # Rect(x, y, width, height)
print(f'size of bg_Img = {width}x{height}')

# scale img
# syntax: pygame.transform.scall(img, (new widht, new height))
scaled_bg = pygame.transform.scale(bg_Img, (900, 600)) # 4608x3072 -> 900x600
car2x = pygame.transform.scale(car, (1.5 * car.get_width(), 1.5 * car.get_height())) # x1.5

# rotate the img
# syntax: pygame.transform.rotate(img, degree)
rotate_car = pygame.transform.rotate(car, 90)

# flip screen
# syntax: pygame.transform.flip(img, xbool, ybool)
xflip_car = pygame.transform.flip(car, True, False)
flip_car = pygame.transform.flip(car, 1, 1)

# update screen
screen.blit(scaled_bg, (0, 0))
screen.blit(car2x, (100, 100))
screen.blit(rotate_car, (400, 400))
screen.blit(xflip_car, (300, 300))
screen.blit(flip_car, (500, 200))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

