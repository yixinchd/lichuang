import scrapy
import pandas as pd
from scrapy_lichuang.items import ScrapyLichuangItem


class XiaozeSpider(scrapy.Spider):
    name = 'xiaoze'
    allowed_domains = ['www.szlcsc.com']
    # 读取数据
    df = pd.read_excel('data.xlsx')
    # 转成Python列表
    python_list = df['addr'].tolist()
    # 拼接成字符串列表
    str_result = ', '.join(df['addr'].astype(str))
    start_urls = str_result.split(',')

    def parse(self, response):
        # print(brand_name)
        li_list = response.xpath('//*[@id="lc-item"]/main/div/div[1]/div/div[1]/div[1]/div[2]/div[3]/ul[1]')
        for li in li_list:
            brand_name = li.xpath('./li[3]/a/text()').extract_first()
            marque = li.xpath('./li[4]/span/text()').extract_first()
            item_code = li.xpath('./li[5]/span/text()').extract_first()
            encapsulation = li.xpath('./li[6]/span/text()').extract_first()
            packaging_method = li.xpath('./li[7]/p[2]/text()').extract_first()
            gross_weight = li.xpath('./li[8]/p[2]/text()').extract_first()

            # print(brand_name,marque,item_code,encapsulation,packaging_method,gross_weight)
            thing = ScrapyLichuangItem(brand_name=brand_name, marque=marque, item_code=item_code,
                                       encapsulation=encapsulation, packaging_method=packaging_method,
                                       gross_weight=gross_weight)
            yield thing
