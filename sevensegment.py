# a seven segment display attatched to a shift register
from shiftregister import ShiftRegister

MAP = {
        #  : "ABCDEFG"
        "1": "0110000",
        "2": "1101101",
        "3": "1111001",
        "4": "0110011",
        "5": "1011011",
        "6": "1011111",
        "7": "1110000",
        "8": "1111111",
        "9": "1110011",
        "A": "1110111",
        "B": "0011111",
        "C": "1001110",
        "D": "0111101",
        "E": "1001111",
        "F": "1000111"
    }
class SevenSegment:
    def __init__(self, shift):
        self.shift = shift
    
    def display(self, digit, dp=False):
        binary = MAP[str(digit)]
        if dp:
            binary += "1"
        else:
            binary += "0"
        self.shift.shift_bits(binary)
        self.shift.update()
