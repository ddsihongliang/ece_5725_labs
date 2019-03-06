import pygame # Import pygame graphics library
import os # for OS calls
from time import sleep

# os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
# os.putenv('SDL_FBDEV', '/dev/fb0') 

pygame.init()

size = width, height = 320, 240
speed1 = [4,5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball1 = pygame.image.load("magic_ball_small.png")
ballrect1 = ball1.get_rect()

while 1:
    sleep(.05)
    ballrect1 = ballrect1.move(speed1)
    if ballrect1.left < 0 or ballrect1.right > width:
        speed1[0] = -speed1[0]
    if ballrect1.top < 0 or ballrect1.bottom > height:
        speed1[1] = -speed1[1]


    screen.fill(black)            # Erase the Work space
    screen.blit(ball1, ballrect1) # Combine Ball surface with workspace surface
    pygame.display.flip()         # display workspace on screen
