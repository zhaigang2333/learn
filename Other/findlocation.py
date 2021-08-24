from numpy import nan
import requests
import json
import pandas as pd 
import os 
import time 
from pandas.core.frame import DataFrame

#url = "https://restapi.amap.com/v3/geocode/regeo?key=1c0e9d9301651aa28fb7a556ef9af1b6&location=107.397690,34.516220"

payload={}
headers = {}


n=0
def getres(lnglat):
    url="https://restapi.amap.com/v3/geocode/regeo?key=1c0e9d9301651aa28fb7a556ef9af1b6&location="+lnglat
    response = requests.request("GET", url, headers=headers, data=payload)
    res=json.loads(response.text)
    res_l2='',
    res_l3=''
    try:
        res_l2=res["regeocode"]["addressComponent"]["province"]+res["regeocode"]["addressComponent"]["district"]
        res_l3=res["regeocode"]["addressComponent"]["province"]+res["regeocode"]["addressComponent"]["district"]+res["regeocode"]["addressComponent"]["township"]
    except Exception:
        print(Exception)
    return res_l2,res_l3


l2=[]
l3=[]
pf=pd.read_excel('./realfile/全国企业数据详情.xlsx')
for r in pf['经纬度']:
    #print(r)
    res_l2,res_l3=getres(r)
    l2.append(res_l2)
    l3.append(res_l3)
    print('-----',n,'------')
    n=n+1

new={
    'l2':l2,
    'l3':l3
  }

data=DataFrame(new)#将字典转换成为数据框
#print(data)
print('----采集完毕---- ')
test=pd.concat([pf,data],axis=1)
test.to_excel('企业数据v1.xlsx')