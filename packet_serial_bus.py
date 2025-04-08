from roboclaw_3 import Roboclaw
from time import sleep

address = 0x80
roboclaw = Roboclaw("/dev/ttyACM0", 38400)
roboclaw.Open()

while True:
    
    
        
    roboclaw.ForwardM1(address,32)
    roboclaw.ForwardM2(address,32)
    #roboclaw.ForwardM2(address,64)
    sleep(2)
    roboclaw.ForwardM1(address,0)
    roboclaw.ForwardM2(address,0)
    #roboclaw.ForwardM2(address,0)
    sleep(2)
    roboclaw.BackwardM1(address,32)
    roboclaw.BackwardM2(address,32)
    #roboclaw.ForwardM2(address,64)
    sleep(2)
    roboclaw.ForwardM1(address,0)
    roboclaw.ForwardM2(address,0)
    #roboclaw.ForwardM2(address,0)
    sleep(2)
        
    


