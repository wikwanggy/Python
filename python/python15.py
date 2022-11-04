# 파일 읽고 쓰기
# 1. 파일 생성하기
#f=open("새파일.txt","w")

#f.close()
# 2. 파일 내용 쓰기(python->파일로 글을 쓴다)
#f=open("D:/python/새파일.txt","w")
#for i in range(1,11):
#    data="%d번째 줄입니다.\n" %i
#    f.write(data) # data변수에 있는 내용을 파일에 써라
#f.close()

# 3. 파일의 저장된 내용을 python으로 읽어들이는  방법
# 3-1 readline함수
#f=open("D:/python/새파일.txt","r")
#line=f.readline()
#print(line)
#f.close()
# 모든 줄을 읽어서 화면에 출력하고 싶다면
#f=open("D:/python/새파일.txt","r")
#while True: # 무한 루프
#    line=f.readline()
#    if not line: # line 변수에 아무것도 없으면
#       break #반목문 취소
#    print(line)
#f.close()
# 3-2 readlines함수
#f=open("D:/python/새파일.txt","r")
#lines=f.readlines()
#for line in lines: 
#    print(line)
#f.close()
# 3-3 read 함수
#f=open("D:/python/새파일.txt","r")
#data=f.read()
#print(data)
#f.close()

# 4. 파일에 기존내용 그래도 놔두고, 새로운 내용 추가하기
f=open("새파일.txt","a")
for i in range(11,21):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close(0)