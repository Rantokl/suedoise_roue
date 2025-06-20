import serial

# Remplace ttyACM0 par le port correspondant si besoin
<<<<<<< HEAD
ser = serial.Serial('/dev/ttyACM0', 115200)
=======
def joystick_to_scale(value):
    if 570 <= value <= 590:
        return 0  # Zone morte
    elif value > 590:
        return int((value - 590) * 64 / (1023 - 590))
    elif value < 570:
        return int((570 - value) * 64 / 570)

def get_direction(x, y):
    dx = joystick_to_scale(x)
    dy = joystick_to_scale(y)

    direction = "repos"

    if dx == 0 and dy == 0:
        direction = "repos"
    elif dx > 0 and dy == 0:
        direction = "droite"
    elif dx < 0 and dy == 0:
        direction = "gauche"
    elif dx == 0 and dy > 0:
        direction = "haut"
    elif dx == 0 and dy < 0:
        direction = "bas"
    elif dx > 0 and dy > 0:
        direction = "haut-droite"
    elif dx < 0 and dy > 0:
        direction = "haut-gauche"
    elif dx > 0 and dy < 0:
        direction = "bas-droite"
    elif dx < 0 and dy < 0:
        direction = "bas-gauche"

    print(f"Valeurs converties : X = {dx}, Y = {dy} -> Direction : {direction}")
    return dx, dy, direction





ser = serial.Serial('/dev/ttyACM1', 115200)
>>>>>>> bcf451e3d110fc353484232b7dabe63d6a93d30a

print("Lecture depuis le micro:bit...")
while True:

    data = ser.readline().decode('utf-8').strip()
    print("Reçu :", data)
