from flask import Flask
from src.routes.auth import auth_bp
from src.routes.user import user_bp
from src.routes.payment import payment_bp
from src.routes.zipper import zipper_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(payment_bp, url_prefix='/payment')
    app.register_blueprint(zipper_bp, url_prefix='/zipper')

    return app

app = create_app()
