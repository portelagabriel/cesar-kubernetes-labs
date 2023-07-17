from flask import Flask, render_template
import os

app = Flask(__name__)
title = os.getenv('title')
info = os.getenv('info')

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/infos")
def infos():
    obj = {
        "info": info,
        "title": title
    }

    return obj

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000)
