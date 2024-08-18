import RPi.GPIO as GPIO
import time

PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)

print("LED On")
GPIO.output(PIN, GPIO.HIGH)

# One second pause for LED on
time.sleep(1)
print("LED Off")
GPIO.output(PIN, GPIO.LOW)
