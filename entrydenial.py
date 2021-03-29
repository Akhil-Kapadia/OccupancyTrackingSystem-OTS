import RPi.GPIO as GPIO
import time
from omxplayer.player import OMXPlayer
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import re




doorLocked = True

class EntryDenial: 	
    
    #set inputs 
	def setMode1(self,input1,input2,input3,input4):
		GPIO.setwarnings(False)
		GPIO.output(A1_1,input1)
		GPIO.output(A2_1,input2)
		GPIO.output(B1_1,input3)
		GPIO.output(B2_1,input4)
		time.sleep(0.005)

	#set inputs door 2 
	def setMode2(self,input1,input2,input3,input4):
		GPIO.setwarnings(False)
		GPIO.output(A1_2,input1)
		GPIO.output(A2_2,input2)
		GPIO.output(B1_2,input3)
		GPIO.output(B2_2,input4)
		time.sleep(0.005)
		
	#switched inputs 2 and 3
	#move motors counter clockwise
	def OpenDoor1(self,doorLocked):

		
		#audio for door 1 opening
		if(doorLocked == True):
		  path = Path('/home/pi/Downloads/OpenDoor1.wav')
		  player = OMXPlayer(path, args='-o alsa')
		
		#turn on green LED,turn off red
		GPIO.output(27,False)
		GPIO.output(17,True)
		
		#go sign(go - 2.5)
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False) 
		GPIO.setup(3, GPIO.OUT)
		servo1 = GPIO.PWM(3,50) #50 Hz
		servo1.start(2.5)
		
		if(doorLocked == True):
	     #move motors counterclockwise
		 for d in range(0,256):
			 self.setMode1(1,0,0,1)
			 self.setMode1(0,1,0,1)
			 self.setMode1(0,1,1,0)
			 self.setMode1(1,0,1,0)
			
		doorLocked = False
		
		return doorLocked
		
	"""def OpenDoor2(self,doorLocked):
		
		#audio for door 2 opening
		path = Path('/home/pi/Downloads/OpenDoor2.wav')
		player = OMXPlayer(path, args='-o alsa')
		
		#turn on green LED
		GPIO.output(21,False)
		GPIO.output(20,True)
		
		#stop go sign(go - 2.5)
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False) 
		GPIO.setup(4, GPIO.OUT)
		
		servo1 = GPIO.PWM(4,50) #50 Hz
		servo1.start(2.5)
		
		
		for d in range(0,256):
			self.setMode2(1,0,0,1)
			self.setMode2(0,1,0,1)
			self.setMode2(0,1,1,0)
			self.setMode2(1,0,1,0)
			
        doorLocked = False

        return True"""

    

	def CloseDoor1(self,doorLocked):
		
		#audio for door 1 closing
		if(doorLocked == False):
		  path = Path('/home/pi/Downloads/CloseDoor1.wav')
		  player = OMXPlayer(path, args='-o alsa')
		
		#turn on red LED,turn off green
		GPIO.output(17,False)
		GPIO.output(27,True)
		
		#stop go sign(stop - 12.5)
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False) 
		GPIO.setup(3, GPIO.OUT)
		servo1 = GPIO.PWM(3,50) #50 Hz
		servo1.start(12.5)
		
		if(doorLocked == False):
		  #move motors clockwise
		  for i in range(0,256):
			  self.setMode1(1,0,1,0)
			  self.setMode1(0,1,1,0)
			  self.setMode1(0,1,0,1)
			  self.setMode1(1,0,0,1)
		   
        #turn off red LED
		#GPIO.output(27,False)
		self.setMode1(0,0,0,0)

		doorLocked = True

		return doorLocked

	def CloseDoor2(self,doorLocked):
		#audio for door 2 closing
		path = Path('/home/pi/Downloads/CloseDoor2.wav')
		player = OMXPlayer(path, args='-o alsa')
		
		
		#stop go sign(go - 12.5)
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False) 
		GPIO.setup(4, GPIO.OUT)
		
		servo1 = GPIO.PWM(4,50) #50 Hz
		servo1.start(12.5)
		
		#turn on red LED,turn off green
		GPIO.output(20,False)
		GPIO.output(21,True)
			
		for i in range(0,256):
			self.setMode2(1,0,1,0)
			self.setMode2(0,1,1,0)
			self.setMode2(0,1,0,1)
			self.setMode2(1,0,0,1)
        #turn off red LED
		#GPIO.output(21,False)
		self.setMode2(0,0,0,0)

		doorLocked = True

		return doorLocked
	    
	
if __name__ == "__main__":
	
	
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
	GPIO.setwarnings(False)
	GPIO.setup(A1_1,GPIO.OUT)
	GPIO.setup(A2_1,GPIO.OUT)
	GPIO.setup(B1_1,GPIO.OUT)
	GPIO.setup(B2_1,GPIO.OUT)
	
    
	GPIO.setup(A1_2,GPIO.OUT)
	GPIO.setup(A2_2,GPIO.OUT)
	GPIO.setup(B1_2,GPIO.OUT)
	GPIO.setup(B2_2,GPIO.OUT)
	currentOcc = 30
	maxOcc = 1
	parsed_content = 5
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
	
	check = 0
	
	
	#test entry denial class
	while True:
	  try:
		   url = 'https://occupancy-tracking-system.herokuapp.com/app/True/2'
		   myobj = {'somekey':'somevalue'}
		   #get request
		   x = requests.get(url,data = myobj,headers = {'Referer':'OTS - The Occupancy Detection System'})
		   soup = BeautifulSoup(x.text, "html.parser")
		   #parsed content to string
		   string = str(soup.p)
		   #current occ percentage
		   currentOcc = float(re.findall(r"[-+]?\d*\.\d+|\d+",string)[1])
		   print("WebApp Current Occ Percent:")
		   print(currentOcc)
		   var = EntryDenial()
		   if(currentOcc > maxOcc):
		     doorLocked = var.CloseDoor1(doorLocked)
		   if(currentOcc < maxOcc):
		     doorLocked = var.OpenDoor1(doorLocked)
		   time.sleep(5)
		   
	  except requests.exceptions.RequestException as e:
			   raise SystemExit(e)
	

	"""var.OpenDoor1()
	var.OpenDoor2()
	var.CloseDoor1()
	var.CloseDoor2()"""
	GPIO.output(17,False)
	GPIO.output(20,False)
	GPIO.output(21,False)
	GPIO.output(27,False)
	
	