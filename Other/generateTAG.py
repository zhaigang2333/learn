from numpy import arange, nan
import requests
import json
import pandas as pd 
import os 
import time 
import numpy as np
from pandas.core.frame import DataFrame
import re
#文件夹路径
path='./zgss_yq'
url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/keyword?charset=UTF-8&access_token=24.9b97cd40de3f5602b6a9ea8d9100eae7.2592000.1630649963.282335-24649396"
headers = {
  'Content-Type': 'application/json'
}

title='标题'
content='txt'

def getresult(url,payload,headers):
  print('请求:')
  #print('请求数据',payload)
  payloaddata = json.dumps(payload)
  response = requests.request("POST", url, headers=headers, data=payloaddata)
  #print(json.loads(response.text))
  re=json.loads(response.text)
  if 'items' in re and len(re['items'])>0:
    print(re['items'])
    return re['items']
  else:
    return False



filelist=os.listdir(path)
for i in filelist:
  #要处理的文件列表
  print(path+'/'+i)
  #print(re.findall(r'emotion(.+?)\.',i)[0])
  p=re.findall(r'emotion(.+?)\.',i)[0]
  result_motion=[]
  result_classifiction=[]
  result_tags=[]
  pf=pd.read_excel(path+'/'+i)
  if title in pf.columns :
    for r in pf[[title,content]].iterrows():

      payload={
        "title": str(r[1][title])[:30],
        "content": r[1][content]
       }
      try:
          it=getresult(url,payload,headers)
      except Exception:
        print(Exception)
        continue
      if it != False:
          result_tags.append(it)
      else:
        print('无')
        result_tags.append(['无'])
      time.sleep(0.3)
  else:
    #print(pf['content'])
    # for j in pf['content']:
    #   if j!=nan:
    #     pass
    #     #print(j)
    #   if j==nan:
    #     pass
    pass
  print('result_tags',result_tags)
  try:
    for value in result_tags: 
          print('value:',value)  
          if value[0]!='无':
            for j in arange(len(value)):
              value[j]=value[j]['tag']
          else:
            pass
  except Exception:
    print(str(Exception))
    continue
  
  print('result_tags_new',result_tags)        

  if len(result_tags)==0:
    continue
  data=pd.concat([pd.DataFrame({k: v}) for k,v in enumerate(result_tags) ], axis=1)
  data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index,dtype=np.object)
  #print(data)
  pf.insert(pf.shape[1], 'brand', p)
  print('----采集完毕---- ',data)
  test=pd.concat([pf,data],axis=1)
  filename="tag_"+i
  print(filename)
  test.to_excel(path+'/'+filename)


# {
#   "title": "涪陵榨菜：“青疙瘩”变“金疙瘩”",
#   "content": "时下，涪陵榨菜原料青菜头进入丰收季。在重庆市涪陵区涉及青菜头种植的20多个乡镇的70多万亩青菜头田地里，农民在进行紧张的收砍工作。涪陵榨菜是重庆市农村经济中产销规模最大、品牌知名度最高、辐射带动能力最强的优势特色产业。涪陵区的青菜头种植加工带动了60万农民、近2000户加工户增收致富，“青疙瘩”青菜头成为了“金疙瘩”。"
# }



  



