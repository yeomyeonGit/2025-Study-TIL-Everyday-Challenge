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

