from sqlalchemy import or_
from sqlalchemy.orm import relationship

from index import db

forks_to_bets = db.Table('association', db.Model.metadata,
    db.Column('forks_id', db.Integer, db.ForeignKey('forks.id')),
    db.Column('bets_id', db.Integer, db.ForeignKey('bets.id'))
)

class Bookmaker(db.Model):
    __tablename__ = 'bookmakers'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    url = db.Column(db.VARCHAR, nullable=False, unique=True)
    is_enabled = db.Column(db.BOOLEAN, nullable=False, default=True)
    vpn_required = db.Column(db.BOOLEAN, nullable=False, default=False)

    def __init__(self, name, url, is_enabled, vpn_required):
        self.name = name
        self.url = url
        self.is_enabled = is_enabled
        self.vpn_required = vpn_required

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        return False

    def __lt__(self, other):
        return len(self.name) < len(other.name)

    @staticmethod
    def get_by_id(id):
        return db.session.query(Bookmaker).get(id)

    @staticmethod
    def list_all():
        return db.session.query(Bookmaker).all()

    @staticmethod
    def list_by_criteria(criteria):
        queries = []
        if criteria.is_enabled != None:
            queries.append(Bookmaker.is_enabled == criteria.is_enabled)
        if criteria.vpn_required != None:
            queries.append(Bookmaker.vpn_required == criteria.vpn_required)
        if criteria.name_fragment != None:
            queries.append(or_(Bookmaker.name.like('%{}%'.format(criteria.name_fragment)),
                               Bookmaker.url.like('%{}%'.format(criteria.name_fragment))))

        return db.session.query(Bookmaker).filter(*queries).all()

    class Criteria:

        def __init__(self):
            self.is_enabled = None
            self.vpn_required = None
            self.name_fragment = None

        @property
        def is_enabled(self):
            return self.__is_enabled

        @property
        def vpn_required(self):
            return self.__vpn_required

        @property
        def name_fragment(self):
            return self.__name_fragment

        @is_enabled.setter
        def is_enabled(self, value):
            self.__is_enabled = value

        @vpn_required.setter
        def vpn_required(self, value):
            self.__vpn_required = value

        @name_fragment.setter
        def name_fragment(self, value):
            self.__name_fragment = value


class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    title = db.Column(db.VARCHAR, nullable=False)
    sport_kind = db.Column(db.VARCHAR, nullable=False)
    championship = db.Column(db.VARCHAR, nullable=False)

    def __init__(self, title, sport_kind, championship):
        self.title = title
        self.sport_kind = sport_kind
        self.championship = championship

    def __repr__(self):
        return '<title {}'.format(self.title)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.title == other.title
        return False

    def __lt__(self, other):
        return self.title.__lt__(other.match_title)


class Bet(db.Model):
    __tablename__ = 'bets'
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    match_id = db.Column(db.Integer, db.ForeignKey("matches.id"))
    match = relationship("Match", foreign_keys=[match_id])
    bookmaker_id = db.Column(db.Integer, db.ForeignKey("bookmakers.id"))
    bookmaker = relationship("Bookmaker", foreign_keys=[bookmaker_id])
    exodus = db.Column(db.String(10), nullable=False)
    coef = db.Column(db.Integer, nullable=False)

    def __init__(self, match, bookmaker, exodus, coef):
        self.match = match
        self.bookmaker = bookmaker
        self.exodus = exodus
        self.coef = coef

    def __repr__(self):
        return '<match {}, bookmaker {}, coef {}>, exodus {}'.format(self.match, self.bookmaker,self.coef, self.exodus)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.match == other.match and self.bookmaker.__eq__(other.bookmaker) and self.coef == other.coef
        return False

    def __lt__(self, other):
        return self.bookmaker.__lt__(other.bookmaker)


class Fork(db.Model):
    __tablename__ = 'forks'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    bet = relationship("Bet", secondary=forks_to_bets)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, bet, timestamp):
        self.bet = bet
        self.timestamp = timestamp

    def __repr__(self):
        return '<bet {}>'.format(self.bet)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.bet.__eq__(other.bet)
        return False

    def __lt__(self, other):
        return self.bet.__lt__(other.bet)


# class ForkToBet(db.Model):
#     __tablename__ = 'forks_to_bet'
#
#     id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
#     fork_id = db.Column(db.Integer, db.ForeignKey("fork.id"))
#     fork = relationship("Match", foreign_keys=[fork_id])
#     bet_id = db.Column(db.Integer, db.ForeignKey("bet.id"))
#     bet = relationship("Match", foreign_keys=[bet_id])
#
#     def __init__(self, fork, bet):
#         self.fork = fork
#         self.bet = bet
#
#     def __repr__(self):
#         return '<fork {}, bet {}>'.format(self.fork, self.bet)
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self.bet.__eq__(other.bet)
#         return False
#
#     def __lt__(self, other):
#         return self.bet.__lt__(other.bet)



