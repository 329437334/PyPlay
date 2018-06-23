'''
爬取中央气象台图片
'''
import time
import requests
import json
from bs4 import BeautifulSoup

TIME_INTERVAL = 180
DEFAUL_URL = 'http://www.nmc.cn/publish/radar/jiang-su/chang-zhou.htm'

class Spider():

    def __init__(self):
        self.url = DEFAUL_URL
        self.file_dict = dict()

    def __fetch_content(self):
        '''
         取数据
        '''
        page = requests.get(self.url)
        page.encoding = 'utf-8'
        return page.text

    def __analysis(self, htmls):
        soup = BeautifulSoup(htmls, 'html.parser')
        # 拿到当前页时间点
        select_time = soup.find('select', {'id': 'plist'})
        options = select_time.find_all('option')
        time = [op.string for op in options][0]

        # 拿到图片地址
        img_tag = soup.find('img', {'id': 'imgpath'})
        src = img_tag['src']
        d = dict()
        d[time] = src
        print(d)
        return d

    def __save_to_file(self, dict):
        # 读写
        with open("中央气象台.json", "r") as f:
            self.file_dict = json.load(f)
            self.file_dict.update(dict)

        with open("中央气象台.json", "w") as f:
            json.dump(self.file_dict, f)

    def go(self):
        htmls = self.__fetch_content()
        dict = self.__analysis(htmls)
        self.__save_to_file(dict)


if __name__ == '__main__':
    while True:
        print('开始爬取,' + '时间间隔:' + str(TIME_INTERVAL))
        spider = Spider()
        spider.go()
        time.sleep(TIME_INTERVAL)
