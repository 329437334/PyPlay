class Human(object):
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        print(self.name)
