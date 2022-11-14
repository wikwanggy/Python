# 강력한 정규식의 세계로
import re

p=re.compile("Crow|Servo") # Crow라는 단어 또는 Servo라는 단어
m=p.match("CrowHello")
print(m) # <re.Match object; span=(0, 4), match='Crow'>

p=re.search('^Life', 'Life is too short')
print(p) # <re.Match object; span=(0, 4), match='Life'>

p1=re.search('^Life', 'My Life')
print(p1) #None

p=re.search('short$', 'Life is too short')
print(p) #<re.Match object; span=(12, 17), match='short'>

p=re.search('short$', 'Life is too short, you need python')
print(p) # None


p=re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))

p=re.compile("^Life",re.MULTILINE)
p1=re.compile("\ALife",re.MULTILINE)

data="""Life is too short
Life! is too short
Life@ is too short
"""
print(p.findall(data)) # ['Life', 'Life', 'Life']
print(p1.findall(data)) # ['Life']

p=re.compile("short$",re.MULTILINE)
p1=re.compile("short\Z",re.MULTILINE)

data="""Life is too short
Life! is too short
Life@ is too short"""
print(p.findall(data)) # ['short', 'short', 'short']
print(p1.findall(data)) #[short]

p=re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))