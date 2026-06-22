from v1.admin import admin_bp
from flask import request, render_template
from models import User
from flask_login import login_required


@admin_bp.route('/user/list', methods=['GET'])
@login_required
def user_list():
    if request.method == 'GET':
        # get data from model
        data = []
        users = User.query.all()
        # deserialize sqlalchemy object into dict
        for user in users:
            data.append(user)

        # set data into view
        return render_template("admin/user/list.html", data=data)
