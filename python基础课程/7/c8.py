import t.c7 as test
import t.c14

# t.c7.a = 666

# print(t.c7.a)
print(test.a)
print(t.c14.A)

from t.c7 import a
print(a)

from t import c7
print(c7.A)