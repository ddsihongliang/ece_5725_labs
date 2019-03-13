#**************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 3/4/2019 (Monday's Lab)
# pwm_calibrate.py
# Use PWM signals to control a servo
#**************************************

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

freq = raw_input("Enter Frequency: ")
DC = raw_input("Enter new duty cycle: ")

p = GPIO.PWM(6, float(freq))
p.start(float(DC)) #dc is duty cycle 0 to 100

run = 1
while run < 100:
    time.sleep(.02)
    try:
	freq = raw_input("Enter new frequcy: ")
	p.ChangeFrequency(float(freq))
	DC = raw_input("Enter new duty cycle: ")
	p.ChangeDutyCycle(float(DC))
	
    except:
	run = 100
    run += 1

p.stop()
GPIO.cleanup()

