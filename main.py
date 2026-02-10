from motors import MotorController
from time import sleep

if __name__ == "__main__":
    
    motors = MotorController()

    print("Forward!")
    motors.right_motor.forward()
    sleep(2)
    print("Brake!")
    motors.right_motor.brake()
    sleep(1)
    print("Reverse!")
    motors.right_motor.reverse()
    sleep(2)
    print("Brake!")
    motors.right_motor.brake()

    motors.cleanup()
        
        