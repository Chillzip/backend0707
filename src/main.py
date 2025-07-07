# src/main.py

from flask import Flask
from src.routes.auth import auth_bp  # Import the auth blueprint

app = Flask(__name__)

# Register the auth blueprint
app.register_blueprint(auth_bp)

# Optional: Add a root route so the homepage isn't blank
@app.route("/")
def home():
    return {"message": "Welcome to ChillZip API"}

# This line is only needed for local testing — not required for Render
if __name__ == "__main__":
    app.run(debug=True)