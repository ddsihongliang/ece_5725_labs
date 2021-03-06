#***********************************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 2/11/2019 (Monday's Lab)
# two_collide.py
# python code to play animation of two bouncing balls
#********************************************************
import pygame # Import pygame graphics library
import os # for OS calls
from time import sleep

os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb0')

pygame.init()

size = width, height = 320, 240
speed1 = [8,5]
speed2 = [10,6]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball1 = pygame.image.load("magic_ball_small.png")
ball2 = pygame.image.load("xmas_ball.png")
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()

counter = 1;

while 1:
    sleep(.03)
    ballrect1 = ballrect1.move(speed1)
    ballrect2 = ballrect2.move(speed2)

    #checking walls
    if ballrect1.left < 0 or ballrect1.right > width:
        speed1[0] = -speed1[0]
    if ballrect1.top < 0 or ballrect1.bottom > height:
        speed1[1] = -speed1[1]
    if ballrect2.left < 0 or ballrect2.right > width:
        speed2[0] = -speed2[0]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed2[1] = -speed2[1]

    #collision
    dx = (ballrect2.center[0]-ballrect1.center[0])
    dy = (ballrect2.center[1]-ballrect1.center[1])
    rad = dx*dx + dy*dy
    if (rad < 576 and counter > 20):
        counter = 1
        dvx = speed1[0] - speed2[0]
        dvy = speed1[1] - speed2[1]
        dvx = -dx * (dx * dvx + dy * dvy) / rad
        dvy = -dy * (dx * dvx + dy * dvy) / rad
        speed1[0] += dvx
        speed1[1] += dvy
        speed2[0] -= dvx
        speed2[1] -= dvy


    screen.fill(black)            # Erase the Work space
    screen.blit(ball1, ballrect1) # Combine Ball surface with workspace surface
    screen.blit(ball2, ballrect2) # Combine Ball surface with workspace surface
    pygame.display.flip()         # display workspace on screen
    counter+=1
