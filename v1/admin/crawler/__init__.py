from flask import Blueprint, request, render_template, redirect, url_for

admin_crawler_bp = Blueprint('admin_crawler', __name__,
                             template_folder='templates')

from . import list
from . import create
