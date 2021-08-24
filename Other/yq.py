from numpy import nan
import requests
import json
import pandas as pd 
import os 
import time 
from pandas.core.frame import DataFrame
import 

pf=pd.read_excel('yq.xlsx')
for i in pf['time']:
    print(i)