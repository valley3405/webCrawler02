#!/usr/bin/env python
# encoding:utf-8

'''
爬虫，用于爬知乎某个问题下所有图片
'''

import re, requests
from bs4 import BeautifulSoup

#图片保存目录，需要修改为合适的目录
SAVE_DIR_PATH = '/home/git/zhihu/'

#女人什么样的脚才算的上是好看的脚？脚的审美该如何定义？
URL = 'http://www.zhihu.com/question/24279174'  


html = requests.get(URL).content

soup = BeautifulSoup(html,'lxml')

img_name = '1'
for imgurl_list_soup in soup.findAll('img', {'class':'origin_image zh-lightbox-thumb'}):
	imgurl = imgurl_list_soup.get('data-original')
	print imgurl
	ex = imgurl[-4:]
	img = requests.get(imgurl,stream=True)
	with open(SAVE_DIR_PATH+str(img_name)+ex,'wb') as fd:
		for chunk in img.iter_content():
			fd.write(chunk)
	img_name = img_name+1


'''
save = lambda url: open(SAVE_DIR_PATH + url[url.rfind('/')+1:], 'wb').write(requests.get(url).content)

if __name__ == '__main__':
    map(save, ['http:' + url for url in re.findall(ur'<img src=[\'"](//pic.+?)[\'"].+?>', requests.get(URL).content)])

'''