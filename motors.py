# import RPi.GPIO if it exists: otherwise simulate it
try:
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

from time import sleep, monotonic

PIN_R_PWM = 18
PIN_R_CNTRL_1 = 17
PIN_R_CNTRL_2 = 27

PIN_L_PWM = 12
PIN_L_CNTRL_1 = 5
PIN_L_CNTRL_2 = 6

TURN_SLOW_WHEEL_SPEED_MULT = 0.2
SAFETY_BRAKE_TIME = 0.5

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

    def set_dc(self, dc):
        if dc is None: return
        dc = min(dc, 100) #A simple clamp
        dc = max(dc, 0)
        self.pwm.ChangeDutyCycle(dc)
    
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
        del self.pwm # have to do this or python blows up on shutdown

class MotorController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.right_motor = Motor(PIN_R_PWM, PIN_R_CNTRL_1, PIN_R_CNTRL_2)
        self.left_motor = Motor(PIN_L_PWM, PIN_L_CNTRL_1, PIN_L_CNTRL_2)

        self.left_speed = 1
        self.right_speed = 1
        self.speed = 100

        self.direction = 0
        self.forward_timestamp = monotonic()
        self.reverse_timestamp = monotonic()

    def update_state(self, new_dir):
        if (self.direction == 1 and new_dir != 1):
            self.forward_timestamp = monotonic()

        if (self.direction == -1 and new_dir != -1):
            self.reverse_timestamp = monotonic()

        self.direction = new_dir


    def safe_brake_if_needed(self, new_dir):
        self.update_state(new_dir)

        now = monotonic()
        if (new_dir == 1):
            since_reverse = now - self.reverse_timestamp
            if (since_reverse < SAFETY_BRAKE_TIME):
                self.safety_brake()
                sleep(SAFETY_BRAKE_TIME - since_reverse)

        if (new_dir == -1):
            since_forward = now - self.forward_timestamp
            if (since_forward < SAFETY_BRAKE_TIME):
                self.safety_brake()
                sleep(SAFETY_BRAKE_TIME - since_forward)

    def forward(self):
        self.safe_brake_if_needed(1)

        self.left_speed = 1
        self.right_speed = 1

        self.update_speed(self.speed)

        self.right_motor.forward()
        self.left_motor.forward()

    def reverse(self):
        self.safe_brake_if_needed(-1)
        
        self.left_speed = 1
        self.right_speed = 1

        self.update_speed(self.speed)

        self.right_motor.reverse()
        self.left_motor.reverse()

    def right(self):
        self.left_speed = 1
        self.right_speed = TURN_SLOW_WHEEL_SPEED_MULT
        self.update_speed(self.speed)

    def left(self):
        self.left_speed = TURN_SLOW_WHEEL_SPEED_MULT
        self.right_speed = 1
        self.update_speed(self.speed)

    def update_speed(self, speed):
        self.speed = speed
        self.right_motor.set_dc(self.right_speed * self.speed)
        self.left_motor.set_dc(self.left_speed * self.speed)

    def brake(self):
        self.update_state(0)
        self.right_motor.brake()
        self.left_motor.brake()
        self.direction = 0

    def safety_brake(self):
        self.right_motor.brake()
        self.left_motor.brake()

    def float(self):
        self.update_state(0)
        self.right_motor.float()
        self.left_motor.float()
        self.direction = 0

    def cleanup(self):
        self.right_motor.cleanup()
        self.left_motor.cleanup()
        GPIO.cleanup()
        

    
