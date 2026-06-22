# import scrapy
# from scrapy.crawler import CrawlerProcess
#
#
# class DynamicURLSpider(scrapy.Spider):
#     name = 'dynamic_url_spider'
#
#     def __init(self, start_url=None, *args, **kwargs):
#         super(DynamicURLSpider, self).__init__(*args, **kwargs)
#         self.start_urls = [start_url] if start_url else []
#
#         def parse(self, response):
#             title = response.css('title::text').get()
#             print(f"title:{title}")
#
# def run_spider(start_url):
#     process = CrawlerProcess(settings={
#         'USER_AGENT': 'Mozilla/5.0',
#         'ROBOTSTXT_OBEY': True
#     })
#
#     process.crawl(DynamicURLSpider, start_url= start_url)
#     process.start()
