# 그루핑 Grouping
import re
p=re.compile("(ABC)+")
m=p.search("ABCABCABC OK?") 
print(m) # <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group(0)) # ABCABCABC
print(m.group(1)) # ABC

p=re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m=p.search("park 010-1234-1234")
print(m) # <re.Match object; span=(0, 18), match='park 010-1234-1234'>

p=re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m=p.search("park 010-1234-1234")
print(m.group(1))  # park
print(m.group(2)) #  010-1234-1234
print(m.group(3)) # 010
# 그루핑된 문자열 재참조 하기
p=re.compile(r'(\b\w+)\s+\1')
m=p.search("Paris in the the spring").group()
print(m) # the the
# 그루핑된 문자열에 이름 붙이기
p=re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m=p.search("park 010-1234-1234")
print(m.group("name"))
# 정규식 안에서 재참조
p=re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
m=p.search("Paris in the the spring").group()
print(m)
# 전방탐색
p=re.compile(".+:")
m=p.search("http://google.com")
print(m.group())
#긍정형 전방 탐색
p=re.compile(".+(?=:)")
m=p.search("http://google.com")
print(m.group())
# 문자열 바꾸기
p=re.compile("(blue|white|red)")
print(p.sub("color","blue socks and red socks"))
print(p.subn("color","blue socks and red socks"))
# 문자열 바꾸기
p=re.compile("(blue|white|red)")
print(p.sub("color","blue socks and red socks", count=1))
print(p.subn("color","blue socks and red socks", count=1))
# sub 메서드를 사용할 때 참조구문 사용하기
p=re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
m=p.sub("\g<phone>\g<name>","park 010-1234-1234")
print(m)
# sub 메서드를 사용할 때 참조구문 사용하기
p=re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
m=p.sub("\g<2>\g<1>","park 010-1234-1234")
print(m)

# sub 메서드의 매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value)
p= re.compile(r'\d+')
m=p.sub(hexrepl, "Call 65490 for printing, 49152 for user code.")
print(m)

#Greedy
s='<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>',s).span())
print(re.match('<.*>',s).group())

#Non-Greedy
s='<html><head><title>Title</title>'

print(re.match('<.*?>',s).group())