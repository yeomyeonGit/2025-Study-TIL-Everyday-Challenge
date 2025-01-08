'''

start = 1
number = int(input('정수를 입력하세요: '))
a = 0

while start <= number:
    print(number)
    start += 1
    
    '''

''' number = int(input('정수를 입력하세요: '))
i = 1

while i <= number:
    print(i, i * i)
    i += 1
    '''

# i = 1
# popping = 100 * 0.6

# while i <= 10:
#     print(i, round(popping, 4))
#     i += 1
#     popping *= 0.6

#or

height = 100
bounce = 3 / 5

i = 1

while i <= 10:
    height = height * bounce
    print(i, round(height, 4))
    i += 1