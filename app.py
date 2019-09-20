from flask import Flask, render_template
from time import strftime

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    time_str = strftime("%m/%d/%Y %H:%M")
    print(time_str)
    return render_template("index.html", time_info=time_str)

