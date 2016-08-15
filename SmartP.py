# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:38:25 2016

@author: phucn_000
"""
import json
from engineP import compute
from flask import Flask
from crossdomain import crossdomain




app = Flask(__name__)

@app.route("/")
@crossdomain(origin="*")
def hello():
    return json.dumps(compute())

if __name__ == "__main__":
    app.run()







