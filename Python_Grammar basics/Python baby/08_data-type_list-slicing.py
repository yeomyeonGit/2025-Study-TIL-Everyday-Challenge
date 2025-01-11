p = 'Python'
# print(p[:2])

# h = 'Hello World!'
# print(h[:6] + p + '!')

# print(h.replace('Hello', 'Python'))

# fruit = ['apple', 'banana', 'cherry', 'mango', 'orange']
# print(fruit[2:])

#연습 문제 3: 회문 판별 함수 만들기
'''
def palindrome(word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    
    return print(result)

text = input('단어를 입력하세요: ')
palindrome(text)

'''
'''
def palindrome(word):
    if word.lower() == word[::-1].lower():
        result = True
    else:
        result = False
    
    return print(result)

text = input('단어를 입력하세요: ')
palindrome(text)

'''
'''
def palindrome(word):
    word = word.replace(' ', '')
    if word.lower() == word[::-1].lower():
        result = True
    else:
        result = False
    
    return print(result)

text = input('단어를 입력하세요: ')
palindrome(text)
'''

#연습 문제 4: 각 자리 숫자의 합을 구하는 함수
'''
def sum0fDigits(num):
    num = str(num)
    total = 0
    for i in range(len(num)):
        total += int(num[i])
    
    return print(total)

    '''

'''
def sum0fDigits(num):
    num = str(num)
    separate = []
    for i in num:
        separate.append(int(i))

    total = sum(separate)
    
    return print(total)

sum0fDigits(123456)

'''

#연습 문제 5
'''
score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]

stem_leaf = [[], [], []]

for num in score:
    if num < 10:
        stem_leaf[0].append(num)
    elif num < 20:
        stem_leaf[1].append(num % 10)
    else:
        stem_leaf[2].append(num % 20)

for i in range(len(stem_leaf)):
    print(f'{i}:', stem_leaf[i])
'''

#연습 문제 6
'''
map(함수, 리스트)

map(lambda x: x ** 2, range(5))             # 파이썬 2
[0, 1, 4, 9, 16]  

'''

def sum0fDigits1(num):
    numbers = str(num)
    a = 0
    for i in numbers:
        a += int(i)
    
    return a


