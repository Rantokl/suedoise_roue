from roboclaw_3 import Roboclaw
from time import sleep

class MotorController:
    def __init__(self):
        self.moteur12 = Roboclaw("/dev/ttyACM0", 38400)
        self.moteur34 = Roboclaw("/dev/ttyS0", 38400)
        self.address = 0x80
        self.moteur12.Open()
        self.moteur34.Open()

    def marche_avant(self,vitesse):
        self.moteur12.ForwardM1(self.address,vitesse)
        self.moteur34.ForwardM1(self.address,vitesse)

        self.moteur12.ForwardM2(self.address,vitesse)
        self.moteur34.ForwardM2(self.address,vitesse)
  

    def marche_arriere(self,vitesse):
        self.moteur12.BackwardM1(self.address,vitesse)
        self.moteur34.BackwardM1(self.address,vitesse)

        self.moteur12.BackwardM2(self.address,vitesse)
        self.moteur34.BackwardM2(self.address,vitesse)


    def tourner_gauche(self,vitesse):
        self.moteur12.BackwardM2(self.address,vitesse)
        self.moteur34.BackwardM1(self.address,vitesse)

    def tourner_droite(self,vitesse):
        self.moteur12.BackwardM1(self.address,vitesse)
        self.moteur34.BackwardM2(self.address,vitesse)

    def stop(self):
        self.moteur12.ForwardM1(self.address,0)
        self.moteur34.ForwardM1(self.address,0)

        self.moteur12.ForwardM2(self.address,0)
        self.moteur34.ForwardM2(self.address,0)

        
    