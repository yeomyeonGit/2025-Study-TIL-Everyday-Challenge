# 오류가 있을 때
"""
try:
    4 / 0

except ZeroDivisionError as e:
    print(e)

    """


# try-finally 문
"""
try:
    f = open('too.txt', 'w')

finally:
    f.close()

    """

# 여러 개의 오류 처리하기
"""
try:
    a = [1, 2]
    print(a[3])
    4 / 0

except ZeroDivisionError as e:
    print(e)

except IndexError as e:
    print(e)

    ##'list index out of range'만 나온다. 아래와 동일한 코드이다.

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

    """


# try-else 문
"""
try:
    age=int(input('나이를 입력하세요: '))

except:
    print('입력이 정확하지 않습니다.')

else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    
    else:
        print('환영합니다.')

        """

# 오류 회피하기
"""
try:
    f = open('나없는파일', 'r')

except FileNotFoundError:
    pass

    """


# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplemented


class Eagle(Bird):
    def fly(self):
        print("펄럭펄럭")


eagle = Eagle()
eagle.fly()
