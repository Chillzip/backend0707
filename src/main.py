from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set secret key from environment variable
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret-key")

# Import Blueprints
from src.routes.auth import auth_bp
from src.routes.payment import payment_bp
from src.routes.user import user_bp
from src.routes.zipper import zipper_bp

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(payment_bp, url_prefix="/payment")
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(zipper_bp, url_prefix="/zip")

# Root route for health check or landing
@app.route('/')
def index():
    return "✅ ChillZip backend is running."

# Run the app locally (Render will ignore this block)
if __name__ == '__main__':
    app.run(debug=True)