from serial import Serial
from time import sleep

if __name__ == "__main__":

    serial_port = "/dev/ttyS0"
    baudrate = 38400

    roboclaw = Serial(serial_port, baudrate, timeout=1)
    
    while True:
    
        roboclaw.write(chr(94))
        sleep(5)
        roboclaw.write(64)
        sleep(5)
        roboclaw.write(0x32)
        sleep(5)
        roboclaw.write(64)
        sleep(5)
        
        roboclaw.write(223)
        sleep(5)
        roboclaw.write(192)
        sleep(5)
        roboclaw.write(160)
        sleep(5)
        roboclaw.write(192)
        sleep(5)