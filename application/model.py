from index import db


class Bookmaker(db.Model):
    __tablename__ = 'bookmakers'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    url = db.Column(db.VARCHAR, nullable=False, unique=True)
    is_enabled = db.Column(db.BOOLEAN, nullable=False, default=True)
    vpn_required = db.Column(db.BOOLEAN, nullable=False, default=False)

    def __init__(self, url, is_enabled, vpn_required):
        self.url = url
        self.is_enabled = is_enabled
        self.vpn_required = vpn_required

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Bet(db.Model):
    __tablename__ = 'bets'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    bookmaker_id = db.Column(db.Integer, db.ForeignKey("bookmakers.id"))
    match_title = db.Column(db.VARCHAR, nullable=False)
    sport_kind = db.Column(db.VARCHAR, nullable=False)
    championship = db.Column(db.VARCHAR, nullable=False)
    k1 = db.Column(db.Float, nullable=False)
    k2 = db.Column(db.Float, nullable=False)

    def __init__(self, match_title, sport_kind, championship, k1, k2):
        self.match_title = match_title
        self.sport_kind = sport_kind
        self.championship = championship
        self.k1 = k1
        self.k2 = k2

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Fork(db.Model):
    __tablename__ = 'forks'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    major_bet = db.Column(db.Integer, db.ForeignKey("bets.id"))
    minor_bet = db.Column(db.Integer, db.ForeignKey("bets.id"))
    timestamp = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, major_bet, minor_bet, timestamp):
        self.major_bet = major_bet
        self.minor_bet = minor_bet
        self.timestamp = timestamp

    def __repr__(self):
        return '<id {}>'.format(self.id)
