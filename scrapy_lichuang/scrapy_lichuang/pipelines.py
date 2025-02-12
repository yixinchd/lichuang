# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class ScrapyLichuangPipeline:
    def open_spider(self, spider):
        self.fp = open('thing.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 将item转换为字典，然后转换为JSON字符串，并替换单引号为双引号
        json_str = json.dumps(dict(item))
        json_str_fixed = json_str.replace("'", '"')

        # 保存到文件或数据库等
        with open('thing.json', 'a+', encoding='utf-8') as f:  # 使用'a'模式以追加方式写入，如果是新文件则用'w'模式
            # f.write(json_str_fixed + '\n')  # 每条记录后添加换行符
            f.seek(0)
            try:
                existing_data = json.load(f)
            except(json.JSONDecodeError, ValueError):
                existing_data = []
            finally:
                existing_data.append(eval(json_str_fixed))
                f.seek(0)
                f.truncate(0)
                json.dump(existing_data, f, ensure_ascii=False, indent=4)
        # self.fp.write(str(item)+',')
        return item

    def close_spider(self, spider):
        self.fp.close()
