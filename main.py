from motors import MotorController
from time import sleep

if __name__ == "__main__":
    
    motors = MotorController()

    print("Forward 25%")
    motors.right_motor.forward(25)
    sleep(2)
    
    print("Forward 50%")
    motors.right_motor.forward(50)
    sleep(2)

    print("Forward 75%")
    motors.right_motor.forward(75)
    sleep(2)

    print("Forward 100%")
    motors.right_motor.forward(100)
    sleep(2)

    print("Brake")
    motors.right_motor.brake()
    motors.cleanup()
        
        