
from motor_state import *

# import RPi.GPIO if it exists: otherwise simulate it
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

PIN_R_PWM = 18
PIN_R_CNTRL_1 = 17
PIN_R_CNTRL_2 = 27

PIN_L_PWM = 12
PIN_L_CNTRL_1 = 5
PIN_L_CNTRL_2 = 6

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

        self.state = MotorStateController()

        self.float()

    def update(self):
        pass
        #dir = self.state.update_and_get()

        #match dir:
        #    case Direction.BRAKE: self.__brake()
        #    case Direction.FLOAT: self.__float()
        #    case Direction.FORWARD: self.__forward()
        #    case Direction.REVERSE: self.__reverse()

    def set_speed(self, speed):
        if speed is None: return
        speed = min(speed, 100) #A simple clamp
        speed = max(speed, 0)
        self.pwm.ChangeDutyCycle(speed)

    #def brake(self):
    #    self.state.update(Direction.BRAKE)
    
    def brake(self):
        GPIO.output(self.pin_cntrl_1, GPIO.LOW)
        GPIO.output(self.pin_cntrl_2, GPIO.LOW)
        
    #def float(self):
    #    self.state.update(Direction.FLOAT)
    
    def float(self):
        GPIO.output(self.pin_cntrl_1, GPIO.HIGH)
        GPIO.output(self.pin_cntrl_2, GPIO.HIGH)

    #def forward(self, speed = None):
    #    self.set_speed(speed)
    #    self.state.update(Direction.FORWARD)

    def forward(self):
        GPIO.output(self.pin_cntrl_1, GPIO.HIGH)
        GPIO.output(self.pin_cntrl_2, GPIO.LOW)

    #def reverse(self, speed = None):
    #    self.set_speed(speed)
    #    self.state.update(Direction.REVERSE)

    def reverse(self):
        GPIO.output(self.pin_cntrl_1, GPIO.LOW)
        GPIO.output(self.pin_cntrl_2, GPIO.HIGH)

    def cleanup(self):
        self.pwm.stop()
        del self.pwm # have to do this or python blows up on shutdown

class MotorController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.right_motor = Motor(PIN_R_PWM, PIN_R_CNTRL_1, PIN_R_CNTRL_2)
        self.left_motor = Motor(PIN_L_PWM, PIN_L_CNTRL_1, PIN_L_CNTRL_2)

    def forward(self, speed = None):
        self.right_motor.forward()
        self.left_motor.forward()

    def reverse(self, speed = None):
        self.right_motor.reverse()
        self.left_motor.reverse()

    def set_speed(self, speed):
        self.right_motor.set_speed(speed)
        self.left_motor.set_speed(speed)

    def brake(self):
        self.right_motor.brake()
        self.left_motor.brake()

    def float(self):
        self.right_motor.float()
        self.left_motor.float()

    def right(self, speed=None):
        self.right_motor.forward()
        self.left_motor.reverse()

    def left(self, speed=None):
        self.right_motor.reverse()
        self.left_motor.forward()

    def update_both(self):
        self.right_motor.update()
        self.left_motor.update()

    def cleanup(self):
        self.right_motor.cleanup()
        self.left_motor.cleanup()
        GPIO.cleanup()
        

    
