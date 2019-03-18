#****************************************************
# Hongliang Si & Jim Connelly
# hs983 & jpc324 (@cornell.edu)
# 3/4/2019 (Monday's Lab)
# two_wheel.py
# Select two unused GPIO pins for the attachment for two continuous
# rotation servos. Attach the servos for correct power and control
# using the RPi
#****************************************************
import time
import RPi.GPIO as GPIO

def changeServo (servo, speed):
	#servo 0 = left, servo 1 = right
	#speed -1 = CCW, speed 0 = stopped, speed 1 = CW
	if servo == 0:
		if speed == 0:
			freq = 46.511
			dc = 0
		elif speed == 1:
			freq = 46.948
			dc = 6
		else:
			freq = 46.083
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

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)

GPIO.setup(5, GPIO.OUT)   #servo 0
GPIO.setup(19, GPIO.OUT)  #servo 1

freq1 = 46.511
dc1 = 0

p1 = GPIO.PWM(5, freq1)
p1.start(dc1) #dc is duty cycle 0 to 100

p2 = GPIO.PWM(19, freq1)
p2.start(dc1) #dc is duty cycle 0 to 100

run = True
while run:
    time.sleep(.3)
    if ( not GPIO.input(17) ):
        print "Left servo Clock-wise."
        changeServo (0, 1)

    elif ( not GPIO.input(22) ):
        print "Left servo Counter-Clock-wise."
        changeServo (0, -1)

    elif ( not GPIO.input(23) ):
        print "Right servo Clock-wise."
        changeServo (1, 1)

    elif ( not GPIO.input(27) ):
        print "Right servo Counter-Clock-wise."
        changeServo (1, -1)

    elif ( not GPIO.input(13) ):
        print "Left servo stop."
        changeServo (0, 0)

    elif ( not GPIO.input(6) ):
        print "Right servo stop."
        changeServo (1, 0)

p.stop()
GPIO.cleanup()
