from numpy import nan
import requests
import json
import pandas as pd 
import os 
import time 
from pandas.core.frame import DataFrame


a=[]
b=[]
c=[]
d=[]
e=[]
f=[]


pf=pd.read_excel('榨菜政务相关信息orgin.xlsx')
for i in pf['tag']:
    if i=='无':
        a.append('无')
        b.append('无')
        c.append('无')
        d.append('无')
        e.append('无')
        f.append('无')
    else:
        content=eval(i)
        flag=len(content['lv2_tag_list'])
        print('flag',flag)
        if content['lv1_tag_list'][0]['tag']:
            a.append(content['lv1_tag_list'][0]['tag'])

        else:
            a.append('无')

        if 0 <=(flag-1) and len(content['lv2_tag_list'])>0 :
            print(content['lv2_tag_list'])
            b.append(content['lv2_tag_list'][0]['tag'])

        else:
            b.append('无')

        if 1 <=(flag-1) and len(content['lv2_tag_list'])>0 :
            c.append(content['lv2_tag_list'][1]['tag'])

        else:
            c.append('无')
        
        if 2 <=(flag-1) and len(content['lv2_tag_list'])>0 :
            d.append(content['lv2_tag_list'][2]['tag'])

        else:
            d.append('无')
       
        if 3 <=(flag-1) and len(content['lv2_tag_list'])>0 :
            e.append(content['lv2_tag_list'][3]['tag'])

        else:
            e.append('无')

        if 4 <=(flag-1) and len(content['lv2_tag_list'])>0 :
            f.append(content['lv2_tag_list'][4]['tag'])
        
        else:
            f.append('无')
new={
    'tag1':a,
    'tag2':b,
    'tag3':c,
    'tag4':d,
    'tag5':e,
    'tag6':f,
  }

print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

data=DataFrame(new)#将字典转换成为数据框

print('----采集完毕---- ')
test=pd.concat([pf,data],axis=1)
test.to_excel('test3.xlsx')
