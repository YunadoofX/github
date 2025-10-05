import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

RELAY = 37

GPIO.setup(RELAY, GPIO.OUT)


GPIO.output(RELAY, GPIO.HIGH)
GPIO.output(RELAY, GPIO.LOW)
time.sleep(2)
GPIO.output(RELAY, GPIO.HIGH)

