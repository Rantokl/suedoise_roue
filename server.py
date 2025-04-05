from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message')
    print(f"Message reçu depuis AJAX : {message}")
    return jsonify({"status": "ok", "message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
