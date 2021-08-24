from numpy import nan
import requests
import json
import pandas as pd 
import os 
import time 
from pandas.core.frame import DataFrame
#文件夹路径
path='./zgss_yq'
url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token=24.9b97cd40de3f5602b6a9ea8d9100eae7.2592000.1630649963.282335-24649396"
headers = {
  'Content-Type': 'application/json'
}



def getresult(url,payload,headers):
  payloaddata = json.dumps(payload)
  response = requests.request("POST", url, headers=headers, data=payloaddata)
  #print(json.loads(response.text))
  re=json.loads(response.text)
  if 'items' in re:
    print(re['items'][0]['positive_prob'])
    return re['items'][0]['positive_prob'],re['items'][0]['negative_prob']
  else:
    return False,False

title='标题'
content='txt'

filelist=os.listdir(path)
for i in filelist:
  #要处理的文件列表
  print(path+'/'+i)
  result_motion=[]
  result_classifiction=[]
  result_positive=[]
  result_negative=[]
  pf=pd.read_excel(path+'/'+i)
  if title in pf.columns :
    for r in pf[[title,content]].iterrows():

      # print(r[1]['title'])
      # print(r[1]['content'])
      payload={
        # "title": r[1]['标题'],
        "text": r[1][content]
       }
      try:
          p,n=getresult(url,payload,headers)
      except Exception:
        print(Exception)
        continue
      if p != False:
          result_positive.append(p)
          result_negative.append(n)
      else:
        print('无')
        result_positive.append('无')
        result_negative.append('无')
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
  new={
    'positive':result_positive,
    'negative':result_negative
  }

  data=DataFrame(new)#将字典转换成为数据框
  #print(data)
  print('----采集完毕---- ')
  test=pd.concat([pf,data],axis=1)
  filename="emotion"+i
  test.to_excel(path+'/'+filename)




# {
#   "title": "涪陵榨菜：“青疙瘩”变“金疙瘩”",
#   "content": "时下，涪陵榨菜原料青菜头进入丰收季。在重庆市涪陵区涉及青菜头种植的20多个乡镇的70多万亩青菜头田地里，农民在进行紧张的收砍工作。涪陵榨菜是重庆市农村经济中产销规模最大、品牌知名度最高、辐射带动能力最强的优势特色产业。涪陵区的青菜头种植加工带动了60万农民、近2000户加工户增收致富，“青疙瘩”青菜头成为了“金疙瘩”。"
# }



