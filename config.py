import os

base_dir = os.path.abspath(os.getcwd())

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('app-secret')
    # other generic configuration
    # ..options

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir}/devdb.sqlite"
    DEBUG = True
    FLASK_ENV = 'development'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    FLASK_ENV = 'production'

config_ = {
    'default': DevConfig,
    'development': DevConfig,
    'production': ProdConfig
}
