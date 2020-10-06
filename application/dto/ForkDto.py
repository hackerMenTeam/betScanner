import datetime
from dataclasses import dataclass

from application.dto.BookmakerDto import BookmakerDto


@dataclass
class MatchDto:
    id: int
    title: str
    sport: str
    championship: str

    def __init__(self):
        pass

    # def __init__(self, match):
    #     self.id = match.id
    #     self.title = match.title
    #     self.sport = match.sport_kind
    #     self.championship = match.championship


@dataclass
class BetDto:
    id: int
    match: MatchDto
    bookmaker: BookmakerDto
    exodus: str
    odd: float

    def __init__(self):
        pass

    # def __init__(self, bet):
    #     self.id = bet.id
    #     self.match = MatchDto(bet.match)
    #     self.bookmaker = BookmakerDto(bet.bookmaker)
    #     self.exodus = bet.exodus
    #     self.odd = bet.coef


@dataclass
class ForkDto:
    id: int
    timestamp: datetime.datetime
    bets: list

    def __init__(self):
        pass

    # def __init__(self, fork):
    #     self.id = fork.id
    #     self.timestamp = fork.timestamp
    #     self.bets = list(map(lambda bet: BetDto(bet), fork.bets))

