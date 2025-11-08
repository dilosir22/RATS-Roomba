import RPi.GPIO as GPIO
from time import sleep
from time import time

PIN_PWM = 18
PIN_CONTROL_A = 17
PIN_CONTROL_B = 27

class MotorController:
    def __enter__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_PWM, GPIO.OUT)
        self.pwm = GPIO.PWM(PIN_PWM, 1000)
        self.pwm.start(50)

        return self
    
    def brake(self):
        GPIO.output(PIN_CONTROL_A, GPIO.LOW)
        GPIO.output(PIN_CONTROL_B, GPIO.LOW)
    
    def float(self):
        GPIO.output(PIN_CONTROL_A, GPIO.HIGH)
        GPIO.output(PIN_CONTROL_B, GPIO.HIGH)

    def forward(self):
        GPIO.output(PIN_CONTROL_A, GPIO.HIGH)
        GPIO.output(PIN_CONTROL_B, GPIO.LOW)

    def reverse(self):
        GPIO.output(PIN_CONTROL_A, GPIO.LOW)
        GPIO.output(PIN_CONTROL_B, GPIO.HIGH)
    
    def __exit__(self):
        self.left.stop()
        GPIO.cleanup()

    
