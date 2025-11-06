from gpiozero import PWMLED
from time import sleep
from time import time

class MotorController:
    def __enter__(self):
        self.left = PWMLED(17)
        self.right = PWMLED(18)
        self.update_motors(0, 0)
        return self
    
    def __exit__(self):
        self.update_motors(0, 0)

    def update_motors(self, left_value, right_value):
        self.left.value = left_value
        self.right.value = right_value

    
