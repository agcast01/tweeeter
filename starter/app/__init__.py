from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from random import choice
from .forms.form import CreateTweetForm
import datetime

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def home():
    tweet = choice(tweets)
    return render_template('index.html', tweet=tweet)


@app.route('/feed')
def feed():
    def sorter(tweet):
        a_list = tweet['date'].split('/')
        return datetime.date(int(a_list[2]) + 2000, int(a_list[0]), int(a_list[1]))
    sorted_by_date = sorted(tweets, key=sorter, reverse=True)
    return render_template('feed.html', tweets=sorted_by_date)


@app.route('/new', methods=['GET', 'POST'])
def newTweet():
    form = CreateTweetForm()

    if form.validate_on_submit():
        new_tweet = {
            'id': len(tweets),
            'author': form.data['author'],
            'tweet': form.data['tweet'],
            'date': datetime.date.today(),
            'likes': 0
        }
        tweets.append(new_tweet)
        return redirect('/feed')

    if form.errors:
        return form.errors

    return render_template('new_tweet.html', form=form)
