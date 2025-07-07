# src/routes/payment.py
from flask import Blueprint, jsonify

payment_bp = Blueprint('payment_bp', __name__)

@payment_bp.route("/ping", methods=["GET"])
def payment_ping():
    return jsonify({"message": "Payment route working!"})