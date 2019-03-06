#***********************************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 2/11/2019 (Monday's Lab)
# video_control.py
# python code to control video playback by GPIO pins and FIFO.
# Added callback functions. For performance test with perfself.
#********************************************************
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

#callback functions
def GPIO5_callback(channel):
    print("GPIO 5 Callback function")
    cmd_line = 'echo "seek -30" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)

def GPIO6_callback(channel):
    print("GPIO 6 Callback function")
    cmd_line = 'echo "seek 30" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)

def GPIO17_callback(channel):
    print("GPIO 17 Callback function")
    cmd_line = 'echo "seek 10" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)

def GPIO22_callback(channel):
    print("GPIO 22 Callback function")
    cmd_line = 'echo "seek -10" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)

def GPIO23_callback(channel):
    print("GPIO 23 Callback function")
    cmd_line = 'echo "p" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)

def GPIO27_callback(channel):
    print("GPIO 27 Callback function")
    cmd_line = 'echo "q" > /home/pi/lab2/video_fifo'
    print subprocess.check_output(cmd_line, shell=True)
    run = False

# add rising edge event detection on a channel
GPIO.add_event_detect(5, GPIO.RISING, callback=GPIO5_callback)
GPIO.add_event_detect(6, GPIO.RISING, callback=GPIO6_callback)
GPIO.add_event_detect(17, GPIO.RISING, callback=GPIO17_callback)
GPIO.add_event_detect(22, GPIO.RISING, callback=GPIO22_callback)
GPIO.add_event_detect(23, GPIO.RISING, callback=GPIO23_callback)
GPIO.add_event_detect(27, GPIO.RISING, callback=GPIO27_callback)

cmd_line = ""
run = True
t_end = time.time() + 10
while run and (time.time() < t_end):

    #~ try:
    time.sleep(0)
    #~ except KeyboardInterrupt:
        #~ GPIO.cleanup()
GPIO.cleanup()
