import scrapy

from ..items import ScrapZemenItem

class ZemenScrapSpider(scrapy.Spider):
    name = 'zamen'
    page_no =2
    
    start_urls = ['https://www.zameen.com/Homes/Islamabad_Bahria_Town_Bahria_Enclave-1705-1.html']

    def parse(self, response):
        items = ScrapZemenItem()

        location=response.css('div._162e6469').css('::text').extract()
        price=response.css('.f343d9ce').css('::text').extract()
        image=response.css('img._8f499ba9::attr(src)').extract()

        items['location']=location
        items['price']=price
        items['image']=image

        yield items

        next_page ='https://www.zameen.com/Homes/Islamabad_Bahria_Town_Bahria_Enclave-1705-'+str(ZemenScrapSpider.page_no)+'.html'
       

        if ZemenScrapSpider.page_no <=2:
            ZemenScrapSpider.page_no+=1
            yield response.follow(next_page, callback=self.parse)