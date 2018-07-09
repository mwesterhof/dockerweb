from flask import Flask, render_template

from .containers import Containers
from .images import Images


app = Flask(__name__)
app.register_blueprint(Images)
app.register_blueprint(Containers)


@app.route('/')
def index():
    return render_template('index.html')
