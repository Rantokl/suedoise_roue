import RPi.GPIO as GPIO
import time

# Configuration des broches PWM pour les moteurs
PWM_PINS = [12, 13]  # Moteurs 1 à 4 18, 19
DIR_PINS = [  # 2 broches direction par moteur
    (20, 21),  # Moteur 1
    (16, 26),  # Moteur 2
    #(19, 17),  # Moteur 3
    #(4, 25)    # Moteur 4
]

def motors_set():
      # en Hz

    # Initialisation GPIO
    GPIO.setmode(GPIO.BCM)

    # Configuration PWM et direction
    for pin in PWM_PINS:
        GPIO.setup(pin, GPIO.OUT)

    for dir1, dir2 in DIR_PINS:
        GPIO.setup(dir1, GPIO.OUT)
        GPIO.setup(dir2, GPIO.OUT)

    # Création des PWM
    pwms = [GPIO.PWM(pin, FREQUENCY) for pin in PWM_PINS]

    # Démarrer les PWM
    for pwm in pwms:
        pwm.start(0)

def set_motor(motor_index, speed, direction):
    """
    motor_index: 0 à 3
    speed: 0 à 100 (duty cycle)
    direction: 'forward' ou 'backward'
    """
    FREQUENCY = 2000
    pwms = [GPIO.PWM(pin, FREQUENCY) for pin in PWM_PINS]
    dir1, dir2 = DIR_PINS[motor_index]

    if direction == 'forward':
        GPIO.output(dir1, GPIO.HIGH)
        GPIO.output(dir2, GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(dir1, GPIO.LOW)
        GPIO.output(dir2, GPIO.HIGH)
    else:
        GPIO.output(dir1, GPIO.LOW)
        GPIO.output(dir2, GPIO.LOW)

    pwms[motor_index].ChangeDutyCycle(speed)

# try:
#     while True:
#         print("Tous les moteurs en avant")
#         for i in range(2):
#             set_motor(i, 70, 'forward')  # 70% de vitesse
#         time.sleep(5)

#         print("Tous les moteurs en arrière")
#         for i in range(2):
#             set_motor(i, 50, 'backward')  # 50% de vitesse
#         time.sleep(5)

#         print("Arrêt")
#         for i in range(2):
#             set_motor(i, 0, 'stop')
#         time.sleep(5)

# except KeyboardInterrupt:
#     print("Arrêt du programme")

# finally:
#     for pwm in pwms:
#         pwm.stop()
#     GPIO.cleanup()
