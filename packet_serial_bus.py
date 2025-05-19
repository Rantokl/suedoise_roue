from roboclaw_3 import Roboclaw
from time import sleep
from motors import *
import serial

# Remplace ttyACM0 par le port correspondant si besoin
ser = serial.Serial('/dev/ttyACM0', 115200)

while True :
    data = ser.readline().decode('utf-8').strip()
    #print("data {}".format(data))
    if data=="haut" :
        print("Avancer")
        marche_avant(16)
        
    elif data == "bas":
        marche_arriere(16)
        print("Reculer")
    elif data == "gauche":
        tourner_gauche(16)
        print("Tourner a gauche")
        
    elif data == "droite":
        tourner_droite(16)
        print("Tourner a droite")
        
        
    if not data:
        print("Arreter")
        stop()
    
    


