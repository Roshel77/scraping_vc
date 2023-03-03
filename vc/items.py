import scrapy


class VcItem(scrapy.Item):
    _id = scrapy.Field()
    # user = scrapy.Field()
    subscribers = scrapy.Field()
    subscriptions = scrapy.Field()
