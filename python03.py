from re import A
#문자열 길이 구하기

a="Life is too short"

print(len(a)) #17
print(a[2]) #f
print(a[-1]) #t
print(a[12]) #s

print(a[0:4]) #인덱스 0부터 4번째 글자까지
print(a[12:])
print(a[:4])

b="20221025wkg"
year=b[0:4]
month=b[4:6]
day=b[6:8]
name=b[8:]

print(year)
print(month)
print(day)
print(name)

#온도를 저장하는 변수 선언
temp=18

print("오늘은 %d도 입니다" %temp)

temp=20
print("오늘은 %d도 입니다" %temp)
print("오늘은 {0}도 입니다" .format(temp))

# 사과 갯수

count="5개"
print("나는 사과 %s를 먹었다." %count)
print("나는 사과 {0}를 먹었다." .format(count))

#나는 사과 10개를 먹었다. 그래서 나는 3일동안 아팠다
appcnt=10
day="3일"

print("나는 사과 %d개를 먹었다. 그래서 나는 %s일동안 아팠다" %(appcnt,day))
print("나는 사과 {0}개를 먹었다. 그래서 나는 {1}일동안 아팠다" .format(appcnt,day))
s="안녕"

print("%10s" %s)
print("{0:>10}".format(s))

s1="광규"

print("%-10s %s" %(s,s1))
print("{0:^10} {1}" .format(s,s1))
print("{0:<10} {1}" .format(s,s1))

f=3.42134234
print("%f" %f)
print("{0:f}" .format(f))

print("%0.4f" %f)
print("{0:0.4f}" .format(f))

print("%10.4f" %f)
print("{0:10.4f}" .format(f))
