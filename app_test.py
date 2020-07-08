from flask import Flask, request
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler


############################################
# ---------------- INIT ---------------- #
############################################

def create_app(config_file):
    app = Flask(__name__)
    cors = CORS(app)
    return app


# scheduler = BackgroundScheduler()
# scheduler.add_job(func=si_db_backup_job, **BACKUP_TRIGGER)
# scheduler.start()


@app.route('/')
def check_connection():
    return "FICARA BOLADAO"

     