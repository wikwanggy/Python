# 불 자료형 (boolean)
# Python에서는 대문자 T, 대문자 F임을 주의!!
a=True
b=False

print(1==1) #True
print(1<2)  #True
print(1>2)  #False

a=[] #list 자료형이나, 값은 없다.(False)
if a:
    print("참")
else:
    print("거짓")

b=[1,2,3] #list 자료형이나, 값이 있다.(True)
if b:
    print("참")
else:
    print("거짓")
    
print(bool("")) # False
print(bool("안녕")) # True

print(bool([])) #False
print(bool([1,2,3,])) #True