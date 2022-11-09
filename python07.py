# 집합 자료형 set
# set함수의 특징 
# 1. 중복하지 않는다.
# 2. 순서가 없다.
s1=set([1,2,3]) #set함수  list자료형 입력
print(s1)
s2=set("hello") #set함수 문자 자료형 입력
print(s2)

ls=list(s1) #set자료형 -> 리스트 자료형으로 변환 후 ls에 저장
print(ls) #[1,2,3]
print(ls[0]) # 1
print(ls[1]) # 2 
print(ls[2]) # 3

t1=tuple(s2) #set자료형을 -> 리스트 자료형으로 변환 후 t1에 저장
print(t1)
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#교집합 
print(s1&s2)
print(s1.intersection(s2))

#합집합
print(s1|s2)
print(s1.union(s2))

#차집합
print(s1-s2)
print(s1.difference(s2))

#기존에 있는 집합에 값 추가하기(add)

s1=set([1,2,3])
print(s1)
s1.add(4)
print(s1)

#기존에 있는 집합에 값 추가하기(update)
s1=set([1,2,3])
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기(remove)
s1=set([1,2,3])
s1.remove(2)
print(s1)