#**************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 3/4/2019 (Monday's Lab)
# blink.py
# Use PWM signals to control an LED
#**************************************
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)

freq = raw_input("Enter Frequency: ")

p = GPIO.PWM(5, float(freq))

p.start(50) #dc is duty cycle 0 to 100

time.sleep(1)

#p.ChangeFrequency(freq)

#p.ChangeDutyCycle(dc)

p.stop()
GPIO.cleanup()
