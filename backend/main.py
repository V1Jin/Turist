from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import Dbase
import os

app = Flask(__name__)
CORS(app) 

@app.route("/")
def index():
    frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../frontend")
    return send_from_directory(frontend_dir, "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../frontend")
    return send_from_directory(frontend_dir, filename)

@app.route("/api/dataOrgs", methods=["GET"])
def get_data():
    orgs = Dbase.getOrgs()
    return orgs
    
    
@app.route("/api/getAudio", methods=["GET"])
def get_audio():
    pass




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
