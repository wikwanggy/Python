#다음은 "text.txt"라는 파일에 "Life is too short"문자열을 저장한 후 다시 
#그 파일을 읽어서 출력하는 프로그램이다
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지않는다.
# 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해보자.
f1=open("test.txt","w")
f1.write("Life is too short")
f1.close()
f2=open("test.txt","r")
print(f2.read())
f2.close()

#사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해보자.
#(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한
# 내용을 추가해야한다.)
user_input=input("저장할 내용을 입력하세요 : ")
f=open("test.txt","a")
f.write(user_input)
f.write('\n')# 입력한 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()

#다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는
# 문자열을 "python"으로 바꾸어서 저장해보자.
#ㅣLife is too short
#  you need java
f=open("test.txt","r")
body=f.read() #test.txt 파일에 있는 내용 읽기 위해 읽기모드
f.close()   #test.txt 파일에 있는 내용 읽어서 body변수에 저장

body=body.replace("java","python") #body변수에 저장되어 있는 문자열 중에서java를 python으로 치환
f=open("test.txt","w") # 치환한 후 test.txt에 그 내용을 쓰기위해 쓰기모드
f.write(body) # 치환 한 후 test.txt에 그  내용을 쓰기 위해 쓰기
f.close()