import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "meli"
    start_urls = ["https://lista.mercadolivre.com.br/acessorios-veiculos/som-automotivo/_Loja_all_NoIndex_True?original_category_landing=true#applied_filter_id%3Dofficial_store%26applied_filter_name%3DLojas+oficiais%26applied_filter_order%3D9%26applied_value_id%3Dall%26applied_value_name%3DSomente+lojas+oficiais%26applied_value_order%3D1%26applied_value_results%3D320372%26is_custom%3Dfalse"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper') 

        
        for product in products:

            prices = product.css('span.andes-money-amount__fraction::text').getall()
            cents = product.css('span.andes-money-amount__cents::text').getall()

            yield {
                'official_store': product.css('p.ui-search-official-store-label ::text').get(default='').replace('Por', '').strip(),
                'name': product.css('h2.ui-search-item__title::text').get(default='').strip(),
                'old_price_reais': prices[0] if len(prices) > 0 else None,
                'old_price_centavos': cents[0] if len(cents) > 0 else None,
                'new_price_reais': prices[1] if len(prices) > 1 else None,
                'new_price_centavos': cents[1] if len(cents) > 1 else None,
                'reviews_rating_number': product.css('span.ui-search-reviews__rating-number::text').get(),
                'reviews_amount': product.css('span.ui-search-reviews__amount::text').get()
            }

        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)