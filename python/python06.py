# 튜플 자료형
# 변경, 삭제 불가
t1=()
t2=(1,)
t3=(1,2,3)
t4=1,2,3
t5=('a','b',('ab','cd'))

t1=(1,2,'a','b')
t2=(3,4)
# 인덱싱
print(t1[0])
print(t1[3])
# 슬라이싱
print(t1[1:]) # 인덱스번호 1 ~ 끝까지

print(t1+t2) # t1에 t2 결합
print(t2*3) # t2를 3번 반복

print(len(t1)) # 길이 확인

#python 자료형

# list=[1,2,3]
# tuple=(1,2,3)
# dic={"name":"정자바","age":30}

#딕셔너리 a의 key로 1, value로 "hi"를 저장해보자
a={1:"hi"}

b={"a":[1,2,3]}

a={1:"a"}
print(a)
a[2]="b"
print(a)
a["name"]="pey"
print(a)

# 딕셔너리 a에 저자되어 있는 값을 사용하기
# 딕셔너리 이름[key]
grade={"pey":10,"julliet":99}

print(grade["pey"]) #10
print(grade["julliet"]) #99

a={1:"a",2:"b"}

print(a[1]) #a
print(a[2]) #b

b={1:"a",1:"b"}

print(b)


c={"a":[1,2,3]} # value에는 listm 자료형이 들어갈 수 있다.
# d={[1,2,3]:"a"} # key에는 list자료형이 들어갈 수 없다.
e={(1,2,3):"a"} #key에는 tuple자료형이 들어갈 수 있다.

print(c)
# print(d)
print(e)

# Key리스트 만들기(Keys)
# Key     value    key     value      key    value
a={"name":"pey","phone":"0119993323","brith":"1118"}

print(a.keys())# 딕셔너리 a에서 key들만 따로 저장(list)
print(a.values()) # 딕셔너리 a에서 value들만 따로 저장(list)
print(a.items()) # 딕셔너리 a에서 {key,value}을 list에 저장
print(a["name"])    #딕셔너리 a에서 key가 name인 value 값 가져오기
print(a.get("name")) #딕셔너리 a에서 key가 name인 value 값 가져오기
# print(a["1"])    #None:딕셔너리 a에 1이라는 키가 없으면 error
print(a.get("1")) #None : 딕셔너리 a에 1이라는 키가 없으면 None
print(a.get(1,"a")) #딕셔너리 a에서 key가 name인 value 값 가져오기
print("name" in a) #딕셔너리에 a에서 name인 key가 있는지 조사하기
print(a.clear()) # 딕셔너리 a에서 key와 value을 최기화

for k in a.keys():
    print(k)
    print("a")
print("b")

for k in a.values():
    print(k)


