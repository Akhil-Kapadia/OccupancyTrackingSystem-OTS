import RPi.GPIO as GPIO
import time

class EntryDenial: 	
    
    #set inputs 
	def setMode(self,input1,input2,input3,input4):
		GPIO.output(A1,input1)
		GPIO.output(A2,input2)
		GPIO.output(B1,input3)
		GPIO.output(B2,input4)
		time.sleep(0.005)
		
	#switched inputs 2 and 3
	#move motors counter clockwise
	def OpenDoor(self):
		#turn on green LED
		GPIO.output(17,True)
		
		for d in range(0,256):
			self.setMode(1,0,0,1)
			self.setMode(0,1,0,1)
			self.setMode(0,1,1,0)
			self.setMode(1,0,1,0)
			
		#turn off green LED
		GPIO.output(17,False)
		
		return None

	def CloseDoor(self):
		#turn on red LED
		GPIO.output(27,True)	
		for i in range(0,256):
			self.setMode(1,0,1,0)
			self.setMode(0,1,1,0)
			self.setMode(0,1,0,1)
			self.setMode(1,0,0,1)
        #turn off red LED
		GPIO.output(27,False)
		self.setMode(0,0,0,0)
	    
	
if __name__ == "__main__":
	print("here")
	A1 = 18
	A2 = 23
	B1 = 24
	B2 = 25
	
	#setup inputs to output
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
		
	#test entry denial class
	var = EntryDenial()
	var.OpenDoor()
	var.CloseDoor()
	
