#조건에 따라 반복문 중단하기

'''
max = 10

while True:
    num = int(input())
    if num > max:
        print(num, "is too big!")
        break
        #조건에 따라 반복문 중단하기

        '''

#연습문제 1
'''
num = int(input('정수를 입력하세요: '))
if num == 1:
    print('일')
elif num == 2:
    print('이')
else:
    print('삼')

        '''

#연습 문제 2: 나이에 따른 세대 구분

'''
내가 쓴 코드

birth_year = int(input('출생년도: '))

if birth_year >= 1997:
    print('Z')

elif birth_year >= 1981:
    print('M')

elif birth_year >= 1965:
    print('X')

elif birth_year >= 1946:
    print('Boomer')

else:
    print('The Greatest')

'''

#답안 코드
'''
y = int(input('What year were you born?: '))
gen = None

if y <= 1924:
    gen = 'The Greatest'
elif y <= 1945:
    gen = 'the Silent'
elif y <= 1964:
    gen = 'Bommer'
elif y <= 1980:
    gen = 'X'
elif y <= 1996:
    gen = 'M'
else:
    gen = 'Z'

print(f'당신은 {gen}세대입니다.')

'''

#연습 문제 3번
'''

num = int(input('숫자를 입력하세요.: '))

if num >= 1000000000:
    num = num // 1000000000
    print(f'{num}G')
elif num >= 1000000:
    num = num // 1000000
    print(f'{num}M')
elif num >= 1000:
    num = num // 1000800
    print(f'{num}k')
else:
    pass
    
    '''

#연습 문제 4번

'''

start = 0

while True:
    num = int(input('정수를 입력하세요:'))
    if num >= 0:
        start += num
        print(start)
    else:
        break

'''

#연습문제 5번

'''해야 해... 그런데 집중력이 딸려'''

'''

s = 'banana'

if 'a' in s or 'c' in s:
    print(f'{s}에는 a또는 c가 있어요!')

    '''


