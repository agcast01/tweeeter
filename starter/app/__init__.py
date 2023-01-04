from flask import Flask, render_template
from .config import Config
from .tweets import tweets
from random import choice
from .forms.form import CreateTweetForm

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def home():
    tweet = choice(tweets)
    return render_template('index.html', tweet=tweet)


@app.route('/feed')
def feed():
    return render_template('feed.html', tweets=tweets)


@app.route('/new', methods=['GET', 'POST'])
def newTweet():
    form = CreateTweetForm()
    return render_template('new_tweet.html', form=form)
