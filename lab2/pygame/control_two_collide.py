import pygame
from pygame.locals import * # for event MOUSE variables
import os
from time import sleep
import RPi.GPIO as GPIO

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
#these are just random guesses without the actual piTFT
my_buttons2={'Pause':(30,220),'Fast':(120,220), 'Slow':(210,220),'Back':(290,220)}
screen.fill(BLACK) # Erase the Work space

size = width, height = 320, 240
speed1 = [8,5]
speed2 = [10,6]
tempSpeed1 = [8,5]
tempSpeed2 = [10,6]

screen = pygame.display.set_mode(size)
ball1 = pygame.image.load("magic_ball_small.png")
ball2 = pygame.image.load("xmas_ball.png")
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()

paused = 0
counter = 1
run = 1
speed_multi = 1
while run:
    sleep(0.02)
    if ( not GPIO.input(27) ):
        run = 0

    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if (x > 221 and y > 192) and (x < 260 and y < 208):
                run = 0

            if (x > 50 and y > 190) and (x < 100 and y < 208):
            	#this if statement enters level 2
            	level2 = 1
                while (run and level2):
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
                    if (rad > 600):
                        counter = 1
                    elif (rad <= 600 and counter != 0):
                        counter = 0
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

                    #this should print all 4 new buttons
                    for my_text, text_pos in my_buttons2.items():
                        text_surface = my_font.render(my_text, True, WHITE)
                        rect = text_surface.get_rect(center=text_pos)
                        screen.blit(text_surface, rect)

                    pygame.display.flip()         # display workspace on screen
                    for event in pygame.event.get():
                        if(event.type is MOUSEBUTTONDOWN):
                            pos = pygame.mouse.get_pos()
                            x,y = pos

                            #Done CALIBRATE ALL OF THESE RANGES
                            print 'Position at ' + str(pos[0])+ ' ,'+ str(pos[1])
                            #Pause Button
                            if (x > 5 and y > 210) and (x < 60 and y < 230):
                                if paused:
	                                speed1 = tempSpeed1
	                                speed2 = tempSpeed2
	                                paused = 0
                                else:
	                                tempSpeed1 = speed1
	                                tempSpeed2 = speed2
	                                speed1 = [0,0]
	                                speed2 = [0,0]
	                                paused = 1

                            #Fast Button
                            if (x > 100 and y > 210) and (x < 140 and y < 230):
                                speed1[0] = speed1[0] * 2
                                speed1[1] = speed1[1] * 2
                                speed2[0] = speed2[0] * 2
                                speed2[1] = speed2[1] * 2
                                speed_multi *= 2

                            #Slow Button
                            if (x > 180 and y > 210) and (x < 230 and y < 230):
                                speed1[0] = speed1[0] / 2
                                speed1[1] = speed1[1] / 2
                                speed2[0] = speed2[0] / 2
                                speed2[1] = speed2[1] / 2
                                speed_multi /= 2

                            #Back Button
                            if (x > 260 and y > 210) and (x < 320 and y < 230):
                            	#break out of only inner loop
                                level2 = 0
                                screen.fill(BLACK)
                                speed1 = [8,5]
                                speed2 = [10,6]
                                ballrect1.center = [20,20]
                                ballrect2.center = [30,30]
            else:
               screen.fill(BLACK) # Erase the Work space
               
    screen.fill(BLACK)
    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    pygame.display.flip()
