def f1(x):
    a = 3
    b = 5
    y = a * x + b
    return y


def f2(x):
    a = 3
    b = 5
    y = a * x + b
    print(y)


# 반환문 예제 1


def tri(a, b):
    return a * b / 2

    # a = int(input('높이: '))
    # b = int(input('밑변: '))

    # print(tri(a, b))


# 반환문 예제 2 - 참과 거짓


def quiz():
    ans = input("1 + 2 = ")
    return int(ans)


# 반환문 연습 문제 1


def korean_number(x):
    if x == 1:
        ans = "일"
    elif x == 2:
        ans = "이"
    elif x == 3:
        ans = "삼"
    else:
        ans = "사"

    return print(ans)


# 연습 문제 - 함수 정의하기


## 1. triple() 함수 구하기
def triple(x):
    ans = x * 3

    return print(ans)


## 2. 한국 나이 구하기
def korean_age(x):
    ## 2. 오늘의 날짜 객체 구하기 코드
    from datetime import datetime

    today = datetime.today()
    ans = today.year - x + 1

    return print(f"당신의 한국 나이는 {ans}살입니다.")


## 3-1. 이자 구하기


def simple_interest():
    # p = float(input("원금: "))
    # r = float(input("단리 이율: "))
    # t = float(input("기간: "))

    ans = p * r * t

    return print(ans)


#3-2. 원리금 계산

def simple_interest_amount(p, r, t):
    amount = p * (1 + r * t)
    return amount

    # print(simple_interest_amount(1000000, 3, 36))

#4. 놀이 공원
def read(text):
    # 이곳에 코드를 작성하세요.
    attraction_limit = text.split(':')
    if '이상' in attraction_limit[1]:
        ridename = attraction_limit[0]
        cmmin = attraction_limit[1].replace('cm 이상','')
        cmmax = None
    elif '~' in attraction_limit[1]:
        ridename = attraction_limit[0]
        cmmin = attraction_limit[1].split('~')[0].replace('cm', '')
        cmmax = attraction_limit[1].split('~')[1].replace('cm', '')
    else:
        ridename = attraction_limit[0]
        cmmin = None
        cmmax = None

    return ridename, cmmin, cmmax

a = input('놀이 기구: ')

if __name__ == "__main__":
    ridename, cmmin, cmmax = read(a)
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)

