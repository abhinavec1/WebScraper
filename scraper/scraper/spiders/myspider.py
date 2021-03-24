import scrapy
from scrapy import Request
from ..items import NecklaceSet

class NecklaceSpider(scrapy.Spider):
 
    name = "necklacespider"
    start_urls = [
        "https://www.houseofindya.com/zyra/necklace-sets/cat"
    ]

    custom_settings = {
                'DOWNLOAD_DELAY' : 0,
                'CONCURRENT_REQUESTS_PER_DOMAIN': 1
            }

    def parse_url_list(self, response):
            item = NecklaceSet()
            name = response.css("h1::text").extract()
            price = response.css(".prodRight span:nth-child(3)::text")[0].extract()
            description = response.css("#tab-1 p::text").extract()
            image_url = response.css(".lazySlider").xpath("@data-original").extract()

            item['name'] = name
            item['price'] = price
            item['description'] = description
            item['image_urls'] = image_url

            yield item

    def parse(self, response):
        urls = response.css('div.catgList a').xpath("@href").extract()
        for url in urls:
            next_page = 'https://www.houseofindya.com' + url
            yield Request(next_page, callback=self.parse_url_list)

        
