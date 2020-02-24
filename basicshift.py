from shiftregister import ShiftRegister

ser   = 2
oe    = 3
rclk  = 4
srclk = 17
srclr = 27
    
sr = ShiftRegister(ser, oe, rclk, srclk, srclr)
