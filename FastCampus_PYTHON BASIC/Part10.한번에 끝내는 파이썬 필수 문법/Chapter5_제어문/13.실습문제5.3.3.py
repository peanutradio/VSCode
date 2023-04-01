#  실습문제 5.3.3
# Lerning Koeran

# 한국어 리스트
lk = ['사랑해', '귀엽다', '고마워', '행복해']

print("Let's Learn Korean")
for word in lk:
    print(word)
    data = input()
    if data != word:
        break