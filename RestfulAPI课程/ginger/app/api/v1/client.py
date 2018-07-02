'''
    Create by MccRee
'''
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_clinet():
    # 注册
    # 参数 校验 接收参数
    # WTForms
    # 表单提交  网页
    # JSON提交 APP

    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        #switch不同类型客户端注册不同
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email,
        }


    pass


def __register_user_by_email():
    pass