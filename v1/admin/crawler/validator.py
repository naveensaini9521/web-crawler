from wtforms import StringField, validators
from wtforms.form import BaseForm

PASSWORD_LENGTH_MIN = 12
PASSWORD_LENGHT_MAX = 30


class CrawlerFormValidator(BaseForm):
    name = StringField('name', [
        validators.DataRequired(),
        validators.InputRequired(message='Crawler name is required'),
    ])
