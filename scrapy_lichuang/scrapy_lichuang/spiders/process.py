import json
import pandas as pd
if __name__ == '__main__':
    # 从json文件读取数据
    with open("thing.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 创建DataFrame
    df = pd.DataFrame(data)

    # 保存为Excel文件
    df.to_excel("output.xlsx", index=False, engine='openpyxl')
    print("Excel文件已生成：output.xlsx")
