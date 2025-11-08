import RPi.GPIO as GPIO
from time import sleep
from time import time

PIN_R_PWM = 18
PIN_R_CNTRL_1 = 17
PIN_R_CNTRL_2 = 27

class Motor:
    def __init__(self, pin_pwm, pin_cntrl_1, pin_cntrl_2):
        self.pin_pwm = pin_pwm
        self.pin_cntrl_1 = pin_cntrl_1
        self.pin_cntrl_2 = pin_cntrl_2

        GPIO.setup(self.pin_pwm, GPIO.OUT)
        GPIO.setup(self.pin_cntrl_1, GPIO.OUT)
        GPIO.setup(self.pin_cntrl_2, GPIO.OUT)

        self.pwm = GPIO.PWM(self.pin_pwm, 1000)
        self.pwm.start(50)
    
    def brake(self):
        GPIO.output(self.pin_cntrl_1, GPIO.LOW)
        GPIO.output(self.pin_cntrl_2, GPIO.LOW)
    
    def float(self):
        GPIO.output(self.pin_cntrl_1, GPIO.HIGH)
        GPIO.output(self.pin_cntrl_2, GPIO.HIGH)

    def forward(self):
        GPIO.output(self.pin_cntrl_1, GPIO.HIGH)
        GPIO.output(self.pin_cntrl_2, GPIO.LOW)

    def reverse(self):
        GPIO.output(self.pin_cntrl_1, GPIO.LOW)
        GPIO.output(self.pin_cntrl_2, GPIO.HIGH)

    def cleanup(self):
        self.pwm.stop()

class MotorController:
    def __enter__(self):
        GPIO.setmode(GPIO.BCM)
        self.right_motor = Motor(PIN_R_PWM, PIN_R_CNTRL_1, PIN_R_CNTRL_2)

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.right_motor.cleanup()
        GPIO.cleanup()
        return False # do not suppress exceptions
        

    
