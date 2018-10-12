# coding utf-8
import requests
from bs4 import BeautifulSoup
import os

r = requests.post('https://www.cnblogs.com/sammy1989/category/919202.html')
# 获取整个页面的html
blog = r.content

# 用html.parser解析html
soup = BeautifulSoup(blog, "html.parser")
# print(soup)
images = soup.find_all(class_="lazy")
print(soup)
try:
    for i, j in images:
        jpg_rl = i["data-original"]
        png_rl2 = j["src"]
        title = i["title"]
        title2 = j["title"] + '01'
        print(title)
        print(jpg_rl)
        print("")
        with open(os.getcwd() + "\\jpg\\" + title + '.jpg', "wb") as f:
            f.write(requests.get(jpg_rl).content)
        with open(os.getcwd() + "\\png\\" + title + '.png', "wb") as e:
            e.write(requests.get(png_rl2).content)
except:
    pass
