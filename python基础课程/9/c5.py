
from c6 import Human


class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        # 直接通过显示init调用,不推荐
        # Human.__init__(self, name, age)
        # 通过super来调用,减少耦合性
        super(Student, self).__init__(name, age)

    def do_homework(self):
        print('english homework')


stu1 = Student('学习1', '王大锤', 20)
# stu2 = Student('学校1', '王尼玛', 24)
print(stu1.name)
print(stu1.age)
# print(Student.sum)
# print(stu1.__dict__)
