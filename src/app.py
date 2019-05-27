import requests
import os
import re
import datetime as dt
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from pymongo import MongoClient
import load_commands
from command_interface import Command


client = MongoClient('localhost', 27017)
db = client['bot']


TOKEN = os.getenv('TOKEN')
URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/{}'.format(TOKEN), methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        r = request.get_json()
        if 'text' in r['message']:
            command = re.match(r'/\w+', r['message']['text'])
            if command and command.group(0) in Command.commands_dict:
                send_message(r['message']['chat']['id'], Command.commands_dict[command.group(0)].handle(r))
                return jsonify(r)
        elif 'location' in r['message']:
            send_message(r['message']['chat']['id'], Command.commands_dict['/location'].handle(r))
            return jsonify(r)
        send_message(r['message']['chat']['id'], {'text': "Command isn't found"})
        return jsonify(r)
    return index()


def send_message(chat_id, data):
    url = URL + 'sendMessage'
    d = {'chat_id': chat_id}
    d.update(data)
    requests.post(url, json=data)


if __name__ == '__main__':
    app.run(debug=True)
