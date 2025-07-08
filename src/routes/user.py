from flask import Blueprint
from database import db

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/ping", methods=["GET"])
def user_ping():
    return {"message": "User route working!"}