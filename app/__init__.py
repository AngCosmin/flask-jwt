from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Super_Secret_JWT_KEY'

jwt = JWTManager(app)

from app import routes