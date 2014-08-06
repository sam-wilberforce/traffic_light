#!/usr/bin/python2.7

import RPi.GPIO as GPIO
import time
import sys

# pin 16 = green
# pin 15 = yellow
# pin 11 = red

def usage():
	print('Enter the number of times per second the LED will blink')
	print('Usage: python blink.py 20')

if(len(sys.argv) != 2):
	print('Incorrect arguments supplied')
	usage()
else:
	num = int(sys.argv[1])
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD) #use pin numbering rather than cpu numbering

	#setup gpio pins
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)

	#set all pins off
	GPIO.output(11,False)
	GPIO.output(15,False)
	GPIO.output(16,False)

	while True:
		GPIO.output(11,True) #red on
		time.sleep(num + 5) #wait on red
		GPIO.output(15,True) #amber on
		time.sleep(num)
		GPIO.output(11,False)
		GPIO.output(15,False)
		GPIO.output(16,True) #red,amber off, green on
		time.sleep(num + 5) #wait on green
		GPIO.output(16,False)
		GPIO.output(15,True) #green off, amber on
		time.sleep(num)
		GPIO.output(15,False) #amber off
	GPIO.cleanup()
