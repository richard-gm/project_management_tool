from flask import Blueprint, render_template
from .extensions import mongoDB

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')


@main.route('/admin')
def admin():
    return render_template('admin.html')


@main.route("/test")
def test():
    user_collection = mongoDB.db["cloudApp"]
    user_collection.insert({'name': 'Richard'})
    return '<H1>Connected to the data base!</H1>'
