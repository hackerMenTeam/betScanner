import threading

from flask import render_template, jsonify
from index import app
from .dto.BookmakerDto import BookmakerDto

from .model import *
from main import scanner


@app.before_first_request
def activate_job():
    def run_job():
        scanner.open_pages()

    thread = threading.Thread(target=run_job)
    thread.start()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')


@app.route('/api/list_bookmakers', methods=['GET'])
def list_bookmakers():
    return jsonify(list(map(lambda bookmaker: BookmakerDto(bookmaker), Bookmaker.list_all())))


@app.route('/api/scan', methods=['POST'])
def perform_scanning():
    return jsonify(scanner.scan())


@app.route('/api/stop_scanner', methods=['POST'])
def stop_scanner():
    scanner.shut_down()
    return 'Ok'
