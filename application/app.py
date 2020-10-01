from flask import render_template, jsonify
from index import app
from .dto.BookmakerDto import BookmakerDto

from .model import *


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')


@app.route('/api/list_bookmakers', methods=['GET'])
def list_bookmakers():
    return jsonify(list(map(lambda bookmaker: BookmakerDto(bookmaker), Bookmaker.list_all())))
