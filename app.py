from flask import Flask, render_template, request
from time import strftime

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    time_str = strftime("%m/%d/%Y %H:%M")
    print(time_str)
    return render_template("index.html", time_info=time_str)

@app.route("/get_results", methods=["POST"])
def get_results():
    data = request.form
    print(data)
    user_number = int(data["number"])
    user_number_doubled = user_number * 2
    return render_template("results.html", output_num=user_number_doubled)
