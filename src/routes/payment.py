payment_bp = Blueprint('payment', __name__)

# your routes here, e.g.
@payment_bp.route('/test')
def test():
    return 'Payment route works!'