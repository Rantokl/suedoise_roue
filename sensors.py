# sensors.py
import RPi.GPIO as GPIO
import time

SENSORS = {
    "Gauche": {"TRIG": 22, "ECHO": 27},
    "Droite": {"TRIG": 23, "ECHO": 24},
    "Arrière": {"TRIG": 5, "ECHO": 6}
}

GPIO.setmode(GPIO.BCM)
for sensor in SENSORS.values():
    GPIO.setup(sensor["TRIG"], GPIO.OUT)
    GPIO.setup(sensor["ECHO"], GPIO.IN)

def measure_distance(trig, echo):
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()
    while GPIO.input(echo) == 1:
        stop_time = time.time()

    elapsed = stop_time - start_time
    distance = (elapsed * 34300) / 2
    return round(distance, 2)

def get_all_distances():
    distances = {}
    for name, sensor in SENSORS.items():
        distances[name] = measure_distance(sensor["TRIG"], sensor["ECHO"])
    return distances

def cleanup():
    GPIO.cleanup()
