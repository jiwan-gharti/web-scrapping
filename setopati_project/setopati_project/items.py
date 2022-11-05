# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose,TakeFirst,Join
from w3lib.html import remove_tags


class SetopatiProjectItem(scrapy.Item):
    pub_date = scrapy.Field(
        input_processor = MapCompose(remove_tags), 
        output_processor = TakeFirst()
    )
    image = scrapy.Field(
        input_processor = MapCompose(remove_tags), 
        output_processor = TakeFirst()
    )
    title = scrapy.Field(
        input_processor = MapCompose(remove_tags), 
        output_processor = TakeFirst()
    )
    content = scrapy.Field(
        input_processor = MapCompose(remove_tags), 
        output_processor = TakeFirst()
    )
