class Student(object):
    # 这里定义的是类变量
    className = '类变量name'
    classAge = 0

    def __init__(self, name, age):
        # 构造函数
        # 使用self.来保存实例变量
        self.name = name
        self.age = age
        self.score = 0
        print(name)
        print(age)
        print('student')
        print(self.__class__.className)

    def marking(self, score):
        self.score = score
        if score < 0:
            score = 0

    def do_homework(self):
        print('do_homework')

    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))

    # 使用装饰器@classmethod就可以成为类方法
    @classmethod
    def plus_sum(cls):
        print('plus_sum')
        print(cls.className)

    # 静态方法,可以同时被对象和类调用
    @staticmethod
    def add(x, y):
        print('This is a static method')


student1 = Student('王金虎', 19)
student1.marking(59)
student1.print_file()
print(Student.className)
print(student1.__dict__)
Student.plus_sum()
