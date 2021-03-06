import os
import sys

from flask import Flask, render_template

from containers import Containers
from docker_wrap import client
from images import Images


app = Flask(__name__)
app.register_blueprint(Images)
app.register_blueprint(Containers)


@app.route('/')
def index():
    return render_template('index.html', client=client)


@app.route('/tabletest')
def sb_test():
    return render_template('table_test.html')


if __name__ == '__main__':
    print("Welcome to DockerWeb\n")

    sys.stdout = open(os.devnull, 'w')
    app.run(debug=False, host='0.0.0.0')
