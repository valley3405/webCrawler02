# encoding=utf-8
import requests
import urllib
from bs4 import BeautifulSoup

debug = True # 设置是否打印log
def log(message):
    if debug:
        print message


def download_image(url, save_path): 
    ''' 根据图片url下载图片到save_path '''
    try:
        img = requests.get(url,stream=True)
        with open(save_path,'wb') as fd:
            for chunk in img.iter_content():
                fd.write(chunk)
        log('Downloaded a image: ' + save_path)
    except Exception, e:
        print 'An error catched when download a image:', e

def load_page_html(url):
    ''' 得到页面的HTML文本 '''
    log('Get a html page : ' + url)
    return urllib.urlopen(url).read()

def down_page_images(page, save_dir):
    ''' 下载第page页的图片 '''
    html_context = load_page_html('http://qiubaichengren.com/%d.html' % page)
    soup = BeautifulSoup(html_context,'lxml')
    for ui_module_div in soup.findAll('div', {'class': 'ui-module'}):
        img_tag = ui_module_div.find('img')
        if img_tag is not None and img_tag.has_attr('alt') and img_tag.has_attr('src'):
            alt = img_tag.attrs['alt'] # 图片的介绍
            src = img_tag.attrs['src'] # 图片的地址
            filename = '%s%s' % (alt, src[-4:]) # 取后四位（有的图片后缀是'.jpg'而有的是'.gif'）
            download_image(src, save_dir + filename)

def download_qbcr(frm=1, page_count=1, save_dir='./'):
    for x in xrange(frm, frm + page_count):
        log('Page : ' + `x`)
        down_page_images(x, save_dir)

def main():
    base_path = '/home/git/temp/'
    download_qbcr(frm=1, page_count=2, save_dir=base_path)

if __name__ == '__main__':
    main()
