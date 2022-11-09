# 함수(def)
# 두 수를 더하는 add함수 선언
def add(a,b):
    return a+b
# 두 수를 더하는 add 함수 호출
c=add(3,4)

print(c)

#입력값 O 반환값 O
def add(a,b):
    return a+b

#입력값 O 반환값 X
def add(a,b):
    print("%d, %d의 합은 %d 입니다" %(a,b,a+b))

#입력값 X 반환값 O
def add():
    return 10

#입력값 X 반환값 X
# 함수 선언
def add():
    print("10을 출력합니다.")

def add_many(*args):
    result = 0
    for i in args:
        result = result+i
    return result

# 함수 호출
result=add_many(1,2,3)

print(result)
result=add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

# 사용자가 "+"를 입력하면 값을 더하고,
# 사용자가 "*"를 선택하면 값을 곱하라(함수선언)
def add_mul(choice, *args):
    if choice == "+": # "+"를 선택하면
        result=0
        for i in args:
            result=result+i # 값들을 더하라
    elif choice == "*": # "*"를 선택하면 
        result=1
        for i in args:
            result=result*i #값들을 곱하라
    return result
# 사용자가 "+"를 입력하면 값을 더하고,
# 사용자가 "*"를 선택하면 값을 곱하라(함수  호출)
result=add_mul("+",1,2,3,4,5)
print(result)
result=add_mul("*",1,2,3,4,5)
print(result)

def add_and_mul(a,b):
    return a+b, a*b # 이런식으로 두개의 return은 됨(python만)
def add_and_mul(a,b):
    return a+b
    return a*b # 이런식으로 두개의  return은 안됌 
result=add_and_mul(3,4)
print(result)

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d입니다." %old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다.")

result=say_myself("위광규",25)

#변수의 범위
a=1
def vartest(a):
    a=a+1
vartest(a)
print(a)
#return 사용하기
a=1
def vartest(a):
    a=a+1
    return a
a=vartest(a)
print(a)
#global 사용하기
a=1
def vartest():
    global a
    a=a+1
vartest()
print(a)
# 일반적인 함수 표현
def addLamda(a,b):
    return (a+b)
result=addLamda(3,4)
print(result)
#lamda 식 함수표현
add=lambda a, b: a+b
result=add(3,4)
print(result)
