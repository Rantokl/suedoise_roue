from roboclaw_3 import Roboclaw
from time import sleep


moteur12 = Roboclaw("/dev/ttyACM1", 38400)
moteur34 = Roboclaw("/dev/ttyACM2", 38400)
address = 0x80
moteur12.Open()
moteur34.Open()

def marche_avant(vitesse):
    moteur12.BackwardM1(address,vitesse) 
    moteur12.ForwardM2(address,vitesse)
    moteur34.ForwardM2(address,vitesse)
    moteur34.BackwardM1(address,vitesse)
    
def marche_arriere(vitesse):
    moteur34.ForwardM1(address,vitesse)
    moteur34.BackwardM2(address,vitesse)
    moteur12.BackwardM2(address,vitesse)
    moteur12.ForwardM1(address,vitesse)
    
    
def deplacer_gauche(vitesse):
    moteur12.BackwardM1(address,vitesse)
    moteur12.ForwardM2(address,vitesse)
    moteur34.BackwardM2(address,vitesse)
    moteur34.ForwardM1(address,vitesse)

def deplacer_droite(vitesse):
    moteur12.ForwardM1(address,vitesse) 
    moteur12.BackwardM2(address,vitesse)
    moteur34.ForwardM2(address,vitesse)
    moteur34.BackwardM1(address,vitesse)

def stop(): 
    moteur12.ForwardM1(address,0)
    moteur12.ForwardM2(address,0)
    moteur34.ForwardM2(address,0)
    moteur34.ForwardM1(address,0)

def tourner_gauche(vitesse):
    moteur12.BackwardM1(address,vitesse)
    moteur12.ForwardM2(address,vitesse)
    moteur34.ForwardM2(address,vitesse)
    moteur34.BackwardM1(address,vitesse)

def tourner_droite(vitesse):
    moteur12.ForwardM1(address,vitesse) 
    moteur12.BackwardM2(address,vitesse)
    moteur34.BackwardM2(address,vitesse)
    moteur34.ForwardM1(address,vitesse)



    
