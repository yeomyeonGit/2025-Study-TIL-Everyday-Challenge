charaters = []
sentence = '복돌이가 킁킁킁'

for char in sentence:
    charaters.append(char)

# print(charaters)

# print(list(sentence))

one_to_ten = list(range(1, 11))
# print(sum(one_to_ten))
# a = 0
# for i in one_to_ten:
#     a += i

# print(a)

chulsu = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 60, 70]

students = [chulsu, younghee, yong, minsu]

# for scores in students:
    # print(sum(scores), sum(scores)/3)

#연습 문제 1 아이돌 팬
newjeans = ['철수', '영희', '민수', '지현', '서연']
ive = ['영희', '민수', '지수', '서연', '하나']
aespa = ['철수', '지현', '지수', '서연', '나영']

newive = []
for fan in newjeans:
    if fan in ive:
        if fan not in aespa:
            newive.append(fan)

print(','.join(newive))

