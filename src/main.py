from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')


@main.route('/base')
def base():
    return 'base'


@main.route('/page2')
def page2():
    return 'page2'
