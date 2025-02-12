# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLichuangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    scr = scrapy.Field()                # 网站链接
    brand_name = scrapy.Field()         # 品牌名称
    marque = scrapy.Field()             # 商品型号
    item_code = scrapy.Field()          # 商品编号
    encapsulation = scrapy.Field()      # 商品封装
    packaging_method = scrapy.Field()   # 包装方式
    gross_weight = scrapy.Field()       # 商品毛重
