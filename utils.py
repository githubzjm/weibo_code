import re

# 爬取的博文转发、评论信息的最大数目
limit = 100

project_dir = "C:/Users/zjm/Desktop/weibo_code"
user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
m_cookie = "SUB=_2A25yPNC-DeRhGeBK4lMZ9SjLyj2IHXVR3vD2rDV6PUNbktANLXD2kW1NR2Zya3EcMYWtaHFyTyfEgP3cAmPYzy7K; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhZnFfJUFeK8jIIFp3ZrvPN5JpX5KzhUgL.FoqX1K2RSKqNeK22dJLoI79Ix-LFK0-t; SUHB=0z1AiqbiSQCXXR; _T_WM=60591421804; MLOGIN=1; M_WEIBOCN_PARAMS=featurecode%3D20000320%26oid%3D4495959310653349%26lfid%3D4495959310653349%26luicode%3D20000174"
# url = "https://m.weibo.cn/api/container/getIndex?type=all&queryVal=dota2&featurecode=20000320&luicode=10000011&lfid=106003type%3D1&title=dota2&containerid=100103type%3D1%26q%3Ddota2"
headers = {"User-Agent":user_agent,"cookie":m_cookie}

limted_time = ''
for i in range(2008,2015):
    limted_time = limted_time + str(i) + '|'
limted_time = limted_time[:-1]
re_limited_time = re.compile(limted_time)

d_cookie = "ALF=1512795836; SUB=_2A253B5HrDeRhGeRO4lEV9ivFzTuIHXVUCz-jrDV8PUJbkNBeLUvRkW2adzuZFzF5T0iGeBrk62FGeEH9EA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W50YwhuMpEHsRAAY_PboMLz5JpX5oz75NHD95QEeh.0Shqf1KqNWs4DqcjzKsHXIs-_dG2t; SINAGLOBAL=3020251936370.2905.1510205459247; httpsupgrade_ab=SSL; _s_tentry=www.baidu.com; UOR=www.baidu.com,weibo.com,www.baidu.com; Apache=989667688814.6017.1511687606193; ULV=1511687606206:5:5:1:989667688814.6017.1511687606193:1511423547830; SWBSSL=usrmdinst_3; SWB=usrmdinst_16; WBStorage=82ca67f06fa80da0|undefined"

h_headers = {"User-Agent":user_agent, "cookie": d_cookie}
