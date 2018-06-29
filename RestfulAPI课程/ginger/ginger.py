'''
    Create by MccRee
'''
from app.app import create_app

app = create_app()



#启动web服务器
if __name__ == '__main__':
    app.run(debug=True)