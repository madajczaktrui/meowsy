from app import app
from flask import render_template

import urllib.request, json
import os

@app.route('/')
def home():
    #host = os.environ.get('API_HOST', 'kittini')
    #port = os.environ.get('API_PORT', '5001')
    #with urllib.request.urlopen(host + ':' + port) as url:
        #data = json.loads(url.read().decode())
    return render_template('index.html')#, data)
