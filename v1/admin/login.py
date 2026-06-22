from v1.admin import admin_bp
from flask import request,render_template
from flask import flash, redirect, url_for
from models import User
from flask_login import login_user, logout_user, login_required, current_user


@admin_bp.route('/login', methods=['GET', 'POST'])
@admin_bp.route('/')
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for("admin.dashboard"))
        return render_template("admin/pages-login.html")

    if request.method == 'POST':
        from extension import bcrypt
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if not user:
            flash("Please check your login details and try again.")
            return render_template("admin/pages-login.html", error="Invalid username or password")

        if not user or not bcrypt.check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return render_template("admin/pages-login.html", error="Invalid username or password")
        else:
            login_user(user, remember=True)
            flash('you have successfully logged in.')
            return redirect(url_for("admin.dashboard"))

@admin_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('you have successully logged out.')
    return redirect(url_for("admin.login"))

@admin_bp.route('/dashboard', methods =['GET'])
@login_required
def dashboard():
    return render_template("admin/index.html")


