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

def GPIO5_call(channel):
    print "button pressed 5"
    # Rewind 30 sec
    cmd_line = 'echo "seek -10" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)
    cmd_line = ""

def GPIO6_call(channel):
    print "button pressed 6"
    # Fast forward 30 sec
    cmd_line = 'echo "seek -30" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)
    cmd_line = ""

def GPIO22_call(channel):
    print "button pressed 22"
    # Rewind 10 sec
    cmd_line = 'echo "seek -10" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)
    cmd_line = ""

def GPIO23_call(channel):
    print "button pressed 23"
    # Pause pressed
    cmd_line = 'echo "p" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)
    cmd_line = ""
def GPIO17_call(channel):
    print "button pressed 17"
    # Fast forward 10 sec
    cmd_line = 'echo "seek 10" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)
    cmd_line = ""

GPIO.add_event_detect(5, GPIO.BOTH, callback=GPIO5_call, bouncetime=300)
GPIO.add_event_detect(6, GPIO.BOTH, callback=GPIO6_call, bouncetime=300)
GPIO.add_event_detect(22, GPIO.BOTH, callback=GPIO22_call, bouncetime=300)
GPIO.add_event_detect(23, GPIO.BOTH, callback=GPIO23_call, bouncetime=300)
GPIO.add_event_detect(17, GPIO.BOTH, callback=GPIO17_call, bouncetime=300)

cmd_line = ""
run = True
while run:
    print "waiting for button"
    GPIO.wait_for_edge(27,GPIO.RISING)
    print "Quit the program"
    cmd_line = 'echo "q" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)
    cmd_line = ""
    run = False

GPIO.cleanup()

