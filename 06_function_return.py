def f1(x):
    a = 3
    b =5
    y = a * x + b
    return y


def f2(x):
    a = 3
    b = 5
    y = a * x + b
    print(y)


#반환문 예제 1

def tri(a, b):
    return a * b / 2

    # a = int(input('높이: '))
    # b = int(input('밑변: '))

    # print(tri(a, b))


#반환문 예제 2 - 참과 거짓

def quiz():
    ans = input('1 + 2 = ')
    return int(ans)

#반환문 연습 문제 1

def korean_number(x):
    if x == 1:
        ans = '일'
    elif x == 2:
        ans = '이'
    elif x == 3:
        ans = '삼'
    else:
        ans = '사'
    
    return print(ans)

korean_number(4)