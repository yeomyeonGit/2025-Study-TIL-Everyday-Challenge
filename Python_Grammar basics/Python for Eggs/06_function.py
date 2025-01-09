#매개 변수가 있는 함수
'''

a_list = [3, 4, 62, 27, 83, 956, 26, 58, 3 ,78, 168, 64, 78]

def print_list(a):
    for i in a:
        print(i)

print_list(a_list)

'''

#매개 변수가 없는 함수

def boy():
    print('I am a boy')
    print('You are a gitl')


#혼자 연습

def compare(a, b):
    if a > b:
        print('a > b')
    elif a < b:
        print('a < b')
    else:
        print('a == b')

#연습 문제 1

def length(a):
    print(len((a)))


#연습 문제 2

def gugudan():
    a = 2
    while a <= 9:
        for i in range (1, 10):
            print(f'{a} * {i} = {a * i}')
    
        a += 1
    

