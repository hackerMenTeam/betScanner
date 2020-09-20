from index import db, bcrypt
from sqlalchemy.dialects.postgresql import BOOLEAN


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, email, password):
        self.email = email
        self.active = True
        self.password = User.hashed_password(password)

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None


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
