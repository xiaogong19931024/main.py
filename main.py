import pandas as pd                                   #导入pandas库
from pyecharts import options as opts
from pyecharts.charts import Bar,Line
from pyecharts.globals import ThemeType              #这三行是导入pyecharts库.具体用法参考pyecharts官方文档
#D:\python\Lib\site-packages\pyecharts\datasets
# 指定文件路径
root_path = r'./我的考试成绩/历次考试成绩.xlsx'

#定义一个读取函数,读取Excel文件到pandas的DataFrame,并返回该DataFrame
def Readexcel(path, index_col='历次考试名称'):
    data = pd.read_excel(path, index_col=index_col)
    return data

#定义一个解析函数,将dataFrame解析成字典,方便循环遍历展示
def Parsedata(data: pd.DataFrame):
    dict_one = {}                           #声明一个空字典
    index_list = data.index.tolist()        #把DataFrame的索引存到一个列表
    col_list = data.columns.tolist()        #把DataFrame的列名存到一个列表
    for subject in col_list:                #通过循环,解析DataFrame到字典
        dict_one[subject] = data[subject].values.tolist()
    return dict_one, index_list

#定义一个展示函数,将解析好的字典,借助百度的echarts展示
def Revealdata(data_dict: dict, index_list):
    line = Line(
        opts.InitOpts(
            width="1600px",             #设置长和宽
            height="800px",
            theme=ThemeType.DARK
        )
    )                                 #Bar柱状图  Line折线图
    line.add_xaxis(index_list)
    for key, value in data_dict.items():
        line.add_yaxis(key, value)
    line.render('我的历次考试成绩.html')       #生成一个html文件,用浏览器(谷歌浏览器)打开就能看到效果

#主函数
def Main():
    data = Readexcel(root_path)
    data_dict, index_list = Parsedata(data)
    Revealdata(data_dict, index_list)
#程序入口
Main()