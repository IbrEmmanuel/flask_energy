from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime, timedelta
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='../frontend')
CORS(app)

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client['energy_monitor']
collection = db['readings']

# Track ESP32 connection status
last_esp32_update = None
CONNECTION_TIMEOUT = timedelta(seconds=10)  # Consider ESP32 disconnected after 10 seconds of no data

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/energy', methods=['POST'])
def receive_energy_data():
    try:
        data = request.json
        data['timestamp'] = datetime.utcnow()
        collection.insert_one(data)
        global last_esp32_update
        last_esp32_update = datetime.utcnow()
        return jsonify({"status": "success", "message": "Data received"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/energy', methods=['GET'])
def get_energy_data():
    try:
        limit = int(request.args.get('limit', 100))
        readings = list(collection.find({}, {'_id': 0}).sort('timestamp', -1).limit(limit))
        
        # Check ESP32 connection status
        is_connected = False
        if last_esp32_update and (datetime.utcnow() - last_esp32_update) < CONNECTION_TIMEOUT:
            is_connected = True
        
        if not readings:
            return jsonify({
                "status": "waiting",
                "message": "Waiting for ESP32 connection",
                "is_connected": is_connected,
                "data": None
            }), 200
            
        return jsonify({
            "status": "success",
            "is_connected": is_connected,
            "data": readings[0] if readings else None
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
