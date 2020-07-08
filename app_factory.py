from flask import Flask, request
from flask_cors import CORS


from routes.main import main
############################################
# ---------------- INIT ---------------- #
############################################

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)


    app.register_blueprint(main)

    cors = CORS(app)
    return app


     
