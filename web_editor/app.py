import os
from flask import Flask, send_from_directory, render_template, request

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data/')
def json_data():
    data = request.get_json()
    print(data)
    return True


if __name__ == '__main__':
    app.run(debug=True)
