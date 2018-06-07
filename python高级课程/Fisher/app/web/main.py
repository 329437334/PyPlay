'''
    Create by MccRee
'''

from .blueprint import web


@web.route('/')
def index():
    return 'hello YuShuBook'

@web.route('/personal')
def personal_center():
    pass