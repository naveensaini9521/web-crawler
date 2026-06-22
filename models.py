from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from werkzeug.security import generate_password_hash
from db import db
import flask_login


class User(db.Model, flask_login.UserMixin):
    __tableName__ = 'users'
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(255), unique=True, nullable=False)
    email = db.Column(String(120),unique=True, nullable=True)
    password = db.Column(String(255), nullable=False)

    @staticmethod
    def create(data):
        user = User(username=data['username'],
                    email=data['email'],
                    password=generate_password_hash(data['password'])
                    )
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.rollback()
            raise e

class Crawler(db.Model):
    __tableName__ = 'crawlers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    url = Column(Text, nullable=False)
    start_dateTime = Column(DateTime, nullable=True)
    end_dateTime = Column(DateTime, nullable=True)
    frequency = Column(Integer, nullable=True)
    recursive = Column(Boolean, nullable=True)

    @staticmethod
    def create(data):
        crawler = Crawler(
            name=data['name'],
            url=data['url'],
            start_dateTime=data.get('start_dateTime'),
            end_dateTime=data.get('end_dateTime'),
            frequency=data.get('frequency'),
            recursive=data.get('recursive')
        )

        try:
            db.session.add(crawler)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise e



class CrawlerData(db.Model):
    __tableName__ = 'crawler_data'
    id = Column(Integer, primary_key=True)
    crawler_id = Column(Integer, nullable=False)
    data = Column(Text(12341412), nullable=False)

    @staticmethod
    def create(data):
        crawler_data = CrawlerData(
            crawler_id=data['crawler_id'],
            data=data['data'],
        )

        try:
            db.session.add(crawler_data)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

class CrawlerDataDetails(db.Model):
    __tablename__ = 'crawler_data_details'
    id = db.Column(db.Integer, primary_key=True)
    crawler_id = db.Column(db.String(50), nullable=False)
    field1 = db.Column(db.String(100))
    field2 = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=db.func.now())
    data = db.Column(db.Text)


    @staticmethod
    def create(data):
        crawler_data_details = CrawlerDataDetails(
            crawler_id=data['crawler_id'],
            field1=data.get('field1'),
            field2=data.get('field2'),
            data=data.get('data'),
        )

        try:
            db.session.add(crawler_data_details)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class CronJob(db.Model):
    __tablename__ = 'cronjobs'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.String(36), unique=True, nullable=False)
    flag = db.Column(db.Boolean, default=False, nullable=False)


    @staticmethod
    def create(data):
        cron_job = CronJob(
            job_id=data['job_id'],
            flag = data.get('flag', False)
        )
        try:
            db.session.add(cron_job)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e




