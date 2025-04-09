from roboclaw_3 import Roboclaw
from time import sleep


#moteur34 = Roboclaw("/dev/ttyACM0", 115200)
moteur34 = Roboclaw("/dev/ttyS0", 115200)
address1 = 0x80
address2 = 0x81
#moteur34.Open()
moteur34.Open()

def marche_avant(vitesse):
    moteur34.BackwardM1(address1,vitesse) 
    moteur34.ForwardM2(address2,vitesse)
    moteur34.ForwardM2(address1,vitesse)
    moteur34.BackwardM1(address2,vitesse)
    
def marche_arriere(vitesse):
    moteur34.ForwardM1(address1,vitesse)
    moteur34.BackwardM2(address2,vitesse)
    moteur34.BackwardM2(address1,vitesse)
    moteur34.ForwardM1(address2,vitesse)
    
    
def tourner_gauche(vitesse):
    moteur34.ForwardM1(address1,int(vitesse/2))
    moteur34.ForwardM2(address2,vitesse)
    moteur34.BackwardM2(address1,int(vitesse/2))
    moteur34.BackwardM1(address2,vitesse)

def tourner_droite(vitesse):
    moteur34.BackwardM1(address1,vitesse) 
    moteur34.BackwardM2(address2,int(vitesse/2))
    moteur34.ForwardM2(address1,vitesse)
    moteur34.ForwardM1(address2,int(vitesse/2))

def stop(): 
    moteur34.ForwardM1(address1,0)
    moteur34.ForwardM2(address2,0)
    moteur34.ForwardM2(address1,0)
    moteur34.ForwardM1(address2,0)
    



    