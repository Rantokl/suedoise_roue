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
    while data == "bas":
        marche_arriere(16)
    while data == "gauche":
        tourner_gauche(16)
    while data == "gauche":
        tourner_droite(16)
        # stop()
        # sleep(0.5)
        #tourner_droite(32)
        #tourner_droite(64)

        #stop()
        #sleep(0.5)
        #tourner_gauche(32)
        #tourner_gauche(64)
        # stop()
        # #sleep(0.5)
        # #marche_arriere(32)
        # #marche_arriere(64)
        # sleep(2)
        # stop()

    else :
        stop()
    
    


