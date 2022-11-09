# 03-2. while문
treeHit = 0
while treeHit < 10 :
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무가 넘어갔습니다.")

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    Enter number : 
"""
number = 0
while number != 4:
    print(prompt)
    number = int(input())

4
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee-1
    print("남은 커피의 개수는 %d개입니다." %coffee)
    if coffee ==0:
        print("남은 커피가 없습니다. 판매를 중단합니다.")
        break

print(bool(0)) # False
print(bool(1)) # True
print(bool(2)) # True
print(bool(300)) #True

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
    
