from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import User
from app import db
from werkzeug.security import generate_password_hash

profile = Blueprint('profile', __name__)

@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def user_profile():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.get(current_user.id)
        user.email = email
        if password:
            user.password = generate_password_hash(password, method='sha256')
        db.session.commit()
        flash('Profile updated successfully')

        return redirect(url_for('profile.user_profile'))

    return render_template('profile.html')
