import flask_login
from flask import Flask
import config
from v1.admin import admin_bp
from v1.admin.user import admin_user_bp
from v1.admin.crawler import admin_crawler_bp
from v1.admin.search import admin_search_bp
from v1.admin.crawler.crawler_data import admin_crawler_data_bp
from flask_wtf.csrf import CSRFProtect
from db import db
from models import User

# app initialise
app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["CELERY_BROKER_URL"] = "amqp://guest:guest@localhost:5672//"
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
# csrf protection
csrf = CSRFProtect(app)

# initialize the app with the extension
db.init_app(app)

#login manager setup
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'


# Index route
app.register_blueprint(admin_bp, url_prefix='/')
app.register_blueprint(admin_user_bp, url_prefix='/')
app.register_blueprint(admin_crawler_bp, url_prefix='/')
app.register_blueprint(admin_search_bp, url_prefix='/')
app.register_blueprint(admin_crawler_data_bp, url_prefix='/')



@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))




if __name__ == '__main__':
    # run application
    # qrcode_value = input('Enter QR code value: ')
    # print(utils.generate_qr_code(qrcode_value))
    # Create database tables based in the models
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5001)
