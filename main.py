from motors import MotorController
from time import sleep

if __name__ == "__main__":
    with MotorController() as motors:
        while True: sleep(1)