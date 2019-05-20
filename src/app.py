import requests
import os
import re
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import load_commands
from command_interface import commands_list


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
        for command in commands_list:
            for key in command.keys:
                if re.match(key, r['message']['text']):
                    send_message(r['message']['chat']['id'], command.handle(r))
                    return jsonify(r)
        send_message(r['message']['chat']['id'], 'command not found')
        return jsonify(r)
    return index()


def send_message(chat_id, text):
    url = URL + 'sendMessage'
    data = {"chat_id" : chat_id, "text" : text}
    requests.post(url, json=data)


if __name__ == '__main__':
    app.run(debug=True)
