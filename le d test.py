from gpiozero import PWMLED
from time import sleep
from time import time

red = PWMLED(17)
blue = PWMLED(18)


def main():
    while True:
        red.value = 1
        blue.value = 1
        sleep(1)
        red.value = 0
        blue.value = 0
        sleep(1)

def end():
    red.value = 0
    blue.value = 0
    
    
if __name__ == "__main__":
    try: main()
    except: pass
    finally: end()

    
