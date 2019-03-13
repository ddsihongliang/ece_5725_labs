#**************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 3/4/2019 (Monday's Lab)
# servo_control.py
# run a servo through a range of different speeds
#**************************************

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#start stopped
print("Stopped: ")
print("Freq: 46.511 Hz")
print("Duty Cycle: 6.977")
print("Pulse Width: 1.5 ms")
print("\n")

freq = 46.511
dc = 6.977
p = GPIO.PWM(5, freq)
p.start(dc) #dc is duty cycle 0 to 100

run = 0
while run < 21:
	time.sleep(3)
	
	if run < 10:            #moving towards CW max
		freq -= .0437
		dc -= .0977
	elif run == 10:           #reset to CCW
		print "Clockwise\n"
		freq = 46.554
		dc = 7.0627
	else:
		freq += .0428
		dc += .0857
		
	p.ChangeFrequency(float(freq))
	p.ChangeDutyCycle(float(dc))
	
	print "Freq: ", str(freq)
	print "Duty Cycle: ", str(dc)
	print "Pulse Width: ", str(1/freq*(dc/100)*1000), " ms"
	print "\n"
		
	run += 1

freq = 46.511
dc = 6.977
p.ChangeFrequency(float(freq))
p.ChangeDutyCycle(float(dc))
	
print "Freq: ", str(freq)
print "Duty Cycle: ", str(dc)
print "Pulse Width: ", str(1/freq*(dc/100)*1000), " ms"
print "\n"
time.sleep(3)


p.stop()

GPIO.cleanup()
