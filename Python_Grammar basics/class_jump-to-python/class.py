#클래스 만들기
'''
class FourCal:
    pass #그냥 통과. 임시로 만들고 아직 코드를 작성하지 않았을 때.

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal() #a는 객체, a는 클래스 FourCal의 인스턴스
a.setdata(4, 2)
a.first
a.second

a = FourCal()
b = FourCal()

a.setdata(4, 2)
print(a.first) #결과: 4

b.setdata(3, 7)
print(b.second)
print(a.first) #바뀌지 않음. 서로 다른 객체이기 때문에.

'''

class FourCal():
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result


# a = FourCal()
# # print(a.setdata(20, 2))
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div()) #'FourCal' object has no attribute 'first' 오류 발생.


#__init__ 실행돼야 할 코드를 항상 호출. 생성자
class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4, 2) #생성자를 자동으로 호출했기 때문에 first, second에 해당하는 값을
##전달해야 함

'''
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(a.first)
print(a.second)

'''

#클래스의 상속

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(MoreFourCal):
    def div(self):
        if self.second == 0:
            return 0
        
        else:
            result = self.first / self.second
        return result

# a = SafeFourCal(4, 0)

# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())
# print(a.pow())

# print(a.first)
# print(a.second)

##앞선 클래스를 상속받았기 때문에 FourCal 클래스의 기능을 모두 사용할 수 있다.

#메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        
        else:
            result = self.first / self.second
        return result

a = SafeFourCal(4, 0)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(a.first)
print(a.second) 

#메서드 오버라이딩은 상속한 클래스의 메서드를 새로 만든 클래스 내의 메서드로 수정하는 것.

#클래스 변수