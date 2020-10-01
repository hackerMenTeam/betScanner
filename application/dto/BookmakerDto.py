from dataclasses import dataclass


@dataclass
class BookmakerDto:

    id: int
    name: str
    url: str
    is_enabled: bool
    vpn_required: bool

    def __init__(self, bookmaker):
        self.id = bookmaker.id
        self.name = bookmaker.name
        self.url = bookmaker.url
        self.is_enabled = bookmaker.is_enabled
        self.vpn_required = bookmaker.vpn_required
