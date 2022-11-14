# 파이썬 초보 탈출 코딩면허시험 20제
#1 문자열바꾸기
# a= "a:b:c:d"
# b=a.replace(":","#")
# print(b)
#2 딕셔너리 값 추출하기
# a={"A":90,"B":80}
#          key이 없을때 70을 출력
# print(a.get("C" ,       70))

#리스트 더하기와 extend 함수
# a=[1,2,3]
# a= a+[4,5]
# print(a)
# a=[1,2,3]
# a.extend([4,5]) 
# print(a)
# a+[4,5]와 a.extend([4,5])는 동일한 표현이다.

# 리스트 총합 구하기
# A=[20,55,67,82,45,33,90,87,100,25]
# total=0
# for score in A:
#     if score >= 50:
#         total += score
# a=total
# print(a)

# 피보나치 함수
# def fib(n):
#     if n == 0 : return 0 # n이 0일땐 0을 반환
#     if n == 1 : return 1 # n이 1일때는 1을 반환
#     return fib(n-2)+fib(n-1) # n이 2이상일 대는 그 이전의 두 값을 더하여 반환

# for i in range(10):
#     print(fib(i))

# 숫자의 총합 구하기
# N=6
# list1=[]
# for i in range(N):
#     list1.append(int(input("숫자를 입력해주세요.")))

# print(list1) 
# a=list1
# total=0
# for score in a:
#     total += score
# b=total
# print(b)

# 한줄구구단.
# number=int(input("구구단을 출력할 숫자를 입력하세요(2~9) :"))
# for j in range(1, 10):
#     print(number*j,end=" ")

# 역순 저장
# f=open("test3.txt","w")
# f.close()
# f=open("D:/python/test3.txt","w")
# data="""
# AAA
# BBB
# CCC
# DDD
# EEE
# """
# f.write(data)
# f.close()
# with open("D:/python/test3.txt","r") as f:
#     lines=f.readlines()
# lines.reverse()
# f = open('test3.txt', 'w')
# for line in lines:
#     line = line.strip()  # 포함되어 있는 줄 바꿈 문자 제거
#     f.write(line)
#     f.write('\n')        # 줄 바꿈 문자 삽입
# f.close()

# 평균값 구하기
# f=open("test4.txt","w")
# f.close()

# f=open("D:/python/test4.txt","w")
# data="""70
# 60
# 55
# 75
# 95
# 90
# 80
# 80
# 85
# 100
# """
# f.write(data)
# f.close()
# f=open("D:/python/test4.txt","r")
# lines=f.readlines()
# f.close

# total=0
# for line in lines:
#     score=int(line)
#     total += score
# avg=total/len(lines)

# f=open("D:/python/test5.txt","w")
# f.write(str(avg))

# f.close

# # 사칙연산 계산기
# class Calculator :
#     def __init__(self,numberlist):
#         self.numberlist=numberlist
#     def sum(self):
#         result=0
#         for num in self.numberlist:
#             result += num
#         return result
#     def avg(self):
#         total = self.sum()
#         return total/len(self.numberlist)
    
# cal1=Calculator([1,2,3,4,5])
# print(cal1.avg())
# print(cal1.sum())

# cal2=Calculator([6,7,8,9,10])
# print(cal2.avg())
# print(cal2.sum())