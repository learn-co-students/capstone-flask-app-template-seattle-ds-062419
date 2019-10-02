from flask import Flask, render_template, request
from time import strftime
import time
from waitress import serve

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    time_str = strftime("%m/%d/%Y %H:%M")
    print(time_str)
    restaurants = ["Din Tai Fung", "Rocco's", "Chipotle"]
    return render_template("index.html", time_info=time_str, restaurants=restaurants)

@app.route("/get_results", methods=["POST"])
def get_results():
    data = request.form
    print(data)
    # user_number = int(data["number"])
    # user_number_doubled = user_number * 2

    user_id = data["user"]
    answer = should_make_transaction(user_id)
    return render_template("results.html", answer=answer, user_id=user_id)

def should_make_transaction(user_id):
    return False

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
