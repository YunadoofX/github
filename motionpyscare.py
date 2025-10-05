import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

RELAY = 37
MOTION = 35

GPIO.setup(RELAY, GPIO.OUT)
GPIO.setup(MOTION, GPIO.IN)

while True:
        something = GPIO.input(MOTION)
        print(something)
        if something == 1:
                GPIO.output(RELAY, GPIO.HIGH)
                GPIO.output(RELAY, GPIO.LOW)
                time.sleep(2)
                GPIO.output(RELAY, GPIO.HIGH)
        time.sleep(.5)
