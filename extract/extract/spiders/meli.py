import scrapy


class MeliSpider(scrapy.Spider):
    name = "meli"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/acessorios-veiculos/som-automotivo/alto-falantes"]

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper')
        
        for product in products:
            
           prices = products.css('span.andes-money-amount__fraction::text').getall()
           cents = product.css('span.andes-money-amount__cents::text').getall()
            
           yield {
               'official_store': product.css('p.ui-search-official-store-label ::text').get(default='').replace('Por', '').strip(),
               'name': product.css('h2.ui-search-item__title::text').get(default='').strip(),
               'old_price_real': prices[0] if len(prices) > 0 else None,
               'old_price_cents': cents[0] if len(cents) > 0 else None,
               'new_price_real': prices[1] if len(prices) > 1 else None,
               'new_price_cents': cents[1] if len(cents) > 1 else None,
               'reviews_rating_number': product.css('span.ui-search-reviews__rating-number::text').get(),
               'reviews_amount': product.css('span.ui-search-reviews__amount::text').get()
           }
               
