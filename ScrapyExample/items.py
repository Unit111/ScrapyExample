# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Compose, TakeFirst


def str_to_int(x):
    try:
        return int(float(x))
    except:
        return x


class StripText:
    def __init__(self, chars=' \r\t\n'):
        self.chars = chars

    def __call__(self, value):  # This makes an instance callable!
        try:
            return value.strip(self.chars)
        except:
            return value


class ProductItem(scrapy.Item):
    app_name = scrapy.Field()
    specs = scrapy.Field(
        output_processor=MapCompose(StripText())
    )
    n_reviews = scrapy.Field(
        output_processor=Compose(
            MapCompose(
                StripText(),
                lambda x: x.replace(',', ''),
                str_to_int),
            max
        )
    )


class ProductItemLoader(ItemLoader):
    default_output_processor = TakeFirst()