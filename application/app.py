import datetime
import threading

from flask import render_template, jsonify
from index import app
from .dto.BookmakerDto import BookmakerDto
from .dto.ForkDto import MatchDto, BetDto, ForkDto

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
    return render_template('/dist/index.html')


@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('/dist/index.html')


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


@app.route('/api/list_forks', methods=['GET'])
def list_forks():
    match = MatchDto()
    match.id = 1
    match.title = 'Manchester United - Arsenal'
    match.championship = "English Premier League"
    match.sport = "Football"
    marathoneBet = BookmakerDto()
    marathoneBet.id = 1
    marathoneBet.name = "Marathonebet"
    marathoneBet.url = ""
    _1xbet = BookmakerDto()
    _1xbet.id = 2
    _1xbet.name = "1xBet"
    _1xbet.url = ""
    bet1 = BetDto()
    bet1.match = match
    bet1.id = 1
    bet1.exodus = "1 W"
    bet1.bookmaker = marathoneBet
    bet1.odd = 1.12
    bet2 = BetDto()
    bet2.match = match
    bet2.id = 1
    bet2.exodus = "2 W"
    bet2.bookmaker = _1xbet
    bet2.odd = 3.2
    bet3 = BetDto()
    bet3.match = match
    bet3.id = 1
    bet3.exodus = "Draw"
    bet3.bookmaker = marathoneBet
    bet3.odd = 1.9
    fork1 = ForkDto()
    fork1.id = 1
    fork1.bets = [bet1, bet2, bet3]
    fork1.timestamp = datetime.datetime.now()
    forks = [fork1]
    return jsonify(forks)
