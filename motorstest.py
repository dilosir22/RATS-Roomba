from motors import *
from time import sleep

motors = MotorController()
motors.update_speed(25)

motors.forward()
sleep(1)
motors.brake()
sleep(1)

motors.reverse()
sleep(1)
motors.brake()
sleep(1)

motors.left()
sleep(1)
motors.brake()
sleep(1)

motors.right()
sleep(1)
motors.brake()
sleep(1)

