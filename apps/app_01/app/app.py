from flask import Flask, render_template
import requests
import os

app = Flask(__name__)
url = os.getenv('url', "http://localhost:8000/infos")

@app.route("/")
def index():

    try:
        content = requests.get(url).json()
        return render_template('index.html', titulo=content["title"], info=content["info"])
    except:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)