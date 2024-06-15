from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import db, Task, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)