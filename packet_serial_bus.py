from roboclaw_3 import Roboclaw
from time import sleep
from motors import *
from serial_test import get_direction
import serial

# Remplace ttyACM0 par le port correspondant si besoin
ser = serial.Serial('/dev/ttyACM0', 115200)

while True :
    data = ser.readline().decode('utf-8').strip()
    #print("data {}".format(data))
    data_str = data.split(',')
    if data_str[0]=="joy":
        dx,dy,direction = get_direction(int(data_str[1]), int(data_str[2]))
        if direction=="haut" :
            print("Avancer")
            marche_avant(dy)
            
        elif direction == "bas":
            marche_arriere(-1*dy)
            print("Reculer")
        elif direction == "gauche":
            deplacer_gauche(-1*dx)
            print("Tourner a gauche")
            
        elif direction == "droite":
            deplacer_droite(dx)
            print("Tourner a droite")
            
        elif direction == "repos":
            stop()
            print("Arreter")

    if data_str[0]=="button":
        if data_str[1]=="droite":
            tourner_droite(14)
        elif data_str[1]=="gauche":
            tourner_gauche(14)
    
    


