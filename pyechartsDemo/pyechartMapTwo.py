from pyecharts import Map
import pandas as pd
#注意：省市不要包含“省"、"市"等字
data=[("广东",10430.03),("山东",9579.31),("河南",9402.36),("四川",8041.82),("江苏",7865.99),("河北",7185.42),("湖南",6568.37),("安徽",5950.1),("浙江",5442),("湖北",5723.77),("广西",4602.66),("云南",4596.6),("江西",4456.74),("辽宁",4374.63),("黑龙江",3831.22),("陕西",3732.74),("山西",3571.21),("福建",3552),("重庆",2884),("贵州",3476.65),("吉林",2746.22),("甘肃",2557.53),("内蒙古",2470.63),("上海",2301.391),("台湾",2316.2),("新疆",2181.33),("北京",1961.2),("天津",1293.82),("海南",867.15),("香港",709.76),("青海",562.67),("宁夏",630.14),("西藏",300.21),("澳门",55.23)]

data=pd.DataFrame(data)
data.columns=['city','popu']

map=Map("各省市人口数", "单位：万人", title_color="#fff", title_pos="center", width=1200,  height=600, background_color='#404a59')

attr=data['city']
value=data['popu']
map.add("", attr, value, visual_range=[min(value), max(value)],visual_text_color="#000", symbol_size=15,is_visualmap=True,is_label_show=True,label_pos = 'bottom')
map