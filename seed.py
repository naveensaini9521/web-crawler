from app import app
from db import db
from models import User
from extension import bcrypt


def create_superuser():
    username = "admin"
    password = "admin@123"
    email = "admin@gmail.com"
    with app.app_context():
        db.create_all()
        user = User.query.filter_by(username=username).first()
        if not user:
            password = bcrypt.generate_password_hash(password)
            user = User(username=username, password=password, email=email)
            db.session.add(user)
            db.session.commit()


if __name__ == '__main__':
    create_superuser()