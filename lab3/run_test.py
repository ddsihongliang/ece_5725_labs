#**************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 3/11/2019 (Monday's Lab)
# run_test.py
# test the robot by simple moves.
#**************************************
import pygame # Import pygame graphics library
import os # for OS calls
from pygame.locals import*
from time import sleep
import RPi.GPIO as GPIO
import time

os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)

# Set RGB colors
WHITE = 255, 255, 255
BLACK = 0,0,0
RED   = 255,0,0
GREEN = 0,255,0

# Initialize arrays for display
left = ['stop', 0, 'stop', 0, 'stop', 0]    # Left log
right = ['stop', 0, 'stop', 0, 'stop', 0]   # Right log
screen = pygame.display.set_mode((320, 240))

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.OUT)   #servo 0
GPIO.setup(19, GPIO.OUT)  #servo 1

def func_stop():
    print 'EMERGENCY!!!STOP!!'
    # right stop
    changeServo (1, 0)
    moveTerms(right)
    right[0] = 'Stop'
    right[1] = int(time.time() - timeVal)

    # left stop
    changeServo (0, 0)
    moveTerms(left)
    left[0] = 'Stop'
    left[1] = int(time.time() - timeVal)


def changeServo (servo, speed):
	#servo 0 = left, servo 1 = right
	#speed -1 = CCW, speed 0 = stopped, speed 1 = CW
	if servo == 0:
		if speed == 0:
			freq = 46.511
			dc = 0
		elif speed == 1:
			freq = 46.848
			dc = 6
		else:
			freq = 46.283
			dc = 7.7
		p1.ChangeFrequency(float(freq))
		p1.ChangeDutyCycle(float(dc))
	else:
		if speed == 0:
			freq = 46.511
			dc = 0
		elif speed == 1:
			freq = 46.948
			dc = 6
		else:
			freq = 46.083
			dc = 7.7
		p2.ChangeFrequency(float(freq))
		p2.ChangeDutyCycle(float(dc))


def moveTerms(array):
    # Push old log to the next slot
	array[5] = array[3]
	array[4] = array[2]
	array[3] = array[1]
	array[2] = array[0]

def color(presssed):
    # Determine the color
    if (presssed==-1):
        return GREEN
    if (presssed==0):
	return RED

def print_button(presssed):
    # Print information on the screen
    screen.fill(BLACK) # Erase the Work space
    pygame.draw.circle(screen,color(presssed),(160,120),40)

    if(presssed == 0):
        for my_text, text_pos in STOP_button.items():
	    text_surface = my_font.render(my_text, True, WHITE)
	    rect = text_surface.get_rect(center=text_pos)
	    screen.blit(text_surface, rect)

    elif(presssed==-1):
        for my_text, text_pos in RESUME_button.items():
	    text_surface = my_font.render(my_text, True, WHITE)
	    rect = text_surface.get_rect(center=text_pos)
	    screen.blit(text_surface, rect)

    for my_text, text_pos in QUIT_button.items():
	text_surface = my_font.render(my_text, True, WHITE)
	rect = text_surface.get_rect(center=text_pos)
	screen.blit(text_surface, rect)

    my_textL1 = left[0] + "  " + str(left[1])
    text_surface = my_font.render(my_textL1, True, WHITE)
    rect = text_surface.get_rect(center=[50, 50])
    screen.blit(text_surface, rect)

    my_textL2 = left[2] + "  " + str(left[3])
    text_surface = my_font.render(my_textL2, True, WHITE)
    rect = text_surface.get_rect(center=[50, 70])
    screen.blit(text_surface, rect)

    my_textL3 = left[4] + "  " + str(left[5])
    text_surface = my_font.render(my_textL3, True, WHITE)
    rect = text_surface.get_rect(center=[50, 90])
    screen.blit(text_surface, rect)

    my_textR1 = right[0] + "  " + str(right[1])
    text_surface = my_font.render(my_textR1, True, WHITE)
    rect = text_surface.get_rect(center=[250, 50])
    screen.blit(text_surface, rect)

    my_textR2 = right[2] + "  " + str(right[3])
    text_surface = my_font.render(my_textR2, True, WHITE)
    rect = text_surface.get_rect(center=[250, 70])
    screen.blit(text_surface, rect)

    my_textR3 = right[4] + "  " + str(right[5])
    text_surface = my_font.render(my_textR3, True, WHITE)
    rect = text_surface.get_rect(center=[250, 90])
    screen.blit(text_surface, rect)

    pygame.display.update()

def move(command):
    if(command is "forward"):
        # moving forward
        #print ("moving forward.")
        L = 1
        R = 1
    elif(command is "backward"):
        # moving backward
        print ("moving backward.")
        L = -1
        R = -1
    elif(command is "left"):
        # pivot left
        print ("pivot left.")
        L = -1
        R = 1
    elif(command is "right"):
        # pivot right
        print ("pivot right.")
        L = 1
        R = -1
    changeServo (0, L)
    moveTerms(left)
    left[0] = 'CCW'
    left[1] = int(time.time() - timeVal)
    changeServo (1, -R)
    moveTerms(right)
    right[0] = 'CW'
    right[1] = int(time.time() - timeVal)
    print_button(presssed)

def check_stop(presssed):
    #Check the stop button.
    run = 1
    while run:
	if ( not GPIO.input(27) ):
        exit(0)
        for event in pygame.event.get():
            if(event.type is MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                x,y = pos

                if (x > 221 and y > 192) and (x < 260):
                    exit(0)
                    #~ Check distance from center
                distance = pow(pow(abs(x-160),2) + pow(abs(y-120),2),0.5)

                if (distance < 40):
                    screen.fill(BLACK) # Erase the Work space
                    presssed = ~presssed;
                    #draw the circle
                    pygame.draw.circle(screen,color(presssed),(160,120),40)
                    func_stop()
                    print_button(presssed)

        if (presssed==0):
            run = 0
        time.sleep(0.3)

freq1 = 46.511
dc1 = 0

p1 = GPIO.PWM(5, freq1)
p1.start(dc1) #dc is duty cycle 0 to 100

p2 = GPIO.PWM(19, freq1)
p2.start(dc1) #dc is duty cycle 0 to 100

my_font = pygame.font.Font(None, 25)

QUIT_button = {'Quit':(240,220),'Left History':(50,10),'Right History':(255,10)}
STOP_button   ={'STOP':(160,120)}
RESUME_button ={'RESUME':(160,120)}

screen.fill(BLACK) # Erase the Work space
pygame.draw.circle(screen,RED,(160,120),40)
pygame.display.update()

run = True
presssed = 0;
timeVal = time.time()   #start timing
while run:
    print_button(presssed)
    time.sleep(.3)

    # moving forward
    move("forward")
    for i in range(1,5):
        check_stop(presssed)

    # stop
    func_stop()
    print_button(presssed)
    for i in range(1,5):
        check_stop(presssed)

    # moving backward
    move("backward")
    for i in range(1,5):
        check_stop(presssed)

    # stop
    func_stop()
    print_button(presssed)
    for i in range(1,5):
        check_stop(presssed)

    # Pivot left
    move("left")
    for i in range(1,5):
        check_stop(presssed)

    # stop
    func_stop()
    print_button(presssed)
    for i in range(1,5):
        check_stop(presssed)

    # Pivot right
    move("right")
    for i in range(1,5):
        check_stop(presssed)

    # stop
    func_stop()
    print_button(presssed)
    for i in range(1,10):
        check_stop(presssed)
    time.sleep(1)

p1.stop()
p2.stop()
GPIO.cleanup()
