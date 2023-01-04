from flask import Flask, render_template
from .config import Config
from .tweets import tweets
from random import choice

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def home():
    tweet = choice(tweets)
    return render_template('index.html', tweet=tweet)


@app.route('/feed')
def feed():
    return render_template('feed.html', tweets=tweets)
