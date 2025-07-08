from flask import Blueprint
from database import db

zipper_bp = Blueprint("zipper_bp", __name__)

@zipper_bp.route("/ping", methods=["GET"])
def zip_ping():
    return {"message": "Zipper route working!"}