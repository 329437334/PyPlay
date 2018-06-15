'''
    Create by MccRee
'''
from app.view_models.book import BookViewModel


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self._parse(goods)

    def _parse(self, goods):
        '''
        索要者与赠送者名字数据处理转换
        '''
        self.total = len(goods)
        # 列表推导式
        self.trades = [self._map_to_trade(single) for single in goods]

    def _map_to_trade(self, single):
        if single.create_time:
            time = single.create_time.strftime('%Y-%m-%d')
        else:
            time = 'Unknow'
        return dict(
            user_name=single.user.nickname,
            # strftime时间戳转格式日期
            time=time,
            id=single.id
        )


class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []
        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list
        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for trade in self.__trades_of_mine:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)
        return temp_trades


    def __matching(self, trade):
        count = 0
        for wish_count in self.__trade_count_list:
            if trade.isbn == wish_count['isbn']:
                count = wish_count['count']
        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        # 这里示例了用namedtuple和字典,这里选择用字典
        r = {
            # 这里因为前端还是用wishes_count字段来解析的所以这里用了
            'wishes_count':count,
            'book': BookViewModel(trade.book),
            'id':trade.id
        }
        return r