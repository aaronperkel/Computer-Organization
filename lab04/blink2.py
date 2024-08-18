import RPi.GPIO as GPIO
import time

rPIN = 18
yPIN = 15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(rPIN, GPIO.OUT)
GPIO.setup(yPIN, GPIO.OUT)


def blink(t, pin1, pin2):
	cycle = 0
	while cycle < 20:
		GPIO.output(pin1, GPIO.HIGH)
		GPIO.output(pin2, GPIO.LOW)
		time.sleep(t)
		GPIO.output(pin1, GPIO.LOW)
		GPIO.output(pin2, GPIO.HIGH)
		time.sleep(t)
		cycle += 1


blink(2, rPIN, yPIN)
