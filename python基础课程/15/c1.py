'''
Python中使用字典来代替switch
'''
day = 0


def get_Sunday():
    return 'Sunday'


def get_Monday():
    return 'Monday'


def get_Tuesday():
    return 'Tuesday'


def get_default():
    return 'Unknow'


switcher = {
    0: get_Sunday,
    1: get_Monday,
    2: get_Tuesday
}

day_name = switcher.get(day,get_default)()
print(day_name)
