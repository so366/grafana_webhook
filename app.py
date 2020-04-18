# _*_ coding:utf-8 _*_
from flask import Flask, request, jsonify, current_app
from utils.bot import Bot

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def alert():
    if request.method == 'GET':
        return '404'
    elif request.method == 'POST':
        bot = Bot()
        bot.data()
        return '200'
    return '200'


if __name__ == '__main__':
    app.run()
