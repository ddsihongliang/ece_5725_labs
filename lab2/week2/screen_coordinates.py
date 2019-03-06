#**************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 2/27/2019 (Monday's Lab)
# screen_coordinates.py

# Display a single quit button at the bottom of the screen.
# Tapping any location on the screen still display ‘Hit at x, y’
# where x, y show the screen coordinates
# of the hit. Tapping the ‘quit’ button will exit the program.
# All hits should be displayed on the Linux console as well.
# Also had a physical bail-out button for this code.
#**************************************
import pygame
from pygame.locals import * # for event MOUSE variables
import os
import RPi.GPIO as GPIO
from time import sleep

os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(True)
WHITE = 255, 255, 255
BLACK = 0,0,0
screen = pygame.display.set_mode((320, 240)) #Set display size

GPIO.setmode(GPIO.BCM) # Set for broadcom numbering not board numbers...
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

my_font = pygame.font.Font(None, 30)
my_buttons = {'Quit':(240,200)}
screen.fill(BLACK) # Erase the Work space

run = 1
while run:
    sleep(0.02)
    if ( not GPIO.input(27) ):    # Bail-out funtion
        run = 0

    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            x,y = pos
            print 'Position at ',pos
            if (x > 221 and y > 192) and (x < 260 and y < 208):
                run = 0
            else:
               screen.fill(BLACK) # Erase the Work space
               my_text2 = 'Position at ' + str(pos[0])+ ' ,'+ str(pos[1])
               text_surface = my_font.render(my_text2, True, WHITE)
               rect = text_surface.get_rect(center=[120, 20])
               screen.blit(text_surface, rect)

    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    pygame.display.flip()
