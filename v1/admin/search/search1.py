from flask import request, jsonify, render_template
from models import CrawlerData
from v1.admin.search import admin_search_bp
from db import db

@admin_search_bp.route('/search', methods=['GET', 'POST'])
def search():
    query = db.select(CrawlerData.id, CrawlerData.title)
    crawldata = db.session.execute(query)
    context = {
        "events": crawldata
    }
    form = SearchForm()
    if form.validate_on_submit():
        search_title = request.form.get('title')
        result = CrawlerData.query.filter_by(title=search_title).all()
        return render_template("admin/search/search_page.html")
    return render_template("admin/search/search_page.html", **context, form=form)

# @admin_search_bp.route('/search', methods=['GET'])
# def search(query, index):
#     query_words = re.findall(r'\w+', query.lower())
#     results = {}
#     for word in query_words:
#         if word in index:
#             results[word] = index[word]
#
#     return render_template('admin/search/search_page.html')

# def search_engine(url, query):
#     soup = fetch_page(url)
#     if soup is None:
#         return None
#     index = index_words(soup)
#     index = remove_stop_words(index)
#     results = search(query, index)
#     return results
#
# def fetch_page(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         return soup
#     else:
#         return None
#
# def index_words(soup):
#     index = {}
#     words = re.findall(r'\w+', soup.get_text())
#     for word in words:
#         word = word.lower()
#         if word in index:
#             index[word] += 1
#         else:
#             index[word] = 1
#     return index
#
# def remove_stop_words(index):
#     stop_words = {'a', 'an', 'the', 'and', 'or', 'in', 'on', 'at'}
#     for stop_word in stop_words:
#         if stop_word in index:
#             del index[stop_word]
#     return index


@admin_search_bp.route('/search_result', methods=['GET'])
def search_result():
    response = {"message": "API response generated successfully", "data": []}
    query = request.args.get("query")
    if query:
        search = "%{}%".format(query)
        results = CrawlerData.query.filter(CrawlerData.data.like(search)).all()
        for result in results:
            response['data'].append({
                'data': result.data,
                'url': result.url if hasattr(result, 'url') else '#'  # Assuming each result has a 'url' attribute
            })
    return jsonify(response), 200

    return render_template('admin/search/search_results.html', results=results)
