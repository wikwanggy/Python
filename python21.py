class Person: # 아무 기능 없는 Person클래스 생성
    pass
a=Person() # Person클래스의 인스턴스 a 생성

print(isinstance(a,Person)) #a가 Person클래스의 인스턴스인지 확인
b=3
print(isinstance(b,Person))

print(len("python"))
print(len([1,2,3]))
print(len((1,'a')))

print(list("python"))
print(list((1,2,3)))
a=[1,2,3]
b=list(a)
print(list(b))

#two_times.py
def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result
result=two_times([1,2,3,4])
print(result)

def two_times(x):
    return x*2
print(list(map(two_times,[1,2,3,4])))

print(list(map(lambda a: a*2, [1,2,3,4])))

print(max([1,2,3]))
print(max("python"))

print(min([1,2,3]))
print(min("python"))

print(oct(34))
print(oct(12345))

print(ord('a'))
print(ord('0'))

print(pow(2,4))
print(pow(3,3))

print(list(range(5)))
print(list(range(5,10)))
print(list(range(1,10,2)))

print(round(4.6))
print(round(4.2))
print(round(5.678,2))

print(sorted([3,1,2]))
print(sorted(['a','c','b']))
print(sorted("zero"))
print(sorted((3,1,2)))

print(str(3))
print(str('hi'))
print(str('hi'.upper()))

print(sum([1,2,3]))
print(sum([4,5,6]))

print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

print(type("abc"))
print(type(["abc"]))
print(type(open("test","w")))

print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip("abc","def")))