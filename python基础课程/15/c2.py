'''
列表推导式
'''

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i**2 for i in a]
# set
# dict
# tuple也可以推导
print(b)


students = {
    '希小白':18,
    '石刚党':20,
    '横小五':15
}

d = [key for key,value in students.items()]
print(d)
e = {value:key for key,value in students.items()}
print(e)