"""
c = 10
d = 20
c, d = d, c  # 튜플 = 튜플의 값
print(c, d)


def magu_print(x, y, z, *rest):
    print(x, y, z, rest)


## magu_print(1, 2, 3, 4)

"""

"""

t = ("a", "b", "c")  # 튜플
empty = ()

one = (5,)  # 튜플을 만들 때는 마지막에 ,을 찍어준다
##print(one)

p = (1, 2, 3)
q = p[:1] + (5,) + p[2:] #튜플에 원소 추가. 튜플끼리 잇기.
#리스트 수정이랑 동일

r = p[:1], 5 # ((1,), 5) #컴마로 이으면 튜플이 됨
print(r)

a1 = [1]
a2 = [2]
a3 = [3]

final = a1 + a2 + a3
print(final)

"""

# 연습 문제 1

"""

def sum0f2(x, y):
    a, b, c, d = x + y, x - y, x * y, x / y
    return a, b, c, d

    """

# 연습 문제 2


date = input("날짜 입력: ")

dmy = date.split()

if len(dmy) != 3:
    print("날짜를 형식에 맞게 입력해주세요")

else:
    year, month, day = dmy


    if len(year) != 4:
        print('연도를 네 자리로 입력하세요.')

    else:
        if len(month) == 1:
            month = "0" + month

        if len(day) == 1:
            day = "0" + day
            
        print(f"{year}/{month}/{day}")


"""
if len(dmy[0]) == 4:
    if int(dmy[1]) < 10:
        dmy[1] = "0" + dmy[1]
        if int(dmy[2]) < 10:
            dmy[2] = "0" + dmy[2]
        else:
            dmy[2] = dmy[2]
    else:
        dmy[1] = dmy[1]
        
    day, month, year = dmy[0], dmy[1], dmy[2]
    print(f"{day}/{month}/{year}")
    
else:
    print('error!')
    """
