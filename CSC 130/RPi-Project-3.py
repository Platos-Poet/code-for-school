#########################################################################
# name: Logan Stelter
# date: 10/22/22
# description: A program that takes a button input on a breaboard and
# changes an LED output while the button is pressed
#########################################################################

import RPi.GPIO as GPIO
from time import sleep


led = 18
button = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while(True):
    if (GPIO.input(button) == GPIO.HIGH):
        GPIO.output(led, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(led, GPIO.LOW)
        sleep(0.1)
    else:
        GPIO.output(led, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(led, GPIO.LOW)
        sleep(0.5)
