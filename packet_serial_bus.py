from roboclaw_3 import Roboclaw
from time import sleep

addresses = [0x80,0x81]
roboclaw = Roboclaw("/dev/ttyS0", 38400)
roboclaw.Open()

while True:
    
    for address in addresses:
        
        roboclaw.ForwardM1(address,64)
        roboclaw.ForwardM2(address,64)
        sleep(2)
        roboclaw.ForwardM1(address,0)
        roboclaw.ForwardM2(address,0)
        sleep(2)
        
    


