'''
    Create by mccree
'''

from app import create_app

app = create_app()


if __name__ == '__main__':
    # 生成环境一般会使用 nginx+uwsgi 由uwsgi来加载fisher.py,所以app.run不会被执行
    # app.run会启动flask内置的webServer,生产环境一般不用内置的webServer
    # threaded开启多线程
    # processes = 1开启多进程
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000, threaded=True)

