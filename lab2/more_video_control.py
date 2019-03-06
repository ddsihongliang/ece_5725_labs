#**************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 2/11/2019 (Monday's Lab)
# video_control.py
# python code to control video playback
# by GPIO pins and FIFO
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
        # Pause pressed
        cmd_line = 'echo "p" > /home/pi/lab2/video_fifo'

    elif ( not GPIO.input(22) ):
        # Rewind 10 sec
        cmd_line = 'echo "seek -10" > /home/pi/lab2/video_fifo'

    elif ( not GPIO.input(5) ):
        # Fast forward 10 sec
        cmd_line = 'echo "seek 30" > /home/pi/lab2/video_fifo'

    elif ( not GPIO.input(6) ):
        # Fast forward 10 sec
        cmd_line = 'echo "seek -30" > /home/pi/lab2/video_fifo'

    elif ( not GPIO.input(17) ):
        # Fast forward 10 sec
        cmd_line = 'echo "seek 10" > /home/pi/lab2/video_fifo'

    elif ( not GPIO.input(27) ):
        # Quit pressed
        cmd_line = 'echo "q" > /home/pi/lab2/video_fifo'
        # Quit loop
        run = False

    # Need this so that button doesn't 'float'!
    if cmd_line != "":
        print subprocess.check_output(cmd_line, shell=True)
        cmd_line = ""
