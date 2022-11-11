# 정규 표현식 살펴보기

# data="""
# park 800905-1049118
# kim 700905-1059119
# """

# result=[]
# for line in data.split("\n"):
#     word_result=[]
#     for word in line.split(" "): # 공백 문자마다 나누기
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit:
#             word = word[:6]+ "-" + "********"
#         word_result.append(word)
#     result.append(" ".join(word_result)) #나뉜 단어 조립하기
#     print("\n".join(result))

import re #정규 표현식을 사용하기 위한 re모듈

data="""
park 800905-1049118
kim 700905-1059119
"""
pat=re.compile("(\d{6})[-]\d{7}") #\d는 숫자를 판별
print(pat.sub("\g<1>-*******",data)) #\g=그룹만들기, \g<1>는 그룹만들어서 1번그룹으로 지정  
