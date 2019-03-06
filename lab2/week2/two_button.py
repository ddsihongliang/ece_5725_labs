#**************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 2/27/2019 (Monday's Lab)
# screen_coordinates.py
#
# Two, on-screen buttons are displayed ‘start’ and ‘quit’.
# Hitting ‘start’ begins playback of the program, while hitting
# ‘quit’ ends the program and returns to the Linux console screen.
# Hitting any other location on the screen displays screen coordinates.
# The start and quit buttons should be displayed on the screen, 
# and operate whenever they are displayed, during the entire time
# the program is running (including while the animation is playing).
# Also has a physical bail-out button for this code.
#*************************************************************
import pygame
from pygame.locals import * # for event MOUSE variables
import os
import RPi.GPIO as GPIO
from time import sleep

#~ os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
#~ os.putenv('SDL_FBDEV', '/dev/fb1')
#~ os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
#~ os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(True)
WHITE = 255, 255, 255
BLACK = 0,0,0
screen = pygame.display.set_mode((320, 240))

GPIO.setmode(GPIO.BCM) # Set for broadcom numbering not board numbers...
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

my_font = pygame.font.Font(None, 30)
my_buttons = {'Start':(80,200),'Quit':(240,200)}
screen.fill(BLACK) # Erase the Work space

size = width, height = 320, 240
speed1 = [8,5]
speed2 = [10,6]

screen = pygame.display.set_mode(size)
ball1 = pygame.image.load("magic_ball_small.png")
ball2 = pygame.image.load("xmas_ball.png")
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()

counter = 1
run = 1
while run:
    sleep(0.02)
    if ( not GPIO.input(27) ):
        run = 0

    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            x,y = pos
            #text_surface = my_font.render(my_text, True, WHITE)
            #print 'Position at ',pos
            if (x > 221 and y > 192) and (x < 260 and y < 208):
                run = 0
            if (x > 50 and y > 190) and (x < 100 and y < 208):
                #print "Start"
                while run:
                    if ( not GPIO.input(27) ):
                        run = 0


                    sleep(.03)
                    ballrect1 = ballrect1.move(speed1)
                    ballrect2 = ballrect2.move(speed2)

                    #checking walls
                    if ballrect1.left < 0 or ballrect1.right > width:
                        speed1[0] = -speed1[0]
                    if ballrect1.top < 0 or ballrect1.bottom > 200:
                        speed1[1] = -speed1[1]
                    if ballrect2.left < 0 or ballrect2.right > width:
                        speed2[0] = -speed2[0]
                    if ballrect2.top < 0 or ballrect2.bottom > 200:
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


                    screen.fill(BLACK)            # Erase the Work space
                    screen.blit(ball1, ballrect1) # Combine Ball surface with workspace surface
                    screen.blit(ball2, ballrect2) # Combine Ball surface with workspace surface

                    counter+=1

                    for my_text, text_pos in my_buttons.items():
                        text_surface = my_font.render(my_text, True, WHITE)
                        rect = text_surface.get_rect(center=text_pos)
                        screen.blit(text_surface, rect)

                    pygame.display.flip()         # display workspace on screen
                    for event in pygame.event.get():
                        if(event.type is MOUSEBUTTONDOWN):
                            pos = pygame.mouse.get_pos()
                            x,y = pos
                            #text_surface = my_font.render(my_text, True, WHITE)
                            #print 'Position at ',pos
                            if (x > 221 and y > 192) and (x < 260 and y < 208):
                                run = 0
                            if (x > 50 and y > 190) and (x < 100 and y < 208):
                                speed1 = [8,5]
                                speed2 = [10,6]
                                ballrect1.center = [20,20]
                                ballrect2.center = [30,30]
                                counter = 1

    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)


    pygame.display.flip()
