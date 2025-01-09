#지역변수, 전역변수

jjang = '가을' #전역변수
jjang = '복돌'

print(jjang)

def classroom(): 
    jjang = '카를레토' #지역변수 - 함수 안에서 만들어진 것
    print('jjang = ', jjang)

classroom()
print(jjang)
