# sevenbyfour.py - control 4 seven segment displays
from sevensegment import SevenSegment
from shiftregister import ShiftRegister

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
        display.display(digits[i], dps[i])
