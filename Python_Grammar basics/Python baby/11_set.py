# set은 집합을 표현함

fruits = {"apple", "banana", "orange"}

fruits.add("gold kiwi")

##set은 순서가 없구나!


companies = {"apple", "microsoft", "google"}

type(fruits)
type(companies)

##set은 집합이니까 교집합, 합집합을 이용할 수 있구나!
fruits & companies  # 교집합
fruits | companies  # 합집합

list_of_sets = [fruits, companies]
set.intersection(*list_of_sets)  # 교집합
set.union(*list_of_sets)  # 합집합

alphabet = list('google')
alphabet ## ['g', 'o', 'o', 'g', 'l', 'e']
set(alphabet) ## {'o', 'e', 'l', 'g'}

##set은 중복을 지우고, 원소의 순서도 유지하지 않는다.

s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {3, 6, 9}

s1 - s2 ##뺄셈은 되는데 덧셈은 지원이 안되네?


#연습 문제 1: 아이돌 팬

newjeans = {'철수', '영희', '민수', '지현', '서연'}
ive = {'영희', '민수', '지수', '서연', '하나'}
aespa = {'철수', '지현', '지수', '서연', '나영'}

newive = newjeans & ive
not_aespa = newive - aespa

not_aespa


#연습 문제 2: 주사위 눈의 합

dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)

#원소를 하나씩 방문해서 더한다.
#집합에 넣어서 중복을 제거한다.

randomlist = set()
for num1 in dice1:
    for num2 in dice2:
        a = num1 + num2
        randomlist.add(a)
    
randomlist


#연습 문제 3: 끝말 잇기 (1)
##1. 입력
##2. 셋에 추가. 이러면 중복 방지
##3. 마지막 글자랑 첫번째 글자가 같으면 다음으로 넘어감
##4. 아니면 '졌어' 출력

'''
game = set()
word = input('<시작> 끝말잇기를 하자. 내가 먼저 말할게.')
game.add(word)


word = input('<시작> 끝말잇기를 하자. 내가 먼저 말할게.')

while True:
    word_forward = input('')
    if word == word_forward:
        print('아까 했던 말이야. 내가 이겼어!<끝>')
        break
    elif word[-1] == word_forward[0]:
        game.add(word)
    else:
        print()

        '''