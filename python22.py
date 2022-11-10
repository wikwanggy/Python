# import sys

# print(sys.argv)

# import pickle

# f=open("test.txt","wb")
# data={1:"python",2:"you need"}
# pickle.dump(data,f) # data 딕셔너리 객체를 그대로 파일에 저장하는 기능
# f.close()

# f=open("test.txt","rb")
# data=pickle.load(f)
# print(data)

# import os
# print(os.environ) #내 시스템의 환경 변수 값을 알고 싶을때
# os.chdir("C:\\") #디렉터리 위치 변경하기
# print(os.getcwd()) # 디렉터리 위치 돌려받기 -> 현재 디렉터리 위치에 따라 결과가 다를 수 있음
# os.system("dir") # 시스템 명령어 호출하기
# f=os.popen("dir") # 실행한 시스템 명령어의 결괏값 돌려받기
# print(f.read()) # 읽어 들인 파일 객체의 내용을 보기 위해

# import shutil

# shutil.copy("test.txt","test1.txt")

# import glob
# print(glob.glob("D:/python/test.*"))

# import tempfile

# filename=tempfile.mkstemp
# print(filename)

# f=tempfile.TemporaryFile()
# print(f)
# f.close

# # import time
# #  #UTC를 사용하여 현재 시간을 실수 형태로 돌려주는 함수이다.
# # print(time.time())

# # #돌려준 실수 값을 사용해서 연도,월,일,시,분,초 ...의 형태로 바꾸어주는 함수이다.
# # print(time.localtime(time.time())) 

# # #반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
# # print(time.asctime(time.localtime(time.time()))) 

# # #간편하게 표시할 수 있다.asctime과 다른점은 ctime은 항상 현재 시간만 돌려준다는 점이다.
# # print(time.ctime()) 

# # # strftime 함수는 시간에 관계된것을 세밀하게 표현하는 여러가지 포맷 코드를 제공한다.
# # print(time.strftime("%x",time.localtime(time.time()))) 

# import calendar
# # 2015년도 그해 전체 달력을 볼수 있다.
# # print(calendar.calendar(2015))
# # 2015년도 12월 달력만 보여준다
# # print(calendar.prmonth(2015,12)) 
# # #2015년 12월 31일 그  해당하는 날의 요일정보를 돌려준다 월요일부터 일요일까지 1~6이다.
# # print(calendar.weekday(2015,12,31))
# # # 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다
# # print(calendar.monthrange(2015,12))

import random

# print(random.random())
# print(random.randint(1,10)) 
# print(random.randint(1,55))

# def random_pop(data):
#     number = random.randint(0,len(data)-1)
#     return data.pop(number)

# if __name__=="__main__": # public void static main(){}
#     data=[1,2,3,4,5]
#     while data:
#         print(random_pop(data))

import webbrowser

urL='https://www.google.com'
chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open(urL)
# webbrowser.open("http://www.google.com/")