from flask import Flask, render_template, request, jsonify
import threading
import time
import sensors

app = Flask(__name__)


distances = {"Gauche": 0, "Droite": 0, "Arrière": 0}

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
    message = data.get('message')
    print(f"Message reçu depuis AJAX : {message}")
    return jsonify({"status": "ok", "message": message})

if __name__ == '__main__':
    try:
        thread = threading.Thread(target=update_distances)
        thread.daemon = True
        thread.start()
        app.run(host='0.0.0.0', port=8089, debug=True)
    except KeyboardInterrupt:
        print("Arrêt du serveur.")
        sensors.cleanup()
