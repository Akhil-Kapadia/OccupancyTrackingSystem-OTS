import RPi.GPIO as GPIO
import time

A1 = 18
A2 = 23
B1 = 24
B2 = 25

def setMode(input1,input2,input3,input4):
	GPIO.output(A1,input1)
	GPIO.output(A2,input2)
	GPIO.output(B1,input3)
	GPIO.output(B2,input4)
	time.sleep(0.005)
	
#set inputs to output
GPIO.setmode(GPIO.BCM)
GPIO.setup(A1,GPIO.OUT)
GPIO.setup(A2,GPIO.OUT)
GPIO.setup(B1,GPIO.OUT)
GPIO.setup(B2,GPIO.OUT)

#set LEDs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)

#turn on green LED
GPIO.output(17,True)
#move motors clockwise
for i in range(0,256):
	setMode(1,0,1,0)
	setMode(0,1,1,0)
	setMode(0,1,0,1)
	setMode(1,0,0,1)
	
#turn off green LED
GPIO.output(17,False)

#switched inputs 2 and 3
#move motors counter clockwise
#turn on red LED
GPIO.output(27,True)
for d in range(0,256):
	setMode(1,0,0,1)
	setMode(0,1,0,1)
	setMode(0,1,1,0)
	setMode(1,0,1,0)
	
#turn off red LED
GPIO.output(27,False)

setMode(0,0,0,0)

