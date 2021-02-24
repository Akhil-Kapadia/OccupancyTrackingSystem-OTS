import RPi.GPIO as GPIO
import time

class EntryDenial: 	
    
    #set inputs 
	def setMode1(self,input1,input2,input3,input4):
		GPIO.output(A1_1,input1)
		GPIO.output(A2_1,input2)
		GPIO.output(B1_1,input3)
		GPIO.output(B2_1,input4)
		time.sleep(0.005)

	#set inputs door 2 
	def setMode2(self,input1,input2,input3,input4):
		GPIO.output(A1_2,input1)
		GPIO.output(A2_2,input2)
		GPIO.output(B1_2,input3)
		GPIO.output(B2_2,input4)
		time.sleep(0.005)
		
	#switched inputs 2 and 3
	#move motors counter clockwise
	def OpenDoor1(self):
		#turn on green LED
		GPIO.output(17,True)
		
		for d in range(0,256):
			self.setMode1(1,0,0,1)
			self.setMode1(0,1,0,1)
			self.setMode1(0,1,1,0)
			self.setMode1(1,0,1,0)
			
		#turn off green LED
		GPIO.output(17,False)
		
		return None
		
	def OpenDoor2(self):
		#turn on green LED
		GPIO.output(20,True)
		
		for d in range(0,256):
			self.setMode2(1,0,0,1)
			self.setMode2(0,1,0,1)
			self.setMode2(0,1,1,0)
			self.setMode2(1,0,1,0)
			
		#turn off green LED
		GPIO.output(20,False)
		
		return None

	def CloseDoor1(self):
		#turn on red LED
		GPIO.output(27,True)	
		for i in range(0,256):
			self.setMode1(1,0,1,0)
			self.setMode1(0,1,1,0)
			self.setMode1(0,1,0,1)
			self.setMode1(1,0,0,1)
        #turn off red LED
		GPIO.output(27,False)
		self.setMode1(0,0,0,0)

	def CloseDoor2(self):
		#turn on red LED
		GPIO.output(21,True)	
		for i in range(0,256):
			self.setMode2(1,0,1,0)
			self.setMode2(0,1,1,0)
			self.setMode2(0,1,0,1)
			self.setMode2(1,0,0,1)
        #turn off red LED
		GPIO.output(21,False)
		self.setMode2(0,0,0,0)
	    
	
if __name__ == "__main__":
	print("here")
	A1_1 = 18
	A2_1 = 23
	B1_1 = 24
	B2_1 = 25
    
	A1_2 = 6
	A2_2 = 13
	B1_2 = 19
	B2_2 = 26

	
	#setup inputs to output
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(A1_1,GPIO.OUT)
	GPIO.setup(A2_1,GPIO.OUT)
	GPIO.setup(B1_1,GPIO.OUT)
	GPIO.setup(B2_1,GPIO.OUT)

	GPIO.setup(A1_2,GPIO.OUT)
	GPIO.setup(A2_2,GPIO.OUT)
	GPIO.setup(B1_2,GPIO.OUT)
	GPIO.setup(B2_2,GPIO.OUT)
	
	#set LEDs
	GPIO.setwarnings(False)#green
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17,GPIO.OUT)
	
	GPIO.setwarnings(False)#red
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(27,GPIO.OUT)
	
	GPIO.setwarnings(False)#green
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(20,GPIO.OUT)
	
	GPIO.setwarnings(False)#red
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(21,GPIO.OUT)
	
	#test entry denial class
	var = EntryDenial()
	var.OpenDoor1()
	var.CloseDoor1()
	var.OpenDoor2()
	var.CloseDoor2()
    