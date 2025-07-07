# src/routes/zipper.py
from flask import Blueprint, jsonify

zipper_bp = Blueprint('zipper_bp', __name__)

@zipper_bp.route("/ping", methods=["GET"])
def zip_ping():
    return jsonify({"message": "Zipper route working!"})