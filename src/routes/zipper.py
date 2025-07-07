from flask import Blueprint, jsonify

zipper_bp = Blueprint('zipper', __name__)

@zipper_bp.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "This is the zipper route"})
