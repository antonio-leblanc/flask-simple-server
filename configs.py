class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '\x8a\x97\x83\xb0`Hd\xda\x1a\xce\xe5u\xfbx\x9e\xbf\xe5\xc2y7z\xdc[\xab'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    PORT = 5000