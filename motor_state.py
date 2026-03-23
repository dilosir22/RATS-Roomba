from enum import Enum
from time import monotonic

# motor statemachine logic, 
# to ensure that there is always a brake between direction changes but as little delay as possible

SAFETY_BRAKE_TIME = 0.1

class Direction(Enum):
    BRAKE = 0
    FLOAT = 1
    FORWARD = 2
    REVERSE = 3

class _State(Enum):
    BRAKE = 0
    FLOAT = 1
    FORWARD = 2
    REVERSE = 3
    WAIT_FROM_FORWARD = 4
    WAIT_FROM_REVERSE = 5

# The state machine has the above states. Transitions are predictable and for the most part immediate.
# There are two exceptions: leaving the forward or reverse state goes to a wait state that can act as BRAKE or FLOAT depending on input
class MotorStateController:
    def __init__(self, start_direction = Direction.FLOAT):
         self.state = _State(start_direction.value)
         self.last_input = start_direction
         self.wait_start_time = monotonic()


    def update(self, input: Direction = None):
        if (input is None):
            input = self.last_input
        self.last_input = input

        self.__update_state(input)

    def update_and_get(self, input: Direction = None) -> Direction:
        self.update(input)
        return self.__get_value(input)

    def __update_state(self, input: Direction):
        if (self.state.value == input.value):
            pass

        elif (self.state == _State.WAIT_FROM_FORWARD and input == Direction.FORWARD):
            self.state = _State.FORWARD

        elif (self.state == _State.WAIT_FROM_REVERSE and input == Direction.REVERSE):
            self.state = _State.REVERSE

        elif (self.state == _State.WAIT_FROM_FORWARD or self.state == _State.WAIT_FROM_REVERSE):
            dt = monotonic() - self.wait_start_time
            if (dt >= SAFETY_BRAKE_TIME):
                self.state = _State(input.value)

        elif (self.state == _State.Forward):
            self.state = _State.WAIT_FROM_FORWARD
            self.wait_start_time = monotonic()
        
        elif (self.state == _State.Reverse):
            self.state = _State.WAIT_FROM_REVERSE
            self.wait_start_time = monotonic()

    def __get_value(self, input: Direction) -> Direction:
        match self.state:
            case _State.BRAKE:
                return Direction.BRAKE
            case _State.FLOAT:
                return Direction.FLOAT
            case _State.FORWARD:
                return Direction.FORWARD
            case _State.REVERSE:
                return Direction.REVERSE
            case _State.WAIT_FROM_FORWARD | _State.WAIT_FROM_REVERSE:
                return Direction.FLOAT if input is Direction.FLOAT else Direction.BRAKE

        

        