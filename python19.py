#f=open("나없는파일","r")
#print(4/0) # ZeroDivisionError
# a=[1,2,3]
# print(a[4]) #IndexError

# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)
    
# f=open("foo.txt","w")
# try:
#     #무언가 수행한다.
# finally:
#     f.close()
     
# try:
#     4/0         # ZeroDivisionError
#     a=[1,2,3]
#     print(a[4]) #IndexError
# except ZeroDivisionError :
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱할 수 없습니다.")
    
# try:
#     4/0         # ZeroDivisionError
#     a=[1,2,3]
#     print(a[4]) #IndexError
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# try:
#     4/0         # ZeroDivisionError
#     a=[1,2,3]
#     print(a[4]) #IndexError
# except (ZeroDivisionError,IndexError) as e:
#     print(e)

# try:
#     f=open("나없는파일","r")
# except FileNotFoundError:
#     pass

# class Bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle(Bird): #Bird클래스가 부모클래스, Eagle가 자식클래스로서 상속관계
#     def fly(self): # 오버라이딩
#         print("very fast")

# eagle=Eagle() # java문법 = (Eagle eagle = new Eagle())
# eagle.fly()





class MyError(Exception):
    pass

def say_nick(nick):
        if nick == "바보":
            raise MyError()
        print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")
    
class MyError(Exception):
    def __str__(self):
         return "허용되지 않는 별명입니다."

def say_nick(nick):
        if nick == "바보":
            raise MyError()
        print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
