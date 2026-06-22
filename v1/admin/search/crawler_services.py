# from bs4 import BeautifulSoup
# import requests
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import io
# import base64
#
# def crawl(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         return soup
#     else:
#         return None
#
# def extract_text(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     paragraphs = soup.find_all('p')
#     text = ' '.join([p.get_text() for p in paragraphs])
#     return text
#
# def generate_word_cloud(text):
#     wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
#     buffer = io.BytesIO()
#     plt.figure(figsize=(10, 6))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     plt.savefig(buffer, fromat='png')
#     plt.show()
#     buffer.seek(0)
#     img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
#     return img_str
