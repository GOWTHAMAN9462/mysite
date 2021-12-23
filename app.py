from flask import Flask

from dotenv import load_dotenv
load_dotenv('.env')

from os import environ

app = Flask(__name__)

from scraper import routes

if __name__ == '__main__':
    app.run()
