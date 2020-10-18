import requests
from bs4 import BeautifulSoup
import re
import json
#from __future__ import print_function
import os
import time
import utils
import pandas as pd
import numpy as np
import glob
import codecs
# limit = 100
from spider import *

if __name__=="__main__":
    path = utils.project_dir + "/keylist.csv"
    file_lines = []
    try:
        file_lines=getFileList(path,0)
    except IOError:
        pass

    file_list=[]
    for i in range(len(file_lines)):
        line_params=file_lines[i].split(',')[:2] # 将每行各项分离放入列表
        file_list.append(line_params)
        
    # 将DataFrame的纵轴改为keyword mid
    dataframe = pd.DataFrame(file_list);
    old_names = list(range(2))
    new_names = ['keyword', 'mid']
    dataframe.rename(columns=dict(zip(old_names, new_names)), inplace=True)  
    dataframe=dataframe[new_names]
    # final_data1= final_data1.drop_duplicates(['mid'])

    # 从DataFrame中获取keyword列和mid列
    keywords=list(dataframe['keyword'])
    mid=list(dataframe['mid'])
    keywords_set=list(set(keywords)) # 无重复值的keywords

    # 将keyword相同的行合并，各自的mid放入列表
    documents=[]
    for key in keywords_set:
        mids=[]
        document=[] #["共青团", ['a', 'c']]
        for i in range(len(keywords)):
            if key==keywords[i]:
                mids.append(mid[i])
        document.append(key)
        document.append(mids)
        documents.append(document) # [['共青团', ['a\n', 'c\n']], ['肖战', ['b\n']]]
       
    for doc in documents:
        mid_list=[]# ['b'] ['a', 'c']
        for mid in doc[1]:
            # a=mid.split('/')[-1]
            a=mid.strip('\n')
            mid_list.append(a) 
        scrapy_info_mid(doc[0], mid_list)