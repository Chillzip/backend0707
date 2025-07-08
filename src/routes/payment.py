from flask import Blueprint
from database import db

payment_bp = Blueprint("payment_bp", __name__)

@payment_bp.route("/ping", methods=["GET"])
def payment_ping():
    return {"message": "Payment route working!"}