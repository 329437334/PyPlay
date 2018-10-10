import json
"""
json 是一种时下非常流行的数据格式
在 python 中可以方便地使用 json 格式序列化/反序列化字典或者列表
"""

from utils import log


def save(data, path):
    """
    本函数把一个 dict 或者 list 写入文件
    data 是 dict 或者 list
    path 是保存文件的路径
    """
    # json 是一个序列化/反序列化(上课会讲这两个名词) list/dict 的库
    # indent 是缩进
    # ensure_ascii=False 用于保存中文
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        log('save', path, s, data)
        f.write(s)


def load(path):
    """
    本函数从一个文件中载入数据并转化为 dict 或者 list
    path 是保存文件的路径
    """
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        log('load', s)
        return json.loads(s)


# Model 是用于存储数据的基类
class Model(object):
    def __init__(self):
        self.id = None

    # @classmethod 说明这是一个 类方法
    # 类方法的调用方式是  类名.类方法()
    @classmethod
    def db_path(cls):
        # classmethod 有一个参数是 class
        # 所以我们可以得到 class 的名字
        classname = cls.__name__
        path = 'db/{}.txt'.format(classname)
        return path

    @classmethod
    def new(cls, form):
        # 下面一句相当于 User(form) 或者 Msg(form)
        m = cls(form)
        return m

    @classmethod
    def all(cls):
        """
        得到一个类的所有存储的实例
        """
        path = cls.db_path()
        models = load(path)
        ms = [cls.new(m) for m in models]
        return ms

    @classmethod
    def find_by(cls, **kwargs):
        """
        u = User.find_by(username='gua')

        上面这句可以返回一个 username 属性为 'gua' 的 User 实例
        如果有多条这样的数据, 返回第一个
        如果没这样的数据, 返回 None

        注意, 这里参数的名字是可以变化的, 所以应该使用 **kwargs 功能
        """
        log('kwargs,', kwargs)
        k, v = '',''
        for key, value in kwargs.items():
            k, v = key, value
        all = cls,all()
        for m in all:
            if v == m.__dict__[k]:
                return m
        return None

    @classmethod
    def find_all(cls, **kwargs):
        """
        us = User.find_all(password='123')
        上面这句可以以 list 的形式返回所有 password 属性为 '123' 的 User 实例
        如果没这样的数据, 返回 []

        注意, 这里参数的名字是可以变化的, 所以应该使用 **kwargs 功能
        """
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        all = cls, all()
        data = []
        for m in all:
            if v == m.__dict__[k]:
                data.append(m)
        return data


    def save(self):
        """
        save 函数用于把一个 Model 的实例保存到文件中
        """
        models = self.all()
        if self.__dict__.get('id') is None:
            # 如果没有id则加上id
            if len(models) > 0:
                # 不是第一个数据
                self.id = models[-1].id + 1
            else:
                # 是第一条数据
                self.di = 1
            models.append(self)
        else:
            # 有 id 说明已经是存在于数据库文件中的数据了
            # 那么就找到这条数据并替换之
            index = -1
            for i, m in enumerate(models):
                if m.id == self.id:
                    index = i
                    break
            # 看看是否找到下标，如果存在就替换掉
            if index > -1:
                models[index] = self

            pass
        #保存
        log('models', models)
        models.append(self)
        # __dict__ 是包含了对象所有属性和值的字典
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)

    def __repr__(self):
        """
        这是一个 魔法函数
        不明白就看书或者 搜
        当你调用 str(o) 的时候
        实际上调用了 o.__str__()
        当没有 __str__ 的时候
        就调用 __repr__
        """
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} >\n'.format(classname, s)


        # 以下两个类用于实际的数据处理
        # 因为继承了 Model
        # 所以可以直接 save load
