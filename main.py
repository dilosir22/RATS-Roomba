from motors import MotorController
from time import perf_counter
import curses

def main(stdscr: curses.window):
    motors = MotorController()
    motors.set_speed(25)

    stdscr.nodelay(True)
    stdscr.timeout(50)

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

        stdscr.move(1, 0)
        stdscr.clrtoeol()
        if lr == -1:
            stdscr.addstr(1, 0, "Moving left") 
            motors.left()
        elif lr == 1: 
            stdscr.addstr(1, 0, "Moving right") 
            motors.right()
        elif fw == 1: 
            stdscr.addstr(1, 0, "Moving forward") 
            motors.forward()
        elif fw == -1: 
            stdscr.addstr(1, 0, "Moving backward") 
            motors.reverse()

        elif fw == 0 and lr == 0:
            stdscr.addstr(1, 0, "Braking") 
            motors.brake()

        #curses.flushinp()
        #motors.update_both()

    motors.cleanup()

if __name__ == "__main__":
    curses.wrapper(main)
        
        