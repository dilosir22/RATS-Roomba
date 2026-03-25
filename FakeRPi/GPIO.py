OUT = 0
LOW = 0
HIGH = 1
BCM = 0

# fake pwm
class PWMClass:

    def __init__(self):
        pass

    def start(self, dc):
        pass

    def ChangeDutyCycle(self, dc):
        pass

    def stop(self):
        pass

def setmode(mode):
    pass

def setup(pin, mode):
    pass

def PWM(pin, rate):
    return PWMClass()

def output(pin, level):
    pass

def cleanup():
    pass