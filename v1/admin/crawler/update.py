from v1.admin import admin_bp
from flask import render_template
from models import Crawler


@admin_bp.route('/crawler/<crawler_id>/update', methods=['GET'])
def crawler_update(crawler_id):
    crawler = Crawler.query.filter_by(id,crawler_id).first()

    return render_template("admin/crawler/list.html")
