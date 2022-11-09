# 길이가 3인 배열(python언어를 제외한 나머지 프로그래밍언어)
# 길이가 3인 리스트(python언어에서 사용되는 몇칭)
# 리스트 인덱싱
a=[1,2,3]

print(a[0]) # 1
print(a[-1]) # 3

b=[1,2,3,["a","b","c"]]

print(b[0]) # 1
print(b[3]) # ["a","b","c"]
print(b[-1]) # ["a","b","c"]
print(b[3][0]) # a
print(b[-1][0]) # a

c=[1,2,["a","b",["Life","is"]]]
print(c[2][2][0])

#리스트 슬라이싱
a="12345"
print(a[0:2]) # 12

b=[1,2,3,4,5]
print(b[:2]) # [1,2]
print(b[2:]) # [3,4,5]

d=[1,2,3,["a","b","c"],4,5]
print(d[2:5])
print(d[3][:2])

#리스트 연산하기
# 리스트 더하기
a=[1,2,3]
b=[4,5,6]
print(a+b) # [1,2,3,4,5,6] ( 리스트 + 리스트 값 결합 )
# 리스트 곱하기
print(a*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# 리스트 길이 구하기 
print(len(a)) # 3
# 정수와 문자열 결합할 때 
print(str(a[2]) + "h1") #3hi : str함수는 숫자(3) > 문자열"3"으로

#리스트의 수정과 삭제
# 리스트 값 수정하기
a=[1,2,3]
a[2]=4
print(a)

# 리스트 요소 삭제하기
a=[1,2,3]
del a[1]
print(a) # [1,3]
# 리스트 슬라이싱 삭제
a=[1,2,3,4,5]
del a[2:]
print(a) # [1,2]

# 리스트 관련 함수
# 리스트에 요소 추가(append)
a=[1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)

# 리스트 정렬(sort)
a=[1,4,3,2]
a.sort() # 오름차순(기본값 : reverse=False)
a.sort(reverse=False) # 오름차순
print(a)
a.sort(reverse=True) # 내림차순
print(a)
a=['a','c','b']
a.sort()
print(a)

# 리스트 뒤집기(reverse)
a=['a','c','b']
a.reverse()
print(a)

# 위치 반환(index)
a=[1,2,3]
print(a.index(3)) # 2
print(a.index(1)) # 0

# 리스트 요소 삽입(insert)
a=[1,2,3]
a.insert(0, 4)
print(a) # [4,1,2,3]

# 리스트 요소 제거(remove)
a=[1,2,3,1,2,3]
a.remove(3)
print(a) # 첫번째 3 [1,2,1,2,3] 
a.remove(3)
print(a) # 두번째[1,2,1,2]

# 리스트 요소 끄집어내기(pop)
a=[1,2,3] 
print(a.pop()) # 3
print(a) # [1,2]

a=[1,2,3] 
print(a.pop(1)) # 2
print(a) # [1,3]

# 리스트에 포함된 요소 개수 세기(count)
s="안녕하세여"
print(len(s)) # s변수에 저장되어 있는 글자수 (5)
print(s.count("세")) # 안녕하세요. 문자열에 "세"라는 문자열이 몇개가 있는지.
a=[1,2,3,1]
print(len(a)) # a리스트의 길이(4)
print(a.count(1)) # a리스트에서 1값의 갯수

# 리스트 확장(extend)
a=[1,2,3]
a.extend([4,5])
print(a) # [1,2,3,4,5]
b=[6,7]
a.extend(b)
print(a) # [1,2,3,4,5,6,7]

