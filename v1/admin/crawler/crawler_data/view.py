import io
from v1.admin.crawler.crawler_data import admin_crawler_data_bp
from flask import render_template, flash, redirect, url_for
from models import CrawlerData
from nltk.corpus import stopwords
from collections import Counter
import json
import base64
from wordcloud import WordCloud

from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')


@admin_crawler_data_bp.route('/crawler/<crawler_id>/data/<crawler_data_id>/view', methods=['GET'])
def crawler_data_view(crawler_id, crawler_data_id):
    #page = request.args.get(get_page_parameter(), type=int, default=1)
    try:
        crawler_data_detail = CrawlerData.query.filter_by(crawler_id=crawler_id, id=crawler_data_id).first()

        # convert json to text
        description = []
        json_data = json.loads(crawler_data_detail.data)
        for data in json_data:
            description.append(data['description'])

        words = word_tokenize(' '.join(filter(None, description)))

        stop_words = set(stopwords.words('english'))

        words = [word for word in words if word not in stop_words and len(word) > 3]

        words_freq = Counter(words)
        words_json = [{'text': word, 'weight': count} for word, count in words_freq.items()]

        words_json = json.dumps(words_json)

        return render_template("admin/crawler/crawler-data/view.html", data=crawler_data_detail, words_json=words_json)

    except Exception as e:
       raise e
       return render_template("admin/crawler/crawler-data/view.html", data=None, wordcloud_data=[])


@admin_crawler_data_bp.route('/crawler/wordcloud/<int:data_id>')
def view_wordcloud(data_id):
    data = CrawlerData.query.get(data_id)
    if not data:
        flash("Crawled data not found", "danger")
        return redirect(url_for('admin.crawler.crawl_instantly'))

    # Generate word cloud image in-memory
    wc = WordCloud(width=800, height=400, background_color='white').generate(data.data)
    img_io = io.BytesIO()
    wc.to_image().save(img_io, 'PNG')
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.read()).decode()

    return render_template("admin/crawler_data/view.html", image_base64=img_base64, data=data)