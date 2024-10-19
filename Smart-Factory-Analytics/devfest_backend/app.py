from flask import Flask
from flask_migrate import Migrate
from models import db  # Import db from models
from routes import initialize_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Set up your database URI (example using SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids overhead

# Initialize the db with the app
db.init_app(app)

# Set up Flask-Migrate
migrate = Migrate(app, db)

# Initialize your routes
initialize_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
