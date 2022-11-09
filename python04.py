name="홍길동"
age=30

print(f"나의 이름은 {name}입니다. 나이는 {age+1}입니다.")

d={"name":"홍길동","age":30}
print(f"{d['name']}입니다. 나이는 {d['age']}입니다.")


print(f"{'hi':@<10}") #왼쪽정렬하고 @로 채움
print(f"{'hi':*^10}") #가운데정렬하고 *로 채움
print(f"{'hi':=>10}") #오른쪽정렬하고 =으로 채움

y=3.42134234

print(f"{y:0.4f}") #소수 넷째자리까지 표현
print(f"{y:10.4f}") #총 자릿수 10자 중에서 소수 넷째자리까지 표현


a="hobby"

print(len(a)) # 문자열 글자수 // 5
print(a.count("b")) #문자열에서 해당하는 글자 수 //2

# a="Python is the best choice"
# # Python is the best choice에서 b의 위치를 알려준다
# # 0부터 시작하기 때문에 15가 아니라 14를 결과로 출력
# print(a.find("b"))
# # Python is the best choice에서 "k"는 존재하지 않기 때문에 -1 
# print(a.find("k"))
# print(a.index("b"))
# # Python is the best choice에서 "k"는 존재하지 않기 때문에 error 발생
# print(a.index("k"))

print(",".join("abcd"))

print(",".join(['a','b','c','d']))


s="hi"
# 소문자를 대문자로 변환(upper)
print(s.upper())
s="HI"
# 대문자를 소문자로 변환(lower)
print(s.lower())

# 문자열에 공백 제거
# 왼쪽 공백 제거(lstrip)
s="      hi      "
print(s.lstrip())
# 오른쪽 공백 제거(rstrip)
s="      hi      "
print(s.rstrip())
# 양쪽 공백 제거(strip)
s="      hi      "
print(s.strip())

#문자열바꾸기(replace
s="정자바"
print(s.replace("자바","씨샵"))


#문자열 나누기
s="Life is too short"
c="a:b:c:d"
print(s.split())
print(c.split(":"))

