from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = 'http://localhost:8000/'

@app.route('/')
def index():
    roles = requests.get(f'{API_URL}/roles/')
    roles = roles.json()
    print(roles)

    return render_template('index.html', roles=roles)
