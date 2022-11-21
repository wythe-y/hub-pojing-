# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:59:06 2022

@author: wytheY
"""

import pandas as pd
import pandas

print('------ 开始筛选重复数据：')
# 新建个 DataFrame 用来保存过滤后的数据
df = pd.read_excel(r"C:\Users\wytheY\Desktop\期货手续费_8120_8120-中泰资管（代8001定向）-兴业上海_[2022-09-01_2022-10-10].xls",sheet_name="Sheet1",header=2)
#将文件的路径名称改变后放入原文件，默认为桌面
new_scores = pandas.DataFrame()
# 用来标记是否已存在
existed_name = {}
for index, row in df.iterrows():
    if row['市场代码'] in existed_name:
        print('发现重复项：', row['市场代码'])
        continue
    existed_name[row['市场代码']] = True
    new_scores = new_scores.append(row, ignore_index=True)
new_scores = new_scores.市场代码
print('------ 筛选后的表格：')
#print(new_scores)
df1 = pd.DataFrame()#生成空df
#print(df1)


arr2 = []
new_scores = list(new_scores)
new_scores.sort()
#print(new_scores)
df1.insert(loc=0, column='证券代码', value=new_scores)#证券代码
#print(df1)
for line in new_scores:
    df = pd.read_excel(r"C:\Users\wytheY\Desktop\期货手续费_8120_8120-中泰资管（代8001定向）-兴业上海_[2022-09-01_2022-10-10].xls",header=2)
    df = df[df['市场代码'].isin([line])]
  # print(df)
    df = sum(df.结算费)
    arr2.append(df)
#print(arr2)
df = pd.DataFrame(arr2)
df1.insert(loc=1, column='结算费', value=df)#结算费
df1.to_excel(r"C:\Users\wytheY\Desktop\结算费.xlsx",index=False)#生成文件if index = true 则增加序号
#将文件的路径名称改变后输出原文件，默认为桌面
arr3 = []
arr4 = []
k = 0
show = 0
for line2 in df1.证券代码:
    line2 = str(line2)
    line2 = line2.rstrip('0123456789')
   #print(line2)
    df4 = df1.loc[df1['证券代码'].str.contains(line2)] #筛选（包含）
    for linee in df4.证券代码:
        if line2 != linee.rstrip('0123456789'):
           df8 = df4[df4['证券代码'].isin([linee])]
          #show = linee.rstrip('0123456789')
           k = k+sum(df8.结算费)
          #print(k)
    df3 = sum(df4.结算费) - k
    k = 0
    arr4.append(df3)
    arr3.append(line2)
df2 = pd.DataFrame()
df2.insert(loc=0, column='证券代码', value=arr3)#证券代码
df2.insert(loc=1, column='结算费', value=arr4)#结算费

    # list1 = list(line2)
    # def is_odd(n):
    #     if n!= 0 or n%2 == 1 or n%2 == 0:
    #         reture n
    # tmplist = filter(is_odd, list1)
    # newlist = str(tmplist)
    # print(newlist)
arr5 = []
new_scores2 = pandas.DataFrame()
index,row = 0,0
# 用来标记是否已存在
existed_name2 = {}
for index, row in df2.iterrows():
    if row['证券代码'] in existed_name2:
        print('发现重复项：', row['证券代码'])
        continue
    existed_name2[row['证券代码']] = True
    new_scores2 = new_scores2.append(row, ignore_index=True)
new_scores2 = new_scores2.证券代码
print('------ 筛选后的表格：')
#print(new_scores)

for line3 in new_scores2:
    df6 = df2[df2['证券代码'].isin([line3])]
    df6 = df6.结算费
    df6 = df6.head(1)
    df6 = df6.values
    df6 = str(df6)
    df6 = df6.replace("[","")
    df6 = df6.replace("]","")
    df6 = float(df6)
   #print(df6)
    arr5.append(df6)
df7 = pd.DataFrame()
df7.insert(loc=0, column='证券代码', value=new_scores2)#结算费
df7.insert(loc=1, column='结算费', value=arr5)#结算费
df7.to_excel(r"C:\Users\wytheY\Desktop\结算费2.xlsx",index=False)#生成文件if index = true 则增加序号
