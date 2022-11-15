# 리스트 자료형, 튜플 자료형, 문자열 자료형
# for 변수명 in 자료형
test_list=["one","two","three"]
for i in test_list:
    print(i)
    
a = [(1,2),(3,4),(5,6)]
for(first, last) in a:
    print(first+last)

# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격
# 그렇지 않으면 불합격
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다."% number)
    else:
        print("%d번 학생은 불합격입니다."% number)

# for문과 continue문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생은 합격입니다."% number)

# for문과 함께 자주 사용하는 range 함수
a = range(10) # 0~9인 숫자를 포함하는 range 객체
print(a) # 0 ~ 9

a = range(11)
print(a) # 1 ~ 10

add = 0
for i in range(1, 11):
    add = add + i
print(add) # 55

# 2~9
for i in range(2, 10):
    # 1~9
    for j in range(1, 10):
        print(i*j,end=" ")
    print("")
    
# 리스트 내포(리스트 안에 for문을 포함하는 것) 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
# [3, 6, 9, 12]

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)


# 연습문제 1. 다음 코드의 결괏값은 무엇일까?
a = "Life is too short, you need python"

if "wife" in a:print("wife") # x
elif "python" in a and "you" not in a: print("python") # x
elif "shirt" not in a:print("shirt") # o
elif "need" in a: print("need") # o
else:print("none")

# 연습문제 2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1

print(result) # 166833 출력
    
# 연습문제 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
i = 0
while True:
    i += 1
    if i > 5:break
    print("*"*i)

# 연습문제 4. for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for i in range(1,101):
    print(i)
    
# 연습문제 5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for score in A:
#     total += sum(score)
# print(score)
#average = total / 10
#print(average)

# 연습문제 6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

print(result)
numbers = [1,2,3,4,5]
result = [n % 2 == 0 for n in numbers]
print(result)