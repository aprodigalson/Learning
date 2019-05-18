import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'


class ProductionConfig(Config):
    USERNAME = 'gyy'
    PASSWORD = '123'
    DATABASE = 'test.db'


config = {
    'development': ProductionConfig,
}
