# src/routes/user.py
from flask import Blueprint, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/ping", methods=["GET"])
def user_ping():
    return jsonify({"message": "User route working!"})