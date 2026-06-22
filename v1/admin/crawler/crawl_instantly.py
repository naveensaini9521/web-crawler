from datetime import datetime
from v1.admin.crawler import admin_crawler_bp
from flask import url_for, render_template, redirect, request, flash
from models import Crawler, CrawlerData, db  # Import your SQLAlchemy models and db instance
from wordcloud import WordCloud
import os
@admin_crawler_bp.route('/crawler/crawl_instantly', methods=['GET', 'POST'])
def crawl_instantly():
    if request.method == "GET":
        return render_template("admin/crawler/instant_crawl.html")

    if request.method == "POST":
        crawler_id = request.form.get('crawler_id')

        if not crawler_id:
            flash("Please enter a valid Crawler ID", "error")
            return redirect(url_for("admin.crawl_instantly"))

        try:
            crawler_id = int(crawler_id)
            crawler = Crawler.query.get(crawler_id)

            if not crawler:
                flash("Crawler not found", "error")
                # return redirect(url_for("admin.crawl_instantly"))
                return redirect(url_for("admin_crawler_data.crawl_instantly"))

            # Simulate crawling data instantly
            # Replace this with actual crawling logic
            crawled_data = f"Data crawled at {datetime.now()}"

            # Save crawled data to database
            crawler_data = CrawlerData(
                crawler_id=crawler_id,
                data=crawled_data,
                timestamp=datetime.now()
            )
            db.session.add(crawler_data)
            db.session.commit()

            flash("Data crawled successfully", "success")
            # return redirect(url_for("admin.crawl_instantly"))
            return redirect(url_for("admin_crawler_data.crawl_result", data_id=crawler_data.id))

        except ValueError:
            flash("Invalid Crawler ID format", "error")
            return redirect(url_for("admin.crawl_instantly"))

        except Exception as e:
            flash(f"Failed to crawl data: {str(e)}", "error")
            db.session.rollback()
            return redirect(url_for("admin.crawl_instantly"))
def generate_wordcloud(text, data_id):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    output_path = f'static/wordclouds/wordcloud_{data_id}.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    wordcloud.to_file(output_path)
    return output_path
