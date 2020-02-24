# sevenbyfour.py - control 4 seven segment displays
from sevensegment import SevenSegment
from shiftregister import ShiftRegister
import RPi.GPIO as GPIO

sel1 = 0
sel2 = 0

shift = ShiftRegister(0, 0, 0)
displays = [SevenSegment(shift),
            SevenSegment(shift),
            SevenSegment(shift),
            SevenSegment(shift)
        ]

# digits should be a list of digits to display, dps should be a list of bools
def disp(digits, dps):
    for i, display in enumerate(displays):
        binarysel = bin(i)[2:]
        GPIO.output(sel1, binarysel[0])
        GPIO.output(sel2, binarysel[1])
        display.display(digits[i], dps[i])
