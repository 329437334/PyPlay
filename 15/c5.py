class Test():
    pass
    def __bool__(self):
        return False
    
    def __len__(self):
        return 8

t = Test()
print(bool(t))