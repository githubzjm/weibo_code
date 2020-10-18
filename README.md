# 爬取微博 博客信息、博主信息、博客评论、博客转发、关注者信息
## 使用方法
1. 配置utils.py中的project_dir user_agent m_cookie [获取cookie方法](https://github.com/dataabc/weiboSpider/blob/master/docs/cookie.md)
2. 打开keylist.csv，第一列写关键词，第二列写mid（博客id，注意在首位数字之前加'避免被Excel自动缩写）
3. 运行main.py，开始根据mid抓取数据
4. 打开data文件夹查看抓取结果