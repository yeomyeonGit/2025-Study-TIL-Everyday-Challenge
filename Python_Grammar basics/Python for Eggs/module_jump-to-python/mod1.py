#점프 투 파이썬

##모듈 만들기
def add(a, b):   #mod1.py
    return a + b

def sub(a, b):
    return a - b

# print(add(2, 4))
# print(sub(4, 2))  이렇게 하면 다른 곳에서 이 모듈 불렀을 때 


if __name__ == "__main__": #이걸 이 파일에서 실행하면
    print(add(1, 4))
    print(sub(4, 2))

import mod1