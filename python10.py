# 03-1. if문
money = True
if money :
    print("택시 타고 가기")
else :
    print("걸어 가기")

# 돈이 3000 이상 있거나 카드가 있다면 택시를 타고, 그렇지 않으면 걸어가라
money = 3000
card = True
if money >= 3000 or card :
    print("택시 타고 가기")
else :
    print("걸어 가기")

# x in s, x not in s
print(1 in [1,2,3]) # True
print(1 not in [1,2,3]) # False
# s가 튜플 자료형
print("a" in ("a","b","c")) # True
# s가 문자열 자료형
print("j" not in "python") # True

# 주머니에 돈이 있으면 택시를 타고, 그렇지 않으면 걸어 가라
pocket = ["paper","cellphone","money"]
if "money" in pocket :
    print("택시 타고 가기")
else :
    print("걸어 가기")
#for(int i=0;i<pocket.length;i++){
#     if('money' == pocket[i]){
#         sysout("택시 타고 가기")
#     }else{
#         sysout("걸어 가기")
#     }
# }

# 주머니에 돈이 있으면 가만히 있고, 그렇지 않으면 카드를 꺼내라
pocket = ["paper","cellphone","money"]
if "money" in pocket:
    pass
else:
    print("카드를 꺼낸다")

# 주머니에 돈이 있으면 택시를 타고,
# 주머니에 돈은 없지만 카드가 있으면 택시를 타고
# 둘 다 없으면 걸어 가기
pocket = ["paper", "cellphone"]
card = True
if "money" in pocket :
    print("택시 타고 가기")
elif card:
    print("택시 타고 가기")
else :
    print("걸어 가기")
# 택시 타고 가기

# 조건부 표현식
score = 70
if score >= 60:
    message="success"
else:
    message="failure"
print(message)

# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
message="success" if score >= 60 else "failure"
