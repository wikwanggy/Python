from copy import copy # module
#변수
#변수명= 값
a=1
b="Python"
c=[1,2,3]

print(id(c))

a=[1,2,3]

b=a # a list 자료형에 있는 값을 b list 자료형에 저장
print(id(a))
print(id(b))
b=a[:] # a list에 처음 요소부터 끝 요소까지 슬라이싱
a[1]=4

print(a)
print(b)

a=[1,2,3]
b=copy(a)

print(id(a))
print(id(b))

#a="a"
#b="b"
a,b=("a","b")
(a,b)="a","b"

print(a)
print(b)

[a,b]=['python','life']

print(a)
print(b)

a=b='python'
print(a)
print(b)

a=3
b=5
a,b=b,a
print(a)
print(b)
