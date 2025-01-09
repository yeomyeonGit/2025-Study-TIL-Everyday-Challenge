#지역변수, 전역변수

    # jjang = '가을' #전역변수
    # jjang = '복돌'

    # print(jjang)

    # def classroom(): 
    #     jjang = '카를레토' #지역변수 - 함수 안에서 만들어진 것
    #     print('jjang = ', jjang)

    # classroom()
    # print(jjang)

def d_is_10():
    d = 10
    print('d값은', d, '입니다')

## d_is_10()
## print(d) #전역변수와 지역변수의 차이

#지역변수 내 전역변수

def e_is_10():
    global e
    e = 10
    print('e값은 ', e, '입니다.')

e_is_10()
print(e) #지역변수 내 전역변수는 지역변수 내의 변수를 함수 밖에서도 쓸 수 있게 전역변수화 시키는 것.