from models import Model
from  utils import log
class User(Model):
    def __init__(self, form):
        self.id = form.get('id', None)
        if self.id is not None:
            self.id = int(self.id)
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def validate_login(self):
        u = User.find_by(username=self.username)
        return u is not None and u.password == self.password

        # users = User.all()
        # log('所有用户:',users)
        # for user in users:
        #     if user.username == self.username and user.password == self.password:
        #         return True
        # return False

    def validate_register(self):
        return len(self.username) > 2 and len(self.password) > 2

