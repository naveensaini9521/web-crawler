import requests
from bs4 import BeautifulSoup
from flask import request, render_template
from tasks import crawler
from v1.admin.search.search import search


def crawl(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def extract_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        links.append(a_tag['href'])
    return links

def index():
    if request.method == 'POST':
        url = request.form['url']
        soup = crawler(url)

        if isinstance(soup, str):
            return render_template('admin/search/search_page.html', error=soup)
        links = extract_links(soup)
        return render_template(search)