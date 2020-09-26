from flask import render_template, jsonify
from index import app, db


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')


@app.route('/api/list_bookmakers', methods=['GET'])
def list_bookmakers():
    return jsonify(['MarathoneBet', '1XBet'])
