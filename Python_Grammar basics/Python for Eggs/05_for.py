"""

family = ["엄마", "여명", "복돌이"]

for i in family:
    print(i, len(i))

"""

"""

a = list(range(2, 7))
print(a)

"""

"""
for i in range(4, 8):
    print(i)
    """

# 연습 문제 2
"""
num = int(input('정수를 입력하세요: '))

for i in range(num):
    print(num)

    """

# 연습 문제 3
"""
num = int(input('정수를 입력하세요: '))

for i in range(1, num+1):
    print(i, i * i)
    """

#for-else, while-else & break 문제

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    if input() == "중단":
        break
        
else:
    print("발사!")


for x in [1, 2, 3, 4]:
    if x % 3:
        print(x)
    else:
        break
else:
    print("리스트의 원소를 모두 출력했어요")
