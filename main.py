from motors import MotorController
from time import perf_counter
import curses

def main(stdscr: curses.window):
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

        if lr == -1: motors.left()
        elif lr == 1: motors.right()
        elif fw == 1: motors.forward()
        elif fw == -1: motors.reverse()

        motors.update_both()

    motors.cleanup()

if __name__ == "__main__":
    curses.wrapper(main)
        
        