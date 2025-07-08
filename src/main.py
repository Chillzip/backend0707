from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret-key")

from routes.auth import auth_bp
from routes.user import user_bp
from routes.payment import payment_bp
from routes.zipper import zipper_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(payment_bp, url_prefix="/payment")
app.register_blueprint(zipper_bp, url_prefix="/zip")

@app.route('/')
def home():
    return {"message": "✅ ChillZip backend is running."}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)