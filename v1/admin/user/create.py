from v1.admin import admin_bp
from flask import request, url_for, render_template, redirect, flash
from models import User
from flask_login import login_required


@admin_bp.route('/user/create', methods=['POST','GET'])
@login_required
def user_create():
    if request.method=="GET":
      return render_template("admin/user/create.html")

    if request.method == "POST":
        print(request.form.get('username'))
        form_data = request.form
        required_fields = ['username', 'email', 'password']

        for field in required_fields:
            if not form_data.get(field):
                flash(f"Please enter a valid {field.replace('_',' ')}")
                return redirect(url_for("admin_user_bp.user_create"))

    data ={
        'username': request.form['username'],
        'email': request.form['email'],
        'password': request.form['password']
    }

    User.create(data)
    return redirect(url_for("admin.user_list"))


    return redirect(url_for("admin_user_bp.user_create"))

# @admin_bp.route('/user/create', methods=['POST', 'GET'])
# @login_required
# def user_create():
#     if request.method == 'GET':
#         return render_template("admin/user/create.html")
#
#     # if request.method == 'POST':
#     # For POST requests
#     username = request.form.get('username')
#     email = request.form.get('email')
#
#     if not username or not email:
#         flash('Username and Email are required', 'error')
#         return redirect(url_for('admin.user_create'))
#
#     data = {'username': username, 'email': email}
#     User.create(data)
#     return redirect(url_for('admin.user_list'))
