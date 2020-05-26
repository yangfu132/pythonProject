#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, json
from flask.templating import render_template

app = Flask(__name__);

@app.route('/') 
def index():
    return render_template('index.html', result={});

@app.route('/iframe/<file>') 
def iframe(file):
    return render_template(file, result={'msg':'Hello World!'});

if __name__ == "__main__":
    app.config.from_pyfile('ServerConfig.py', silent=True);
    app.run(host='0.0.0.0');