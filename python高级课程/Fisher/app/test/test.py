'''
    Create by MccRee
'''

from flask import Flask, current_app, request, Request

app = Flask(__name__)

#应用上下文 对象 Flask
#请求上下文 对象 Request
#Flask AppContext
#Request RequestContext

ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config['DEBUG']