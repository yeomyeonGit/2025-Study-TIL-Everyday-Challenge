# 문자열과 리스트

"""

x = 'banana'
print(x[0])

print(x[2:4])
print(x[:5])

"""

# print(type(x[0]))

##x[0] = 'n' #결과: TypeError. 문자열에 들어있는 글자는 바꿀 수 없다


# 메서드 연습
"""

s = "hello Python!"
h = s[0:6]

print(h[0:5])
print(len(h.rstrip()))
print(len(h))
print(s.split()[0])

"""


prime = [3, 7, 11]

prime.append(5)
# print(prime)

prime.sort()
# print(prime)


prime.insert(0, 2)
# print(prime)

del prime[4]
# print(prime)

a = prime.pop(2)
# print(prime)
# print(a)

prime[0] = 1
# print(prime)

orders = ['potato', ['pizza', 'coke', 'salad'],
          'hamburger']
# print(orders[1])
# print(orders[1][2]) #리스트 접근하는 방법

#행렬
matrix =[[1,2,3], [4,5,6], [7,8,9]]