from flask import Flask, render_template, request, jsonify
import threading
import time
import sensors
from motors import MotorController

app = Flask(__name__)

motor= MotorController()
distances = {"Gauche": 0, "Droite": 0, "Arrière": 0}
speed = 0
def update_distances():
    global distances
    while True:
        distances = sensors.get_all_distances()
        time.sleep(1)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/distances')
def get_distances():
    return jsonify(distances)

@app.route('/send', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message', {})
    axis = message.get('axis')
    value = int(message.get('value'))
    #print(f"Message reçu depuis AJAX : {axis} {value}")
    global speed
    speed = value
    if axis=='x':
        motor.tourner_doite(value)
    if axis=='y':
        motor.tourner_gauche(value)

    return jsonify({"status": "ok", "message": message})

@app.route('/direction', method=['POST'])
def MarcheAvant():
    global speed
    data = request.get_json()
    message = data.get('message', {})
    sens = message.get('value')
    while sens == "avant":
        motor.marche_avant(speed)
    while sens == "arriere":
        motor.marche_arriere(speed)
    while sens == "gauche":
        motor.tourner_gauche(speed)
    while sens == "doite":
        motor.tourner_droite(speed)
    while sens == "stop":
        motor.stop()


         

if __name__ == '__main__':
    try:
        thread = threading.Thread(target=update_distances)
        #thread = threading.Thread(target=run_motors, args=(axis,value))
        thread.daemon = True
        thread.start()
        app.run(host='0.0.0.0', port=8089, debug=True)
    except KeyboardInterrupt:
        print("Arrêt du serveur.")
        motor.stop()
        sensors.cleanup()
