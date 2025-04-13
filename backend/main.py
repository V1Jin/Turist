from flask import Flask, jsonify, request
from flask_cors import CORS
import Dbase

app = Flask(__name__)
CORS(app) 

@app.route("/api/dataOrgs", methods=["GET"])
def get_data():
    orgs = Dbase.getOrgs()
    return orgs
    
    
@app.route("/api/getAudio", methods=["GET"])
def get_audio():
    pass




if __name__ == '__main__':
    app.run(debug=True)
