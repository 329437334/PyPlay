import re

s = 'life is short, i user python, write python'

r = re.search('life(.*)python(.*)python', s)
print(r.group(1,2))
print(r.group())
