# result=0

# def add1(num):      # add함수 선언
#     global result1  # 전역변수
#     result1 +=num   
#     return result1
# def add2(num):      # add함수 선언
#     global result2  # 전역변수
#     result2 +=num
#     return result2
# def add3(num):     # add함수 선언
#     global result3 # 전역변수
#     result3 +=num
#     return result3

# print(add1(3))
# print(add1(4))

# class Calculator: # class 선언
    
#     def __init__(self): #생성자
#         result=0
        
#     def add(self,num):       # add 함수 선언
#         global result   # 전역변수
#         result += num
#         return result
# class Calculator: # class 선언
    
#     def __init__(self): #생성자
#         self.result=0
        
#     def add(self,num):       # add 함수 선언
#         self.result+=num
#         return self.result
    
# cal1=Calculator() # class 호출(Calculator 클래스 인스턴스) : Calculator cal1 = new Calculator();
# cal2=Calculator() # class 호출(Calculator 클래스 인스턴스) : Calculator cal2 = new Calculator();

# print(cal1.add(3)) # add 함수 호출
# print(cal1.add(4)) # add 함수 호출
# print(cal1.add(7)) # add 함수 호출

# print(cal2.add(3))  # add 함수 호출
# print(cal2.add(7))  # add 함수 호출
# print(cal2.add(4)) # add 함수 호출

class FourCal: # class 선언
    
    def __init__(self):
        self.first=0
        self.second=0
        
    # 두 수를 입력받아 오는 기능(setdata)
    def setdata(self,first, second):
        self.first=first
        self.second=second
    # 더하기 기능(add) 선언
    def add(self):
        result=self.first+self.second
        return result
    # 빼기 기능(sub) 선언
    def sub(self):
        result=self.first-self.second
        return result 
    # 나누기 기능(div) 선언
    def div(self):
        result=self.first/self.second
        return result
    # 곱하기 기능(mul) 선언
    def mul(self):
        result=self.first*self.second
        return result
    

fc=FourCal()     # FourCal클래스 호출(FourCal 인스턴스화): (자바 문법 :FourCal fc=new FourCal();_
fc.setdata(4,2)  # setdata 함수를 이용하여 first에는 4, second에는 2로 초기화

print(fc.first)
print(fc.second)
print(fc.add()) # FourCal 클래스에 있는 add함수 호출 setdata함수를 이용한 first와 second 값을 더함
print(fc.sub()) # FourCal 클래스에 있는 sub함수 호출 setdata함수를 이용한 first와 second 값을 뻼
print(fc.div()) # FourCal 클래스에 있는 div함수 호출 setdata함수를 이용한 first와 second 값을 나눔
print(fc.mul()) # FourCal 클래스에 있는 mul함수 호출 setdata함수를 이용한 first와 second 값을 곱함

# FourCal 클래스 - 부모클래스
# MoreFourCal 클래스 - 자식클래스
# MoreFourCal 클래스는 FourCal클래스로 부터 상속 받음
# java : MoreFourCal() extends FourCal
class MoreFourCal(FourCal): # 상속 - 자식클래스(부모클래스)
    def power(self):
        result=self.first ** self.second # ** 거듭제곱
        return result
    # 나누기 선언(div) - 오버라이딩
    def div(self): 
        if self.second==0 or self.first == 0:
            return 0
        else:
            return self.first/self.second

mfc=MoreFourCal()
mfc.setdata(4,2)
print(mfc.add())
print(mfc.sub())
mfc.setdata(4,0)
print(mfc.div())
mfc.setdata(4,2)
print(mfc.mul())
print(mfc.power())


class Family:
    lastname="김" # 클래스 변수

print(Family.lastname)
a=Family() # 자바 문법 : Family a = new Family();
b=Family() # 자바 문법 : Family b = new Family();
print(a.lastname)
print(b.lastname)