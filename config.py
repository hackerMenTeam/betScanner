import os


from setup import basedir


class BaseConfig(object):
    SECRET_KEY = "SO_SECURE"
    DEBUG = True
    pg_user = "postgres"
    pg_pwd = "qwerty10253"
    pg_port = "5432"
    SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@localhost:{port}/bet_scanner".format(
        username=pg_user, password=pg_pwd, port=pg_port)
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(object):
    """Development configuration."""
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG_TB_ENABLED = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
