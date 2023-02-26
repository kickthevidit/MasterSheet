from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "The server works"

from app import routes, models

