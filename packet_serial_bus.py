from roboclaw_3 import Roboclaw
from time import sleep

from motors import MotorController

motor = MotorController()

motor.marche_avant(32)
sleep(2)
motor.tourner_droite(32)
sleep(2)
motor.tourner_gauche(32)
sleep(2)
motor.marche_arriere(32)
sleep(2)
motor.stop()
sleep(2)
    


