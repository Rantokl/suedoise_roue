from serial import Serial
from time import sleep

if __name__ == "__main__":

    serial_port = "/dev/ttyS0"
    baudrate = 38400

    roboclaw = Serial(serial_port, baudrate, timeout=1)
    
    while True:
    
        roboclaw.write(0x94)
        sleep(5)
        roboclaw.write(0x64)
        sleep(5)
        roboclaw.write(0x32)
        sleep(5)
        roboclaw.write(0x64)
        sleep(5)
        
        roboclaw.write(0x223)
        sleep(5)
        roboclaw.write(0x192)
        sleep(5)
        roboclaw.write(0x160)
        sleep(5)
        roboclaw.write(0x192)
        sleep(5)