from flask import Blueprint

admin_user_bp = Blueprint('admin_user', __name__,
                  template_folder='templates')
from . import list
from . import create