from motors import MotorController
from time import sleep
from time import time as getTime
from pynput import keyboard

w_down = False
s_down = False

shouldRun = True
targetFPS = 60
targetTPS = 60


def on_pressed(key, injected):
    if key == keyboard.Key.esc:
        shouldRun = False
    if key == 'w':
        w_down = True
    if key == 's':
        s_down = True

def on_released(key, injected):
    if key == 'w':
        w_down = False
    if key == 's':
        s_down = False


if __name__ == "__main__":

    litsener = keyboard.Listener(on_pressed, on_released)
    litsener.start()

    motors = MotorController()

    now = 0
    previous = getTime()
    steps, frames = 0, 0
    while shouldRun:
        now = getTime()
        dtime = now - previous
        ticks += dtime * targetTPS
        frames += dtime * targetFPS

        if(targetFPS <= 0 or frames >= 1):
            speed = 0
            if w_down:
                motors.forward(50)
            elif s_down:
                motors.reverse(50)
            
            if keyboard.is_pressed("esc"):
                shouldRun = False
            
            frames -= 1

        if(ticks >= 1):
            #run tick
            motors.update_both()
            ticks -= 1
        
        previous = now


    motors.cleanup()
        
        