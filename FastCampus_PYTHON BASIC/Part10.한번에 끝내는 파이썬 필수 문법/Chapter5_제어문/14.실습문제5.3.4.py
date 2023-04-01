#  실습문제 5.3.4
# Lerning Koeran ver 2.0

# 한국어 리스트
# lk = ['사랑해', '귀엽다', '고마워', '행복해']

# #점수
# score = 0

# print("Let's Learn Korean")
# for word in lk:
#     print(word)
#     data = input()
#     if data == word: # 문제를 맞힌 경우
#         score +=1    # 점수를 1 증가

# print("전체 문제 개수: ", len(lk))
# print("맞힌 개수 : ", score)
# print("틀린 개수 : ", len(lk)-score)

#=================================#
#리스트를 만들고
lk = ['사랑해', '고마워', '귀엽다', '행복해']

# 담아줄 score 그릇
score = 0

#프린트 영어를 시작합시다. 
print("let's learn english")

#for문 - word에 lk 입력
for word in lk:
    print(word)
    data = input()
    if data == word:
        score += 1

print("전체문제 개수: ", len(lk))
print("맞힌 개수: ", score)
print("틀린 개수: ", len(lk)-score)