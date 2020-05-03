import os

class Config:
    '''
    General configuration parent class
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.urandom(69)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    def init_app(app):
        pass

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nairdaee:mutemuas2001@localhost/pitch'
    DEBUG = True

config_options = {
'development': DevConfig,
'production': ProdConfig,
'test':TestConfig
}
