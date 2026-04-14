from motors import MotorController
from time import perf_counter
import curses

def main(stdscr: curses.window):
    motors = MotorController()
    motors.update_speed(25)

    stdscr.nodelay(True)
    #stdscr.timeout(50)

    stdscr.addstr(0, 0, "Robot running. wasd to move, q to quit.")
    while True:
        key = stdscr.getch()
        
        if key != -1:
            stdscr.move(1, 0)
            stdscr.clrtoeol()   
            if key == ord("q"): break
            elif key == ord("w"): 
                stdscr.addstr(1, 0, "forward!")
                motors.forward()
            elif key == ord("s"): 
                stdscr.addstr(1, 0, "back!")
                motors.reverse()
            elif key == ord("a"): 
                stdscr.addstr(1, 0, "left!")
                motors.left()
            elif key == ord("d"): 
                stdscr.addstr(1, 0, "right!")
                motors.right()
            else: motors.brake()

    motors.cleanup()

if __name__ == "__main__":
    curses.wrapper(main)
        
        