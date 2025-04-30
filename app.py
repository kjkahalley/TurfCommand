import os
from flask import Flask, render_template, request
from threading import Timer
import webbrowser

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

def open_webpage():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        Timer(1, open_webpage).start()
    app.run(debug=True)