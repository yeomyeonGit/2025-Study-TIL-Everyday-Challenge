##def hap(x, y):
##    return x + y

##print(hap(10, 20))

#lambda는 함수를 아주아주 쉽게 표현하는 방법

##(lambda x, y: x + y)(30, 20)

##print(list(map(lambda x: x ** 2, range(5))))

##from functools import reduce
##print(reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]))

print(list(filter(lambda x: x < 5, range(10))))

print(list(filter(lambda x: x % 2 == 0, range(10))))