# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:59:06 2022

@author: wytheY
"""

import pandas as pd
import pandas
import xlrd, xlwt
from xlutils.copy import copy as xl_copy
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook

rb = xlrd.open_workbook('期货手续费测试.xls', formatting_info=True)
# make a copy of it
wb = xl_copy(rb)
# add sheet to workbook with existing sheets
Sheet3 = wb.add_sheet('Sheet3')
wb.save('期货手续费测试.xls')

form_header = ['证券名称','结算费',]
df = pandas.DataFrame(columns=form_header)
df.to_excel('期货手续费测试.xls',sheet_name="Sheet3",index=False)

print('------ 开始筛选重复数据：')
# 新建个 DataFrame 用来保存过滤后的数据
df = pd.read_excel("期货手续费测试.xls",sheet_name="Sheet1",header=2)
new_scores = pandas.DataFrame()
# 用来标记是否已存在
existed_name = {}
for index, row in df.iterrows():
    if row['证券名称'] in existed_name:
        print('发现重复项：', row['证券名称'])
        continue
    existed_name[row['证券名称']] = True
    new_scores = new_scores.append(row, ignore_index=True)

print('------ 筛选后的表格：')
print(new_scores)
new_scores.to_excel('期货手续费测试.xlsx',sheet_name="Sheet3",index=False)

arr2 = []
for line in new_scores.证券名称:
    df = pd.read_excel("期货手续费测试.xls",header=2)
    df = df[df['证券名称'].isin([line])]
    df = sum(df.结算费)
    arr2.append(df)
print(arr2)


"""
print('------ 正在保存到新表格中')
new_scores.to_excel('S_INFO_WINDCODE.xlsx', index=False)

a = 0
print('------ 完成！') 
df = pd.read_excel('S_INFO_WINDCODE.xlsx')
with open("S_INFO_WINDCODE.csv",'w+',newline='') as t2:#numline是来控制空的行数的
    tit=["WINDCODE",]
    writer=csv.writer(t2)#这一步是创建一个csv的写入器
    writer.writerow(tit)#写入标签
    for line in df.S_INFO_WINDCODE:
        line = line[0:2]
        a = ''.join([i for i in line if not i.isdigit()]) #删除数字
        writer.writerow([a])
        t2.close
"""