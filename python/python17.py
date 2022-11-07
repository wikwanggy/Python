# mod1.py 파일 불러오기
# import 모듈명
#import mod1
# from 모듈명 import 모듈 함수
# from mod1 import add
# from mod1 import sub
# from 모듈명 import 모듈 함수 2번째 방법
# from mod1 import add,sub # 콤마로 구분하여 필요한 함수를 불러올 수 있다.
# from 모듈명 import 모듈 함수 3번째 방법
# *은 모든것이라는 뜻으로 모든 함수를 불러서 사용하겠다는 뜻이다.
# from mod1 import * 
# mod1.py파일에 있는 add함수와
# sub함수를 호출
# print(add(1,2))
# print(sub(1,2))

#mod2.py 불러오기
import mod2

result1=mod2.add(3,4)
result2=mod2.Math.solv(2)

print(result1)
print(result2)