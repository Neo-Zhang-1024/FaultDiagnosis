# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:09:47 2019
轴承数据的预处理：
    输入：.csv文件；
    输出：100*1200的数组（100个包含1200个数据点的数组）
@author: Neo
"""

import pandas as pd

data = pd.read_csv('data.csv', engine='python')
headers = ['normal_2', 'B014_3', 'B021_2', 'B028_1', 'IR014_3', 'IR021_2',
           'IR028_1', 'OR014@6_3', 'OR021@6_2', 'OR021@12_1']
for i in headers:
    dat = data[i]
    arr0 = dat.values
    arr1 = arr0[:120000]
    arr2 = arr1.reshape(100, 1200)
    df = pd.DataFrame(arr2)
    df.to_csv(i+'.csv', index=False, header=False)
print('Done')