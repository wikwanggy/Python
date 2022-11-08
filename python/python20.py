# 내장함수
print(abs(3)) #3
print(abs(-3)) #3
print(abs(-1.2))# 1.2

print(all([1,2,3])) # True
#         True && True && True => True
print(all([1,       2,      3])) # True (0:False, 0이 아닌 수:True)

#         True && True && True     False=> False
print(all([1,       2,      3,      0])) # False (0:False, 0이 아닌 수:True)

#         True || True || True  ||  False=> True
print(any([1,       2,      3,      0])) # True (0:False, 0이 아닌 수:True)

#         False || False=> False
print(any([0,       ""])) # False (0:False, 0이 아닌 수:True)

print(chr(98)) #'a'
print(chr(48)) # '0'

print(dir([1,2,3]))

print(divmod(7,3))

for i, name in enumerate(['body','foo','bar']):
    print(i, name)
    
def positive(l):
    result=[]
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))

#filter
def positive(x):
    return x > 0
print(list(filter(positive,[1,-3,2,0,-5,6])))

list(filter(lambda x: x>0,[1,-3,2,0,-5,6]))

print(hex(234))
print(hex(3))

a=3
print(id(3))
print(id(a))
b=a
print(id(b))

# a=input() #사용자가 입력한 정보를 변수 a에 저장
# print(a)
# b=input("Enter : ") # Enter : 프롬프트를 띄우고 사용자 입력을 받음
# print(b)

print(int('3')) # 문자열 형태'3'
print(int(3.4)) # 소수점이 있는 숫자 3.4

print(int('11',2))
print(int('1A',16))