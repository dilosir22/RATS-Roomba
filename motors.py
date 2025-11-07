import RPi.GPIO as GPIO
from time import sleep
from time import time

PIN_LEFT = 18
PIN_RIGHT = 17

class MotorController:
    def __enter__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_LEFT, GPIO.OUT)
        GPIO.setup(PIN_RIGHT, GPIO.OUT)

        self.left = GPIO.PWM(PIN_LEFT, 1000)
        self.right = GPIO.PWM(PIN_RIGHT, 1000)
        self.left.start(50)
        self.right.start(50)
        return self
    
    def __exit__(self):
        self.left.stop()
        self.right.stop()
        GPIO.cleanup()

    
