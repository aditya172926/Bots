from  flask import Flask, render_template
import main
from time import sleep

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/getnames/', methods=['POST'])
def getTheNames():
    testing.bot.get_followings()
    sleep(2)
    done = input("Are you done?")
    following = testing.bot._get_names()
    sleep(1)
    testing.bot.get_followers()
    sleep(2)
    done = input("Are you done?")
    followers = testing.bot._get_names()

    not_following_back = [user for user in following if user not in followers]
    print(not_following_back)
    return render_template('home.html', notList = not_following_back)

@app.route('/instabot/', methods=['POST'])
def testing():
    testing.bot = main.InstaBot('aditya26sg@gmail.com', 'Shivbaba26$')
    return render_template('home.html')