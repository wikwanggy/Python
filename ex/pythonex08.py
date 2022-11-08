# 다음 결과를 예측해 보자
print(all([1,2,abs(-3)-3]))#False
print(chr(ord('a'))=='a')

#filter와 lamda를 사용하여 리스트[1,-2,3,-5,8,-3]음수를 제거해보자
print(list(filter(lambda a:a>0,[1,-2,3,-5,8,-3])))

#234라는 10진수의 16진수는 다음과 같이 구할수 있다
# hex(234)이번에는 반대로 문자열 0xea를 10진수로 변경햅좌