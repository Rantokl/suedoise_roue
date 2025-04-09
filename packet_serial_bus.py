from roboclaw_3 import Roboclaw
from time import sleep
from motors import *


marche_avant(64)
##marche_avant(64)
stop()
sleep(0.5)
tourner_droite(64)
#tourner_droite(64)
stop()
sleep(0.5)
tourner_gauche(64)
#tourner_gauche(64)
stop()
sleep(0.5)
marche_arriere(64)
#marche_arriere(64)
sleep(2)
stop()

    


