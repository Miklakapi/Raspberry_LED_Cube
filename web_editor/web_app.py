#!/usr/bin/env python

"""This module manages the web server."""

import os
from flask import Flask, send_from_directory, render_template, request

data = []
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data/', methods=['POST'])
def json_data():
    global data
    data = request.get_json()
    return '', 200


@app.route('/get/data/')
def get_data():
    return {'data': data}


if __name__ == '__main__':
    app.run('192.168.1.184', debug=False)
