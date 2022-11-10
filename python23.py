#프로그래밍
# 구구단
# def GuGu(n): # n은 단
#     result=[] # 결과를 저장하는 list 자료형
#     result.append(n*1) # 단*1 ex)2단이면 2*1
#     result.append(n*2) # 단*2 ex)2단이면 2*2
#     result.append(n*3) # 단*3 ex)2단이면 2*3
#     result.append(n*4) # 단*4 ex)2단이면 2*4
#     result.append(n*5) # 단*5 ex)2단이면 2*5
#     result.append(n*6) # 단*6 ex)2단이면 2*6
#     result.append(n*7) # 단*7 ex)2단이면 2*7
#     result.append(n*8) # 단*8 ex)2단이면 2*8
#     result.append(n*9) # 단*9 ex)2단이면 2*9
#     return result
# print(GuGu(2))

# def GuGu(n):                 # n은 단
#     result=[]                # 결과를 저장하는 list 자료형
#     i=1                      #단*i (즉 곱하는 수를 저장하는 변수)
#     while i<10:              # i<10는 i>=10이 되기전에 반복문을 멈추어라.
#         result.append(n*i)   #결과를 저장하는 result에 n*i를 한것을 요소 추가
#         i=i+1                # 한번씩 진행될 때마다 i+1을 해라
#     return result            # result에 저장
# dan=int(input("2~9단 중 숫자를 입력해주세요. : "))
# print(GuGu(dan))

# 3과 5의 배수합하기
# n=1                                 #n=1로 설정
# result=0                            #result=0으로 설정
# while n < 1000:                     #n=1000보다 작다 즉 999까지 반복하라.
#     if n % 3 == 0 or n % 5 == 0:    # 만약에 n 나누기 3이 0이라면 or n 나누기 5가 0이라면 
#         result=result+n             # result에 저장후 1000이 되기 전까지 저장한거에 n을 계속 더하라
#     n=n+1                           # n은 while가 반복 될때마다 1씩 증가
# print(result)                       # result를 출력


# result=0                            #result=0으로 설정
# for n in range(1,1000):             #range는 1~1000까지이지만 마지막숫자는 1000보다 전이기에 999이다.
#     if n % 3 == 0 or n % 5 == 0:    # 만약에 n 나누기 3이 0이라면 or n 나누기 5가 0이라면 
#         result = result+n           # result에 저장후 1000이 되기 전까지 저장한거에 n을 계속 더하라
# print(result)                        # result를 출력

#게시판구현하기
# 총 페이지 수 = (총 건수 / 한페이지당 보여 줄 건수)+1
#       1      =     5     / 10 + 1 
#       2      =     15    / 10 + 1 
#       3      =     25    / 10 + 1 
#       4      =     30    / 10 + 1 

# def getTotalPage(m,n):      # m=총 건수, n=한페이지당 보여 줄 건수
#     if m % n == 0:          # 만약에 m을 n으로 나눴을 때 0이라면
#         return m // n       # 나누기에 소숫점 이하를 버리는 // 연산자
#     else:                   # 0이 아니라면
#         return m // n + 1   # 나누기에 소숫점 이하를 버리는 // 연산자 (n에 1을 더하라)
# print(getTotalPage(5,10))
# print(getTotalPage(15,10))
# print(getTotalPage(25,10))
# print(getTotalPage(30,10))


#간단한 메모장 만들기
# import sys

# option=sys.argv[1]
# memo=sys.argv[2]

# print(option)
# print(memo)


# if option == "-a":          #입력받은 문자열을 메모장에 쓰기
#     memo=sys.argv[2]        # 입력받은 문자열(Life is too short)
#     f=open("memo.txt","a")  # memo.txt에 입력받은 문자열 추가하기(a)
#     f.write(memo)           # 입력받은 문자열
#     f.write('\n')           # 줄 바꿈
#     f.close()               # 닫기
# elif option == "-v":        # 메모장에 내용조회하기
#     f=open("memo.txt")      # memo.txt open
#     memo=f.read()           # 오픈한 memo.text read
#     f.close 
#     print(memo)
    
# import sys
# src=sys.argv[1]             #탭 문자열이 포함된 원본파일
# dst=sys.argv[2]             #탭 문자열->빈 공백 4칸으로 치환된 수정파일

# f=open(src)                 #원본파일(a.txt)을 열어라.
# tab_content=f.read()        #원본파일(a.txt)의
# print(tab_content)
# f.close()

#탭 문자열이 포함된(tab_content)에서 탭(\t)을 빈문자열 4칸("    ")으로 치환(replace)
# space_content=tab_content.replace("\t","    ")
# space_content=tab_content.replace("\t"," "*4)
# f=open(dst,"w") # 수정파일에 내용 쓰기
# f.write(space_content) # 수정파일에 빈공백4칸으로 지환된 내용쓰기.
# f.close()

# 하위디렉터리 검색하기
import os
# search함수 선언
def search(dirname):
    try:
        # print(dirname)
        # dirname디렉터리 안에 파일들의 리스트를 filenames변수에 저장
        filenames=os.listdir(dirname)
        for filename in filenames: 
            full_name=os.path.join(dirname, filename)
            # splitext : 파일에는 파일명.확장자 형식으로 되어 있는데, 이를 파일명과 확장자를 구분해서 나눠줌
            ext=os.path.splitext(full_name)[-1]
            if os.path.isdir(full_name): #C:/ 밑에 폴더가 있으면(isdir)
                search(full_name) # 그 폴더도 다시 검색
            else:
                ext=os.path.splitext(full_name)[-1]
                if ext==".json":
                    print(full_name)
    except PermissionError: 
        pass
# search함수 호출
search("C:/")