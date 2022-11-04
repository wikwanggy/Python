# 다음은 Calculator 클래스이다.
# 아래 클래스를 상속하는 UpgradeCalculator를
# 만들고 값을 뺄 수 있는 minus 매서드를 추가해보자.
class Calculator:
    
    def __init__(self):
        self.value=0 #초깃값 value = 0으로 설정
    
    def add(self, val):
        self.value += val # value 값 + val 값

# 즉 다음과 같이 동작하는 클래스를 만들어야 한다.
class UpgradCalculator(Calculator): # 상속 클래스
        
    def minus(self, val):
       self.value -= val  # value 값 - val 값
       

cal=UpgradCalculator()

cal.add(10) # value 값에 10을 더하여 저장
cal.minus(7) # value에 저장되어있는 값(10)에서 7을 빼고 저장

print(cal.value) # 최종적으로 저장되어 있는 value 값을 출력

# 객체변수 value가 100 이상의 값은 가질 수 없도록
# 제한하는 MaxLimtCalculator클래스를 만들어보자.
# 즉 다음과 같이 동작해야한다.
# 단 반드시 ㄱ다음과 같은 Calculator클래스를 상속해서 만들어야한다.
class Calculator:
    def __init__(self):
        self.value = 0 # 초깃값 value = 0 으로 설정
    def add(self, val):
        self.value += val # value값 + val 값
class MaxLimtCalculator(Calculator): # 상속 클래스
    def add(self, val):
        self.value += val  # value 값 + val값
        if self.value > 100: # 만약에 self.value값이 100이 넘으면
            self.value=100 # self.value 값은 100으로 출력한다.
        

cal=MaxLimtCalculator() # 클래스 호출
cal.add(50) # value 값에 add(50)을 더하여 저장
cal.add(60) # value 값에 add(60)을 더하여 저장

print(cal.value) # 최종적으로 저장되어있는 값을 출력 (100이상일땐 100으로 제한)