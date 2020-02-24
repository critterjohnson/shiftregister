import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
from time import sleep

class ShiftRegister:
    def __init__(self, ser, rclk, srclk,  oe=None, srclr=None):
        self.ser   = ser
        self.oe    = oe
        self.rclk  = rclk
        self.srclk = srclk
        self.srclr = srclr
        GPIO.setup(self.ser, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.rclk, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.srclk, GPIO.OUT, initial=GPIO.LOW)
        if self.oe is not None:
            GPIO.setup(self.oe, GPIO.OUT, initial=GPIO.LOW)
        if self.srclr is not None:
            GPIO.setup(self.srclr, GPIO.OUT, initial=GPIO.HIGH)
        
    @staticmethod
    def pulse(pin, delay=0):
        GPIO.output(pin, GPIO.HIGH)
        sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        sleep(delay)
        
    @staticmethod
    def endall():
        GPIO.cleanup()
    
    def update_storage(self):
        self.pulse(self.rclk)
        
    def shift_bit(self, num, delay=0, update_on_pulse=False):
        if num != "0" and num != "1":
            raise ValueError("num can only be '0' or '1'.")
    
        num = int(num)
            
        GPIO.output(self.ser, num)
        sleep(delay)
        
        self.pulse(self.srclk, delay)
        if (update_on_pulse):
            self.pulse(self.rclk, delay)
    
    def shift_bits(self, bits, delay=0, update_on_pulse=False):
        for bit in bits:
            self.shift_bit(bit, delay, update_on_pulse)

    def shift_num(self, num, byteorder="small", delay=0, update_on_pulse=False):
        binary_num = bin(num)[2:]
        bits_to_byte = lambda x: 8*((x+7)//8) - x
        binary = (bits_to_byte(len(binary_num)) * "0") + binary_num
        
        if byteorder == "small":
            self.shift_bits(binary, delay, update_on_pulse)
            return
        elif byteorder == "big":
            byte_num = len(binary) // 8
            byte_list = []
            for i in range(byte_num):
                byte_list.insert(0, (binary[i*8:(i+1)*8]))
            for byte in byte_list:
                self.shift_bits(byte, delay, update_on_pulse)
    
    def output(self, output):
        if output and self.oe is not None:
            GPIO.output(self.oe, GPIO.HIGH)
        elif not output and self.oe is not None:
            GPIO.output(self.oe, GPIO.LOW)
    
    def clear(self):
        if self.srclr is not None:
            GPIO.output(self.srclr, GPIO.LOW)
            GPIO.output(self.srclr, GPIO.HIGH)
    
    def update(self):
        ShiftRegister.pulse(self.rclk)

def main():
    pass
