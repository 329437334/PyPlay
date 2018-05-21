'''
爬虫小demo
'''
from urllib import request
import re


class Spider():
    url = 'https://www.panda.tv/cate/dota1'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        '''
         取数据
        '''
        r = request.urlopen(Spider.url)
        htmls = r.read()  # 这里得到的数字就是字节码bit
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __refine(self, anchors):
        '''
         数据精炼下
         strip()去掉空格的内置函数
        '''
        def l(anchor): return {'name': anchor['name'][0].strip(
        ),                          'number': anchor['number'][0]}
        return map(l, anchors)

    def __analysis(self, htmls):
        '''
         拿到数据
        '''
        anchors = []
        root_html = re.findall(Spider.root_pattern, htmls)
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    def __sort(self, anchors):
        '''
        排序
        '''
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        '''
        展示
        '''
        for rank in range(0, len(anchors)):
            print(str(rank + 1) + ' : ' +
                  anchors[rank]['name'] + '  ' + anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
