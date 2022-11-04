result=0

def add1(num):      # add함수 선언
    global result1  # 전역변수
    result1 +=num   
    return result1
def add2(num):      # add함수 선언
    global result2  # 전역변수
    result2 +=num
    return result2
def add3(num):     # add함수 선언
    global result3 # 전역변수
    result3 +=num
    return result3

print(add1(3))
print(add1(4))

class Calculator: # class 선언
    
    def __init__(self): #생성자
        self.result=0
        
    def add(self,num):       # add 함수 선언
        global result   # 전역변수
        result += num
        return result
    
cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(4))

print(cal2.add(3))
print(cal2.add(7))