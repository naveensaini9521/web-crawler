from v1.admin.search import admin_search_bp
from flask import  request, jsonify, render_template
from models import CrawlerData


@admin_search_bp.route('/search', methods=['GET'])
def search():
    return render_template('admin/search/search_page.html')

@admin_search_bp.route('/search_result', methods=['GET'])
def search_result():
    response = {"message": "api response generated successfully", "data": []}
    query = request.args.get("query")
    if query and query is not None:
        search = "%{}%".format(query)
        results = CrawlerData.query.filter(CrawlerData.data.like(search)).all()
        for result in results:
            response['data'].append({
                'data': result.data,
                'url': result.url if hasattr(result, 'url') else '#'
            })

    return jsonify(response, 200)
    return render_template('admin/search/search_results.html', results=results)

# def index():
#     qs = request.args.get('qs', '')
#     query = Event.query
#     if qs:
#         query = query.filter(User.name.ilike(f'%{qs}%'))
#     events = query.all()
#     return render_template('admin/search/search_results.html', **locals())
# def event_list:
#     query = db.select(Event.id, Event.title)
#     events = db.session.execute(query)
#     context = {
#         "events": events
#     }
#     if form.validate_on_submit():
#         search_title = request.form.get('title')
#
#         result = CrawlerData.query.filter(User.name.like(search)).all()
#         return render_template('admin/search_page.html')
#
#     #session.query(User).filter(User.name.like('% e %'))
#
#
#
#
#     bar_tags = "crawler"
#
#     query_sql = """SELECT * FROM table WHERE tags LIKE '%':bar_tags '%' """
#     tags_list = db.execute(text(query_sql), {"bar_tags": bar_tags}).fetchall()
#
#     return render_template('admin/search/search_results.html', results=results)
