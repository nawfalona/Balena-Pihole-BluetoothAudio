#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import random

def rand_gen():
    return random.uniform(0, 1)


# Set GPIO mode: GPIO.BCM or GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# GPIO pins list based on GPIO.BOARD
# Order: red, yellow, green, green, yellow, red
gpioList0 = [11,13,15,19,21,23]
red = [11,23]
red_r = 23
red_l = 11
yellow = [13,21]
yellow_r = 21
yellow_l = 13
green = [15,19]
green_r = 19
green_l = 15
# Set mode for each gpio pin
GPIO.setup(gpioList0, GPIO.OUT)

#Test LEDS
GPIO.output(gpioList0, 1)
time.sleep(5)
GPIO.output(gpioList0, 0)
time.sleep(1)

while True:
    GPIO.output(yellow_l, 1)
    time.sleep(0.2)
    GPIO.output(green_r, 1)
    time.sleep(0.2)
    GPIO.output(green_l, 1)
    time.sleep(0.2)
    GPIO.output(yellow_r, 1)
    time.sleep(0.2)
    GPIO.output(red_l, 1)
    time.sleep(0.2)
    GPIO.output(red_r, 1)
    time.sleep(0.2)


    GPIO.output(green_l, 0)
    time.sleep(0.2)
    GPIO.output(yellow_r, 0)
    time.sleep(0.2)
    GPIO.output(red_l, 0)
    time.sleep(0.2)
    GPIO.output(red_r, 0)
    time.sleep(0.2)
    GPIO.output(yellow_l, 0)
    time.sleep(0.2)
    GPIO.output(green_r, 0)
    time.sleep(0.2)
    


# Reset all gpio pin
GPIO.cleanup()
