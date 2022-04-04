#!/usr/bin/env python

"""Temporary file"""

import RPi.GPIO as GPIO
import time

from sequence_loader import SequenceLoader
from shift_register import ShiftRegister
from clock import Clock

sr = ShiftRegister(4)
sl = SequenceLoader()

try:
    sequence = sl.get_sequence_by_name("hourGlass")
    cl = Clock()
    for i in range(sequence['repeat']):
        for j in range(len(sequence['data'])):
            cl.restart()
            while cl.get_elapsed_time().as_seconds() < sequence['delay']:
                for k in range(5):
                    level = "00000"
                    level = level[:k] + '1' + level[(k + 1):]
                    sr.run(level + sequence['data'][j][k] + '00')
                    time.sleep(0.002)
except KeyboardInterrupt:
    sr.clear()
    GPIO.cleanup()
