import serial
from motors import *
from roboclaw_3 import Roboclaw 
# Remplace ttyACM0 par le port correspondant si besoin
ser = serial.Serial('/dev/ttyACM0', 115200)

def joystick_to_scale(value):
    if value >= 569 and  value <=590 :
        return 0

    if value > 590:
        #print(str(int((value - 590) * 64 / (1023 - 590))))
        return int((value - 590) * 64 / (1023 - 590))

    if value < 570:
        #print(str(int((value - 590) * 64 / (1023 - 590))))
        return int((value-570) * 64 / 570)



def get_direction(x, y):
    dx = joystick_to_scale(x)
    dy = joystick_to_scale(y)
    #print(dx)
    direction = "repos"

    if dx == 0 and dy == 0:
        direction = "repos"

    if dx > 0 and dy == 0:
        direction = "droite"

    if dx < 0 and dy == 0:
        direction = "gauche"
    if dx == 0 and dy > 0:
        direction = "haut"
    if dx == 0 and dy < 0:
        direction = "bas"
    if dx > 0 and dy > 0:
        direction = "haut-droite"
    if dx < 0 and dy > 0:
        direction = "haut-gauche"
    if dx > 0 and dy < 0:
        direction = "bas-droite"
    if dx < 0 and dy < 0:
        direction = "bas-gauche"

    print(f"Valeurs converties : X = {dx}, Y = {dy} -> Direction : {direction}")
    return dx, dy, direction







#print("Lecture depuis le micro:bit...")
#while True:

    #data = ser.readline().decode('utf-8').strip()
    #data_str =data.split(',')
    #print(str(int((int(data_str[0])-570)*64)/(1023-590)))
    #dx,dy,direction = get_direction(int(data_str[0]), int(data_str[1]))
    #if direction == "repos":
    #    stop()

    #if direction == "haut":
    #    marche_avant(dy)
    
    #if direction == "bas":
    #    marche_arriere(-1*dy)

    #if direction == "gauche":
    #    tourner_gauche(-1*dx)

    #if direction == "droite":
    #    tourner_droite(dx)
