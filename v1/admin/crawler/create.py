from datetime import date
from models import Crawler, CrawlerData
from v1.admin.crawler import admin_crawler_bp
from flask import request, url_for, render_template, redirect, flash
import requests

@admin_crawler_bp.route('/crawler/create', methods=['GET', 'POST'])
def crawler_create():
    if request.method == "GET":
        return render_template("admin/crawler/create.html")
    # run validator to validate user's input
    if request.method == "POST":
        print(request.form.get('name'))
        form_data = request.form
        required_fields = ['name', 'url', 'start_dateTime', 'end_dateTime', 'frequency']

        for field in required_fields:
           if not form_data.get(field):
              flash(f"Please enter a valid {field.replace('_', ' ')}", "error")
              return redirect(url_for("admin_crawler_bp.crawler_create"))

        try:
            start_date = date.fromisoformat(form_data['start_dateTime'])
            end_date = date.fromisoformat(form_data['end_dateTime'])

            # start_date = datetime.strptime(form_data['start_date'], '%Y-%m-%d %H:%M:%S')
            # end_date = datetime.strptime(form_data['end_date'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
           flash("Invalid date format. Please use YYYY-MM-DD.", "error")
           # return redirect(url_for("admin_crawler_bp.crawler_create"))
           return redirect(url_for("admin_crawler.crawler_create"))


        recursive = bool(form_data.get('recursive'))


    # data = {'name': request.form['name'],
    #         'url': request.form['url'],
    #         'start_dateTime': request.form['start_date'],
    #         'end_dateTime': request.form['end_date'],
    #         'frequency': (request.form['frequency']),
    #         'recursive': recursive,
    #         }

    data = {
        'name': form_data['name'],
        'url': form_data['url'],
        'start_dateTime': start_date,
        'end_dateTime': end_date,
        'frequency': int(form_data['frequency']),
        'recursive': recursive,
    }

    try:
        Crawler.create(data)
        # use case call celery job based on start date and end date given
        # use case call celery job based upon frequency
        # use case call celery job based on recursive True or False
        # call celery async and add item into queue

        response = requests.get(data['url'])
        if response.status_code == 200:
            crawl_data = {
                'crawler_id': Crawler.query.filter_by(name=data['name']).first().id,
                'data': response.text
            }
            CrawlerData.create(crawl_data)


        flash("Crawler created successfully.", "success")
        return redirect(url_for("admin.list_crawlers"))
    except Exception as e:
        error_message = "Failed to create crawler:" + str(e)
        flash(error_message, "error")
        # raise e

        return redirect(url_for("admin_crawler_bp.crawler_create"))

@admin_crawler_bp.route('/crawler/crawl_result/<int:data_id>', methods=['GET'])
def crawl_result(data_id):
    result = CrawlerData.query.get_or_404(data_id)
    wc_image = f'/static/wordclouds/wordcloud_{data_id}.png'
    return render_template("admin/crawler/crawl_result.html", result=result, wc_image=wc_image)
