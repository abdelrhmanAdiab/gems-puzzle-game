# build f5fe1338e2
# (auto) 433284
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
