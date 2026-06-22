import os

SECRET_KEY = os.getenv("APP_SECRET","YXNmc2Fmc2FmYXNmYXNmYXNmYXNmYXNmYXNmYXNmc2FmYXNmYXNmc2FmYXNmYXNmYXNmYXNmaGZaGRmaEAhIyQhQCMkIUA=")

username = os.getenv("MYSQL_USERNAME","crawler_app")
password = os.getenv("MYSQL_PASSWORD","Admin#123")
server = os.getenv("MYSQL_HOST","localhost")
database = os.getenv("MYSQL_DATABASE","crawler")
# tcp database connection URL
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{username}:{password}@{server}/{database}"

