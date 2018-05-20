# Python中的枚举
from enum import Enum


class VIP(Enum):
    yellow = 1
    yellow_sub = 1
    green = 2
    black = 3
    red = 4


# 枚举遍历
for v in VIP:
    print(v)

for v in VIP.__members__:
    print(v)


# result = VIP.yellow == 1
# 枚举类型不支持大小比较
# result = VIP.yellow < VIP.red
# print(result)
