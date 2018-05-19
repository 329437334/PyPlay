import json

json_str = '{"name":"qiyue", "age":18}'

stu = json.loads(json_str)
print(type(stu))
print(stu)


student = [{'name': 'qiyue', 'age': 18, 'flag': False},
           {'name': 'qiyue', 'age': 19, 'flag': True}]

string = json.dumps(student)
print(string)
