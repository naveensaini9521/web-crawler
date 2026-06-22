from flask import Blueprint

admin_search_bp = Blueprint('admin_search', __name__,
                  template_folder='templates')

from . import search
