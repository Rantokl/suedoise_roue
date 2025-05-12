import serial

# Remplace ttyACM0 par le port correspondant si besoin
ser = serial.Serial('/dev/ttyACM1', 115200)

print("Lecture depuis le micro:bit...")
while True:
    if ser.in_waiting:
        data = ser.readline().decode('utf-8').strip()
        print("Reçu :", data)