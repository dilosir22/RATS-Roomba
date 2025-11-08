import RPi.GPIO as GPIO
from time import sleep
from time import time

PIN_R_PWM = 18
PIN_R_CNTRL_1 = 17
PIN_R_CNTRL_2 = 27

class MotorController:
    def __enter__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_R_PWM, GPIO.OUT)
        self.pwm = GPIO.PWM(PIN_R_PWM, 1000)
        self.pwm.start(50)

        return self
    
    def brake(self):
        GPIO.output(PIN_R_CNTRL_1, GPIO.LOW)
        GPIO.output(PIN_R_CNTRL_2, GPIO.LOW)
    
    def float(self):
        GPIO.output(PIN_R_CNTRL_1, GPIO.HIGH)
        GPIO.output(PIN_R_CNTRL_2, GPIO.HIGH)

    def forward(self):
        GPIO.output(PIN_R_CNTRL_1, GPIO.HIGH)
        GPIO.output(PIN_R_CNTRL_2, GPIO.LOW)

    def reverse(self):
        GPIO.output(PIN_R_CNTRL_1, GPIO.LOW)
        GPIO.output(PIN_R_CNTRL_2, GPIO.HIGH)
    
    def __exit__(self):
        self.pwm.stop()
        GPIO.cleanup()

    
