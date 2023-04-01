# 기본형
# 1. 정의하기
def printHello(): 
    print("hello")

# 2. 호출하기
printHello()

# 매개변수가 있는 함수
def sum(a,b):
    print(a+b)

sum(3,4)
sum("재은아", "사랑해")

# 3. 반환값이 있는 함수
import random
def getRandomNumber():
    number = random.randint(1,10)
    return number

print(getRandomNumber())


# 4. 매개변수와 반환값이 있는 함수
def add(a,b):
    result = a + b
    return result
print(add(5,6))
