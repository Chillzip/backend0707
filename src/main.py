# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "ChillZip backend is live!"

@app.route("/test")
def test():
    return jsonify({"message": "Test route working!"})