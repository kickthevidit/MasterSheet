import os
import openai
from flask import Flask

app = Flask(__name__)

from app import routes

