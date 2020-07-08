from app_factory import create_app
from configs import DevelopmentConfig
    
app = create_app(DevelopmentConfig())

if __name__ == '__main__':
    app.run(threaded=True) 

