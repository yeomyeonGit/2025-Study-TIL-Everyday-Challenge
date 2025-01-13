# Faker 라이브러리. 주소.

"""
from faker import Faker
from pprint import pprint

fake = Faker('Ko-KR')
print(fake.address())

test_data = [(fake.name(), fake.address()) for i in range(30)]
pprint(test_data)

"""

# sympy 방정식 미지수 대입해서 풀기

'''
from fractions import Fraction
import sympy

x = sympy.symbols("x")
f = sympy.Eq(x * Fraction("2/5"), 1760)

result = sympy.solve(f)
print(result)

remains = result[0] -1760
print(remains)

print('남은 돈은 {}원 입니다.'.format(remains))

'''

#sympy 활용 - 2차 방정식

import sympy

x= sympy.symbols("x")
f = sympy.Eq(x **2, 1)
print(sympy.solve(f))  ##[-1, 1]
