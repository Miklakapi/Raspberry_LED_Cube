import RPi.GPIO as GPIO


def shift_register(byte: bin):
    for x in range(30):
        GPIO.output(data, (byte >> x) & 1)
        GPIO.output(clock, 1)
        GPIO.output(clock, 0)
    GPIO.output(latch, 1)
    GPIO.output(latch, 0)


class ShiftRegister:
    """
    123
    """

    __data: int = 0
    """Number of data pin"""

    __clock: int = 0
    """Number of clock pin"""

    __latch: int = 0
    """Number of latch pin"""

    def __init__(self) -> None:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        data: int = 19
        clock: int = 13
        latch: int = 6

        GPIO.setup(data, GPIO.OUT)
        GPIO.setup(clock, GPIO.OUT)
        GPIO.setup(latch, GPIO.OUT)

    def __del__(self):
        GPIO.output(self.__data, 0)
        GPIO.output(self.__clock, 0)
        GPIO.output(self.__latch, 0)
