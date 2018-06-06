'''
    Create by MccRee
'''
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不可以为空,请输入你的密码'), Length(6, 32)])

    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要2个字符,最多10个字符')])



    def validate_email(self,field):
        '''
        # 自定义验证器函数名 validate_属性名,wtforms会自动执行

        # 业务校验,例如昵称重复,email重复等, 一般也放在forms层,需要用自定义验证器
        # .first()用来触发查询并返回一条结果就行
        '''
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')
