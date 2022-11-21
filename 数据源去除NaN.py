# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:43:36 2022

@author: wytheY
"""

import pandas as pd

df = pd.read_csv("历史数据.csv",)
#index_1为你需要检索的一列的名称，index等于创建了一个掩码
index=df
['S_DQ_CLOSE'].notnull()
df=df[index]
df.to_csv("历史数据2.csv",)

