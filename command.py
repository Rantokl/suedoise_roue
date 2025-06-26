from microbit import *
import radio

def read_joy():
  return pin1.read_analog(), pin2.read_analog(), pin8.read_digital()

radio.config(channel=7)
red = 0
green = 0
blue = 0
nocol = 0

while True:
    if pin15.read_digital()==1:
        while pin15.read_digital():
            radio.send("button,droite")

    elif pin16.read_digital()==1:
        while pin16.read_digital():
            radio.send("button,gauche")

    else:
        x,y,d = read_joy()
        txt = "joy"+str(x)+','+str(y)+','+str(d)
        radio.send(txt)
        pass