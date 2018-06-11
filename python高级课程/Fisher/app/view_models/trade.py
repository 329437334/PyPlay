'''
    Create by MccRee
'''


class TradeInfo:
    def __init__(self,goods):
        self.total = 0
        self.trades = []
        self._parse(goods)


    def _parse(self,goods):
        '''
        索要者与赠送者名字数据处理转换
        '''
        self.total = len(goods)
        # 列表推导式
        self.trades = [self._map_to_trade(single) for single in goods]

    def _map_to_trade(self, single):
        return dict(
            user_name = single.user.nickname,
            #strftime时间戳转格式日期
            time = single.create_time.strftime('%Y-%m-%d'),
            id = single.id
        )