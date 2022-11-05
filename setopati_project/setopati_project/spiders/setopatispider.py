import scrapy
import datetime
import json
import nepali_datetime
from scrapy.loader import ItemLoader

from setopati_project.items import SetopatiProjectItem

class SetopatispiderSpider(scrapy.Spider):
    name = 'setopatispider'
    from_date = datetime.datetime.now().strftime("%Y/%m/%d")
    # allowed_domains = ['https://www.setopati.com/']
    start_urls = [
        f'https://www.setopati.com/search?from={datetime.datetime.strptime(datetime.datetime.now().strftime("%Y/%m/%d"),"%Y/%m/%d")}&to={datetime.datetime.strptime(datetime.datetime.now().strftime("%Y/%m/%d"),"%Y/%m/%d")}'
    ]

    def parse(self, response):
        
        
        for data in response.css(".row.bishesh.news-cat-list.video-list.search-res-list > div.items"):
            link: str =  data.css("a::attr(href)").get()
            if link is not None:
                request =  response.follow(link, self.follow_up_parse)
                yield request 
    
    def follow_up_parse(self, response):
        item = ItemLoader(item = SetopatiProjectItem(),response=response)

        pub_date: str = response.css(".pub-date::text").get()
        date_day: int = int(pub_date.strip().split(",")[1].strip()[-2:])
        system_nepali_date: int = nepali_datetime.datetime.now().day
        if date_day == system_nepali_date:
            
            item.add_xpath('pub_date', '//*[@id="content"]/div/section/div[1]/div[2]/div[1]/div/div[2]/span')
            item.add_xpath('image', '//*[@id="featured-images"]/figure/img/@src')
            item.add_xpath('title', '//*[@id="content"]/div/section/div[1]/h1')
            item.add_xpath('content', '//*[@id="content"]/div/div/aside/div[1]/div/div[1]/p')
            return item.load_item()
           
        
