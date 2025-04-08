from roboclaw_3 import Roboclaw
from time import sleep
from motors import *


marche_avant(32)
sleep(2)
stop()
sleep(0.5)
tourner_droite(32)
sleep(2)
stop()
sleep(0.5)
tourner_gauche(32)
sleep(2)
stop()
sleep(0.5)
marche_arriere(32)
sleep(2)
stop()

    


