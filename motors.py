import RPi.GPIO as GPIO
from enum import Enum
from time import monotonic, sleep

PIN_R_PWM = 18
PIN_R_CNTRL_1 = 17
PIN_R_CNTRL_2 = 27

PIN_L_PWM = 12
PIN_L_CNTRL_1 = 5
PIN_L_CNTRL_2 = 6

SAFETY_BRAKE_TIME = 0.1

class Motor:
    def __init__(self, pin_pwm, pin_cntrl_1, pin_cntrl_2):
        self.pin_pwm = pin_pwm
        self.pin_cntrl_1 = pin_cntrl_1
        self.pin_cntrl_2 = pin_cntrl_2

        GPIO.setup(self.pin_pwm, GPIO.OUT)
        GPIO.setup(self.pin_cntrl_1, GPIO.OUT)
        GPIO.setup(self.pin_cntrl_2, GPIO.OUT)

        self.pwm = GPIO.PWM(self.pin_pwm, 1000)
        self.pwm.start(0)
        self.float()

    def set_speed(self, speed):
        speed = min(speed, 100) #A simple clamp
        speed = max(speed, 0)
        self.pwm.ChangeDutyCycle(speed)
    
    def brake(self):
        GPIO.output(self.pin_cntrl_1, GPIO.LOW)
        GPIO.output(self.pin_cntrl_2, GPIO.LOW)
    
    def float(self):
        GPIO.output(self.pin_cntrl_1, GPIO.HIGH)
        GPIO.output(self.pin_cntrl_2, GPIO.HIGH)

    def forward(self, speed = 50):
        self.set_speed(speed)

        GPIO.output(self.pin_cntrl_1, GPIO.HIGH)
        GPIO.output(self.pin_cntrl_2, GPIO.LOW)

    def reverse(self, speed = 50):
        self.set_speed(speed)

        GPIO.output(self.pin_cntrl_1, GPIO.LOW)
        GPIO.output(self.pin_cntrl_2, GPIO.HIGH)

    def cleanup(self):
        self.pwm.stop()
        del self.pwm

class MotorController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.right_motor = Motor(PIN_R_PWM, PIN_R_CNTRL_1, PIN_R_CNTRL_2)
        self.left_motor = Motor(PIN_L_PWM, PIN_L_CNTRL_1, PIN_L_CNTRL_2)

    def cleanup(self):
        self.right_motor.cleanup()
        self.left_motor.cleanup()
        GPIO.cleanup()
        

    
