from flask import Blueprint, jsonify

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "This is the payment route"})
