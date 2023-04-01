# while 
# 보통 반복 횟수가 정해지지 않았을 때 사용한다. 

# i = 0          # 초기식
# while i < 10:  # 조건식
#     print(i, " 번째 다짐, 나는 할 수 있다.")
#     i += 1     # 증강식 

# i = 5          # 초기식
# while i < 9:  # 조건식
#     print(i, " 번째 다짐, 나는 할 수 있다.")
#     i += 1     # 증강식 


i = 0          # 초기식
while i < 10:  # 조건식
    print(i, " 번째 다짐, 나는 할 수 있다.")
    i += 2     # 증강식 


# 무한 루프
#  : 조건식에 True를 넣어서 항상 반복되게 만드는 것.

while True: 
    x = input("종료하려면 exit을 입력하세요>>>")
    if x == "exit":
        break
print("종료")