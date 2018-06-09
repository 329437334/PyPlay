'''
    Create by MccRee
'''

from .blueprint import web

@web.route('/wish')
def my_wish():
    pass


@web.route('/save/wish')
def save_to_wish():
    pass