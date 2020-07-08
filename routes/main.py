from flask import Blueprint, current_app, request, render_template

main = Blueprint('main', __name__)


@main.route('/')
def check_connection():
    return render_template('landing_page.html')
