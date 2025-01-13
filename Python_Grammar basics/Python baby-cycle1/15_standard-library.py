#datetime.date: 연월일. 객체 함수 이용하면 요일도 출력 가능.

'''
import datetime

day1 = datetime.date(2021, 12, 14) #연월일 리턴하는 함수
day2 = datetime.date(2023, 4, 5)

print(day1)
print(day2)

diff = day2 - day1
print(diff)

print(day1.weekday()) #출력: 1 요일을 리턴하는 함수.
#datetime.date 객체의 weekday 함수.
#0부터 6까지. 0은 월요일, 6은 일요일

'''

#time.time 현재 시간을 실수 형태로 리턴하는 함수

'''
import time

print(time.time())

'''

##1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴해 준다.
##따라서 값이 계속 바뀜


#time.localtime

'''
print(time.localtime()) #연월일시분초요이일...의 평태로 바꿔주는 함수
print(time.asctime()) #위의 결과를 보기 좋게 정리해 줌.

'''

#time.ctime 
'''
import time
print(time.ctime())

'''

#time.strftime 형식을 반영해서 반환 (패스)

#time.sleep

'''
import time
for i in range(10):
    print(i)
    time.sleep(0.3) #time.sleep(1)보다 더 빠르구나!

    '''

##정리
'''
import time
print(time.localtime()) #연월일시분초요일... 튜플로 반환.
print(time.asctime())
print(time.strftime('%c')) #포맷 적용해서 반환

'''

#math.gcd 최대공약수를 찾는 함수
'''
import math
print(math.gcd(60, 100, 80))

'''

#math.lcm 최소공배수를 찾는 함수

#천천히 알아서 해보자~!