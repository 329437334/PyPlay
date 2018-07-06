'''
    Create by MccRee
'''
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

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
        # switch不同类型客户端注册不同
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        }
        # 函数作为字典的value,调用函数就是拿这个value
        promise[form.type.data]()
    return 'success'


def __register_user_by_email(form):
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
