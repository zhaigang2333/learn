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

filename='./品牌/关键词品牌数据采集p.xlsx'
pf=pd.read_excel(filename)
data=[]
for i in pf['标题']:
    try:
        
        s=re.findall(r'\d{1,5}g|\*\d{1,4}|X\d{1,4}|\d{1,2}瓶装|\d{1,4}G|\d{1,4}kg|\d{1,4}斤|\d{1,2}包',i)
        print(i,s)
        data.append(s)
    except Exception:
        data.append([])
        print(str(Exception))
        continue
data=pd.concat([pd.DataFrame({k: v}) for k,v in enumerate(data) ], axis=1)
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index,dtype=np.object)
print(data)

test=pd.concat([pf,data],axis=1)
filename="tag_"+i
print(filename)
filename='./品牌/关键词品牌数据采集w.xlsx'
test.to_excel(filename)