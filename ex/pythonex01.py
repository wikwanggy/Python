# 1. 홍길동씨의 과목별 점수는 다음과 같다. 

국어=80;
영어=75;
과학=55;

총합=국어+영어+과학;
# 홍길동씨의 평균 점수를 구해보자.
평균=총합/3
print(총합) 
print("홍길동의 평균",평균)
print("홍길동의 평균",(국어+영어+과학)/3)

# 2. 자연수의 13이 홀수 인지 짝수인지 판변해보자
num1=13
print(13%2)
# 짝수면 0 홀수면 1을 출력
if num1%2==0:
    print(num1,"짝수")
else : 
    print(num1,"홀수")

# 3. 홍길동씨의 주민등록변호는 881120-1xxxxxx이다.
#       숫자부분으로 나누어 아래와 출력해보자
# 4. 홍길동씨의 주민등록번호를 년월일과 성별을 알수있는


hgd="881120-1xxxxxx"

print("년월일 : %s" %hgd)

yyddmm=hgd[0:6]
gender=hgd[7:8]
print(hgd[0:6])
print("년월일 : {0}" .format(yyddmm))
print("년월일 : %s" %yyddmm)
print(hgd[7:8])
print("성별 : {0}" .format(gender))
print("성별 : %s" %gender)
