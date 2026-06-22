from v1.admin.crawler import admin_crawler_bp
from flask import render_template
from models import Crawler


@admin_crawler_bp.route('/crawler/<crawler_id>/delete', methods=['GET'])
def crawler_delete(crawler_id):
    crawler = Crawler.query.filter_by(id,crawler_id).first()

    return render_template("admin/crawler/list.html")
