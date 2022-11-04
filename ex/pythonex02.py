from unittest import result



# 5번 문제는 replace를 사용하여 ":"를 "#"으로 교체
a="a:b:c:d"
b=a.replace(":","#")
print(b)
# 6번 문자는 sort를 써서 정렬 하지만 reverse에 값을 주어서 오름차순,내림차순으로 정렬
a=[1,2,3,4,5]
a.sort(reverse=False)
a.sort(reverse=True)

print(a)

# 7번 문제는 " "공백을 주고 .join으로 하나의 문장으로 연결
a=['Life','is','too','short']
result=" ".join(a)
print(result)
# 8번 문제는 tuple에 더하기를 써서 요소 추가해주기
a=(1,2,3)   
a=a+(4,)
print(a)
# 9번 문제는 일일이 하나하나 출력해보면 3번만 출력이 안된다
a=dict()

# a['name']='python'
# a[('a',)]='python'
# a[[1]]='python'
# a[250]='python'
print(a)

#10번 문제는 pop함수로 B라는 요소를 끄집어내면 된다
a={'A':90,'B':80,'C':70}
result=(a.pop('B'))
print(a)
print(result)