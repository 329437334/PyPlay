list_x = [0, 1, 2, 1, 0, 0, 1, 0]

r = filter(lambda x: True if x == 1 else False, list_x)
print(list(r))
