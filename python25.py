# 정규 표현식
import re
p=re.compile('[a-z]+')

#match
# m1=p.match("python")
# print(m1)

# m=p.match("3 python")
# print(m)

# 작성 법   
# p=re.compile(정규 표현식)
# m=p.match("조사할 문자열")
# if m:
#     print('Match found : ',m.group())
# else:
#     print('No match')

# m=p.search("python")
# print(m)

# m1=p.search("3 python")
# print(m1)
 
# result=p.findall("life is too short")
# print(result)



# import re

# p=re.compile("[a-z]+")
# m=p.match("python")
# s=p.search("3 python")

# print(m.group()) # 매칭된 문자열을 돌려줌
# print(m.start()) # 매칭된 문지열의 시작 위치
# print(m.end()) # 매칭된 문자열의 끝 위치
# print(m.span()) #매칭된 문자열의 시작위치와 끝위치를 튜플형태(시작위치, 끝위치)로 돌려줌


# print(s.group()) # 매칭된 문자열을 돌려줌
# print(s.start()) # 매칭된 문지열의 시작 위치
# print(s.end()) # 매칭된 문자열의 끝 위치
# print(s.span()) #매칭된 문자열의 시작위치와 끝위치를 튜플형태(시작위치, 끝위치)로 돌려줌

import re
# p=re.compile("a.b") # a로 시작하고 b로 끝나는 문자(중간에는 어떠한 문자가 들어가도 됨)
# print(p.match("a0b")) #<re.Match object; span=(0,3), match="a0b">
# print(p.match("a\nb")) #none

# p1=re.compile("a.b", re.DOTALL) # a로 시작하고 b로 끝나는 문자(중간에는 어떠한 문자가 들어가도 됨)
# print(p1.match("a0b")) #<re.Match object; span=(0,3), match="a0b">
# print(p1.match("a\nb")) #none

# p=re.compile("[a-z]")
# print(p.match("python")) #<re.Match object; span=(0, 1), match='p'>
# print(p.match("Python")) #None
# print(p.match("Python")) #None

# p=re.compile("[a-z]",re.IGNORECASE)
# print(p.match("python")) #<re.Match object; span=(0, 1), match='p'>
# print(p.match("Python")) #<re.Match object; span=(0, 1), match='p'>
# print(p.match("Python")) #<re.Match object; span=(0, 1), match='p'>

# p=re.compile("^python\s\w+") # ^python인 경우 문자열의 처음은 항상 python으로 시작해야 매치된다.

# data="""python one
# Life is too short
# python two
# you need python
# python three"""

# print(p.findall(data))

# p1=re.compile("^python\s\w+",re.MULTILINE) # re.MULTILINE 옵션으로 이해^메타 문자가 문자열 전체가 아닌 각 줄의 처음이라는 의미를 갖게되었다.

# data1="""python one
# Life is too short
# python two
# you need python
# python three"""

# print(p1.findall(data1))

# charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-f]+)')

# charref = re.compile(r"""
#  &[#]            # Star of a numeric entity reference
# (
# 0[0-7]+          #0ctal form (8진수 정규식)
# | [0-9]+         # Decimal form(10진수 정규식)
# | x[0-9a-fA-f]+  #Hexadecimal(16진수 정규식)
# )
#  ;
# """,re.VERBOSE)  # Trailing semicolon

# print(charref)

# 백슬래시(\)section 정규식 형태의 식을 만들고 싶다면
# p=re.compile("\section")  #\s 정규식의 ection [\t\n\r\f\v]ection로 오인
# 의도한 대로 매치하고 싶다면
# p=re.compile("\\section")
# 정규식 문자열 앞에 r문자르 삽입하면 이 정규식은 Raw string 규칙에 의하여 
# 백슬래스 2개 대신 1개만 써도 2개를 쓴것과 동일한 의미를 갖게된다.
# p=re.compile(r"\secion")  