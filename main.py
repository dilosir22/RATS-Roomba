from motors import MotorController
from time import sleep

if __name__ == "__main__":
    with MotorController() as motors:
        motors.right_motor.forward()
        sleep(2)
        motors.right_motor.brake()
        sleep(1)
        motors.right_motor.reverse()
        sleep(2)
        