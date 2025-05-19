from roboclaw_3 import Roboclaw
from time import sleep
from motors import *
import serial

# Remplace ttyACM0 par le port correspondant si besoin
ser = serial.Serial('/dev/ttyACM0', 115200)

while True :
    data = ser.readline().decode('utf-8').strip()
    while data=="haut" :

        marche_avant(16)
        break
    while data == "bas":
        marche_arriere(16)
        break
    while data == "gauche":
        tourner_gauche(16)
        break
    while data == "gauche":
        tourner_droite(16)
        break
        
    stop()
    
    


