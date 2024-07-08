import scrapy


class MeliSpider(scrapy.Spider):
    name = "meli"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/alto-falantes"]

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper')
        
        for product in products:
            
           yield {
               'official_store': product.css('p.ui-search-official-store-label ::text').get(default='').replace('Por', '').strip()
           }
               
