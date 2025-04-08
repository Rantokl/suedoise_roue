import time
from roboclaw_3 import Roboclaw

#Windows comport name
rc = Roboclaw("/dev/ttyS0",38400)
#Linux comport name
#rc = Roboclaw("/dev/ttyACM0",115200)

if(rc):
	print("Roboclaw connected")

rc.Open()
address = 0x80


for i in range(0,8):
    rc.ForwardM1(address,i*4)
    time.sleep(0.5)	#1/4 power forward
	# rc.BackwardM2(address,64)
	# print("Backward")	#1/4 power backward
	