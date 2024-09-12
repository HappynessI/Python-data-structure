import pandas as pd

dict={}
data=pd.read_excel(r"C:\Users\26250\Desktop\词云图实战\词云图示例.xlsx")
data.fillna("",inplace=True)

list=[]
for i in data.index.values:
    line=data.loc[i,["录取高校名称","录取人数"]].to_dict()
    list.append(line)
dict['data']=list
print(dict)

for a_list in dict.values():
    print(a_list)

name_dict={}
for i in a_list:
    name_dict[i["录取高校名称"]]=i["录取人数"]
print(name_dict)

from pyecharts.charts import WordCloud
import numpy as np

x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2 #此时mask是bool型
mask = 255 * mask.astype(int)  #变量类型转换为int型

wordCloud = WordCloud()
wordCloud.add(series_name="", data_pair=name_dict.items(), word_size_range=[20, 60])
wordCloud.render("录取.html")
print("success")

