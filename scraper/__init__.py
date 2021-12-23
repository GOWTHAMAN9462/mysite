from flask import Flask
from os import environ

app = Flask(__name__)

from scraper import routes
