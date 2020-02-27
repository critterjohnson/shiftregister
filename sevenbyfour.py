# sevenbyfour.py - control 4 seven segment displays
from sevensegment import SevenSegment
from shiftregister import ShiftRegister
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sel1 = 14 # sel1 is the first bit (leftmost)
sel2 = 15 # sel2 is the second bit (rightmost)

ser = 18
rclk = 23
srclk = 24

GPIO.setup([sel1, sel2], GPIO.OUT)

shift = ShiftRegister(18, 23, 24)
display = SevenSegment(shift)

# digits should be a list of digits to display, dps should be a list of bools
def disp(digits, dps):
    digits.reverse()
    while True:
        for i in range(4):
            binarysel = bin(i)[2:]
            if len(binarysel) < 2:
                binarysel = "0" + binarysel
            GPIO.output(sel1, int(binarysel[0]))
            GPIO.output(sel2, int(binarysel[1]))
            display.display(digits[i], dps[i])
            time.sleep(0.001)

def main():
    try:
        disp(["A","A","A","A"], [False,False,False,False])
    except KeyboardInterrupt:
        GPIO.output([sel1, sel2], GPIO.LOW)

if __name__ == "__main__":
    main()
