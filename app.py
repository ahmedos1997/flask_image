from flask import Flask
from actions import bp as actionbp


app = Flask(__name__)

app.secret_key = 'SECRET_KEY'

app.register_blueprint(actionbp)

