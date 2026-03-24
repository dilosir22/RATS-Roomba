from motors import MotorController
from time import sleep
from time import time as getTime
import keyboard


shouldRun = True
targetFPS = 60
targetTPS = 100

if __name__ == "__main__":

    motors = MotorController()
    motors.set_speed(25)

    stdscr.addstr(0, 0, "Robot running. wasd to move, q to quit.")
    time_init = perf_counter()
    while True:
        key = stdscr.getch()
        fw = 0
        lr = 0
        if key == ord("q"): break
        if key == ord("w"): fw += 1
        if key == ord("s"): fw -= 1
        if key == ord("a"): lr = -1
        if key == ord("d"): lr += 1

        if(targetFPS <= 0 or frames >= 1):
            speed = 0
            if keyboard.is_pressed("w"):
                motors.forward(50)
            elif keyboard.is_pressed("s"):
                motors.reverse(50)
            
            if keyboard.is_pressed("esc"):
                shouldRun = False
            
            frames -= 1

        if(ticks >= 1):
            #run tick
            motors.update_both()
            ticks -= 1
        
        previous = now

        motors.update_both()

    motors.cleanup()

if __name__ == "__main__":
    curses.wrapper(main)
        
        