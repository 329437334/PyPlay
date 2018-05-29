'''
    create by mccree
    配置文件
    Secure一般放一些敏感数据，区分调试环境的参数，也不传git
'''

#注意配置文件参数要大写不然会被忽略
DEBUG = True

#数据库的连接项必须这么写  '数据库+数据库驱动://用户名:密码@139.196.52.216:端口/库名'
#单数据库,同时也支持分布式数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://jy:mql901111@139.196.52.216:3306/junyu'