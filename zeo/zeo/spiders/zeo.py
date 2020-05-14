import scrapy
from ..items import ZeoItem


class QuotesSpider(scrapy.Spider):
    name = "zeo"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
      items = ZeoItem()

      all_div_quote = response.css('div.quote')
      
      for quotes in all_div_quote:
          title = quotes.css('span.text::text').extract()
          author = quotes.css('.author::text').extract()
          tag = quotes.css('.tag::text').extract()
          
          items['title']= title
          items['author']= author
          items['tag'] = tag
          yield items