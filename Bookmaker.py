from app import db
from sqlalchemy.dialects.postgresql import BOOLEAN


class Bookmaker(db.Model):
    __tablename__ = 'bookmakers'

    id = db.Column(db.String(), primary_key=True)
    url = db.Column(db.String())
    is_enabled = db.Column(BOOLEAN)
    vpn_required = db.Column(BOOLEAN)

    def __init__(self, url, is_enabled, vpn_required):
        self.url = url
        self.is_enabled = is_enabled
        self.vpn_required = vpn_required

    def __repr__(self):
        return '<id {}>'.format(self.id)
