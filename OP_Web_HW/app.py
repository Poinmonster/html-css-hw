import pandas as pd
from flask import Flask, render_template
import tablib
import os

app = Flask (__name__)
cities = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'cities.csv')) as f:
    cities.csv = f.read()
 
@app.route("/")
def index():
    data = cities.html
    #return dataset.html
    return render_template('data.html', data=data)
 
if __name__ == "__main__":
    app.run()