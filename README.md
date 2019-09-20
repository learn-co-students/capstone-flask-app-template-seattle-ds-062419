# Capstone Flask App Template

## Part 1: Students Will Be Able To
 - [] Describe the client-server model
 - [] Describe the terms "frontend" and "backend"
 - [] Understand the difference between a static and a dynamic website
 - [] Understand which part of a Flask app contains Python
 - [] Understand which part of a Flask app contains HTML and CSS
 - [] Create a new `conda` environment and install the requirements for a Flask app
 - [] Run a Flask app locally
 - [] View output from server print statements
 - [] Use the `jinja2` templating system to send data from the backend to the frontend of a Flask app

## Part 2: Students Will Be Able To
 - [] Understand the difference between a `GET` and a `POST` request
 - [] Use an HTML form to send data from the frontend to the backend
 - [] Understand how JavaScript fits into the frontend

## Requirements

This repo uses Python 3.6.0. All python packages can be found in the `requirements.txt` file.

To create a new `conda` environment to use this repo, run:
```bash
conda create --name flask-env --file requirements.txt
conda activate flask-env
```

You will likely need to install additional packages to support your deployment, e.g. `scikit-learn`.  With the `flask-env` activated, you can run `conda install <package-name>`.  Once you are ready to deploy, you can generate your own `requirements.txt` for reproducibility purposes with:
```bash
conda list --export requirements.txt
```
## Running the Flask Application

```bash
export FLASK_ENV=development
env FLASK_APP=app.py flask run
```

## Sending Data From the Backend to the Frontend

Let's get the current time:
```python
from time import strftime
time_str = strftime("%m/%d/%Y %H:%M")
```

Then let's send it to the frontend:
```python
return render_template("index.html", time_info=time_str)
```

Then on the frontend, display it:
```html
<p>
    Current time: {{time_info}}
</p>
```
