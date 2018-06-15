'''
    Create by MccRee
'''

from collections import namedtuple

from app.view_models.book import BookViewModel

MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyWishes:
    '''
    多个礼物
    '''

    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        # 定义两个私有实例属性
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list

        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        # 这里操作两个List
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        # 这里示例了用namedtuple和字典,这里选择用字典
        r = {
            'wishes_count':count,
            'book': BookViewModel(gift.book),
            'id':gift.id
        }
        return r


class MyWish:
    '''
    单个礼物
    '''

    def __init__(self):
        pass

