#주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수 (is_odd)를 작성해보자.
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
result=is_odd(7)
print(result)

#입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

def avg_number(*args):
    result=0
    for i in args:
        result +=i
    return result/len(args)
a=avg_number(1,2)
b=avg_number(1,2,3,4,5)
print(a)
print(b)

# 다음은 두개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
input1=input("첫번째 숫자를 입력하세요: ")
input2=input("두번째 숫자를 입력하세요: ")

total=int(input1)+int(input2)
print("두 수의 합은 %s 입니다" %total)

# 다음 중 출력 결과가 다른 것 한개를 골라보자 답은 3변
print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))