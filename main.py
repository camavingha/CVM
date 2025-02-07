from flask import Flask, jsonify, send_from_directory
import random
import time
import threading
import os

app = Flask(__name__)

data = {"current": 0, "voltage": 0, "power": 0}

def generate_random_values():
    while True:
        data["current"] = round(random.uniform(0, 10), 2)  # Random current (0-10A)
        data["voltage"] = round(random.uniform(200, 240), 2)  # Random voltage (200-240V)
        data["power"] = round(data["current"] * data["voltage"], 2)  # Calculate power (W)
        time.sleep(1)

    
@app.route('/')
def serve_index():
    return send_from_directory(app.root_path, 'index.html')

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    threading.Thread(target=generate_random_values, daemon=True).start()
    app.run(debug=True, host='0.0.0.0', port=5555)
