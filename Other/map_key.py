from datetime import date
from numpy import nan
import requests
import json
import pandas as pd 
import os 
import time 
from pandas.core.frame import DataFrame
import re
import numpy as np

filename='./品牌/关键词.xlsx'
pf=pd.read_excel(filename)
data=[]



filename1='./品牌/关键词品牌数据采集.xlsx'
pf1=pd.read_excel(filename1)
flag=0
for i in pf1['标题']:
    flag=0
    for j in pf['品牌']:
      try:
        s=re.findall(j,i)
        if len(s)>0:
            flag=1
            data.append(j)
            print(s)
            break
      except Exception:
        print(str(Exception))
        break
    if flag==0:
        data.append(0)

new={
    '品牌':data
  }

data=DataFrame(new)#将字典转换成为数据框
 #print(data)
print('----采集完毕---- ')
test=pd.concat([pf1,data],axis=1)
filename2='./品牌/关键词品牌数据采集p.xlsx'
test.to_excel(filename2)
