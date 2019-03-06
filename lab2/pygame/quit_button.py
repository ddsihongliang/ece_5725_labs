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
pygame.mouse.set_visible(False)
WHITE = 255, 255, 255
BLACK = 0,0,0
screen = pygame.display.set_mode((320, 240))

GPIO.setmode(GPIO.BCM) # Set for broadcom numbering not board numbers...
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

my_font = pygame.font.Font(None, 30)
my_buttons = {'Quit':(240,200)}
screen.fill(BLACK) # Erase the Work space

for my_text, text_pos in my_buttons.items():
    text_surface = my_font.render(my_text, True, WHITE)
    rect = text_surface.get_rect(center=text_pos)
    screen.blit(text_surface, rect)

pygame.display.flip()
run = 1
while run:
    if ( not GPIO.input(27) ):
        run = 0
    
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            print 'Quit pressed'
            run = 0
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            print 'Quit pressed'
            run = 0
