#**************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 2/11/2019 (Monday's Lab)
# six_buttons.py
# python code to test all 6 buttons working
#**************************************
import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM) # Set for broadcom numbering not board numbers...

# Setup piTFT buttons
# Pins: 17 22 23 27 5 6
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)

cmd_line = ""
run = True
while run:
    time.sleep(.3)
    if ( not GPIO.input(23) ):
        print "Pin 23 pressed."

    elif ( not GPIO.input(22) ):
        print "Pin 22 pressed."

    elif ( not GPIO.input(5) ):
        print "Pin 5 pressed."

    elif ( not GPIO.input(6) ):
        print "Pin 6 pressed."

    elif ( not GPIO.input(17) ):
        print "Pin 7 pressed."

    elif ( not GPIO.input(27) ):
        print "Pin 27 pressed."
        print "Quit loop."
        run = False

    # Need this so that button doesn't 'float'!
    if cmd_line != "":
        print subprocess.check_output(cmd_line, shell=True)
        cmd_line = ""
GPIO.cleanup()
