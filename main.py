from motors import MotorController
from time import sleep
from time import time as getTime
import keyboard


def update(dtime):

    return

shouldRun = True
targetFPS = 60
targetTPS = 100



if __name__ == "__main__":

    motors = MotorController()

    now = 0
    previous = getTime()
    steps = 0, frames = 0
    while shouldRun:
        now = getTime()
        dtime = now - previous
        ticks += dtime * targetTPS
        frames += dtime * targetFPS

        if(targetFPS <= 0 or frames >= 1):
            speed = 0
            if keyboard.is_pressed("w"):
                motors.forward(50)
            elif keyboard.is_pressed("s"):
                motors.reverse(50)
            
            frames -= 1

        if(ticks >= 1):
            #run tick
            motors.update_both()
            ticks -= 1
        
        previous = now


    motors.cleanup()
        
        