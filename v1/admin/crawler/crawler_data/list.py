from v1.admin.crawler.crawler_data import admin_crawler_data_bp
from flask import render_template, request
from models import CrawlerData
from flask_paginate import get_page_parameter,Pagination


@admin_crawler_data_bp.route('/crawler/<crawler_id>/data', methods=['GET'])
def crawler_data(crawler_id):
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    data = []
    crawler_data = CrawlerData.query.filter_by(crawler_id=crawler_id).with_entities(CrawlerData.id,
                                                                                    CrawlerData.crawler_id).paginate(per_page=per_page)
    total = CrawlerData.query.filter_by(crawler_id=crawler_id).count()

    pagination = Pagination(page=page, total=CrawlerData.query.count(), record_name='crawler_data')

    # deserialize sqlalchemy object into dict
    for crawlers in crawler_data:
        data.append(crawlers)
    return render_template("admin/crawler/crawler-data/list.html", data=data,pagination=pagination)
