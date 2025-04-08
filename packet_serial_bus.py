from roboclaw_3 import Roboclaw
from time import sleep
from motors import *


marche_avant(24)
stop()
sleep(0.5)
tourner_droite(24)
stop()
sleep(0.5)
tourner_gauche(24)
stop()
sleep(0.5)
marche_arriere(24)
sleep(2)
stop()

    


