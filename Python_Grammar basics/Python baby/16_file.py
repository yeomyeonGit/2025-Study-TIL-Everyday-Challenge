# 파일 생성하기
##파일_객체 = open(파일이름, 파일열기모드)
f = open("새파일.txt", "w")
f.close()

f = open(
    "C:/Users/USER/OneDrive/바탕 화면/2025 everyday TIL/Python_Grammar basics/Python baby/test.txt",
    "w",
)

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()

'''
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)

    '''


# readline 함수 이용하기
'''
f = open(
    "C:/Users/USER/OneDrive/바탕 화면/2025 everyday TIL/Python_Grammar basics/Python baby/test.txt",
    "r",
)
line = f.readline()
print(line)
f.close() ##test.txt 파일의 첫번째 줄만 출력됨.

'''

##전부 다 출력하려면?
'''

f = open(
    "C:/Users/USER/OneDrive/바탕 화면/2025 everyday TIL/Python_Grammar basics/Python baby/test.txt",
    "r",
)

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

'''

#readlines 함수 사용하기

'''
f = open("C:/Users/USER/OneDrive/바탕 화면/2025 everyday TIL/Python_Grammar basics/Python baby/test.txt", 'r')
lines = f.readlines()

for line in lines:
    line = line.strip() #.strip()을 넣으면 /n 개행문자 제거. 폭이 좁아짐.
    print(line) #리스트로 반환해서, 각 줄마다 마지막에 개행 문자가 있기 때문에 줄바꿈을 포함해서 출력하는 print 함수 특성상 줄바꿈이 더 커보인다.

f.close()

while True:
    data = input()
    if not data: break
    print(data)

'''
    
#read 함수 사용하기

'''
f = open("C:/Users/USER/OneDrive/바탕 화면/2025 everyday TIL/Python_Grammar basics/Python baby/test.txt", 'r')
data = f.read()
print(data)  ##파일을 문자열로 반환
f.close()

'''

#파일 객체를 for 문과 함께 사용하기
f = open("C:/Users/USER/OneDrive/바탕 화면/2025 everyday TIL/Python_Grammar basics/Python baby/test.txt", 'r')
for line in f:
    print(line)
f.close()   ##파일 객체는 기본적으로 위와 같이 for 문과 함께 사용하여 파일을 줄 단위로 읽을 수 있다.


#파일에 새로운 내용 추가하기

'''
f = open("C:/Users/USER/OneDrive/바탕 화면/2025 everyday TIL/Python_Grammar basics/Python baby/test.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)

f.close()

f = open("C:/Users/USER/OneDrive/바탕 화면/2025 everyday TIL/Python_Grammar basics/Python baby/test.txt", 'r')
for line in f:
    print(line)
f.close()

'''

#with 문과 함께 사용하기
f = open("foo.txt", "w")
f.write("Life is too shor, you need Python")
f.close()   #파일을 열면 항상 닫아 주어야 한다.
##이렇게 파일을 열고 닫는 것을 자동으로 처리하는 것이 바로
##with

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need Python")
