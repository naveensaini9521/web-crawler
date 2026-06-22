from flask import Blueprint

admin_crawler_data_bp = Blueprint('admin_crawler_data', __name__,
                             template_folder='templates')

from . import list
from . import view