from v1.admin import admin_bp
from flask import render_template
from models import Crawler


@admin_bp.route('/crawler/list', methods=['GET'])
def list_crawlers():
    data = []
    crawlers = Crawler.query.all()
    # deserialize sqlalchemy object into dict
    for crawler in crawlers:
        data.append(crawler)
    return render_template("admin/crawler/list.html", data=data)
