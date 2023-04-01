#1. 파이썬 객체는 pickle로 저장하기

import pickle

data = {
    "목표1" : "매일 팔굽펴 펴기 100회", 
    "목표2" : "매일 코딩 공부 1시간"
    }

    file = open("/Users/chanhupark/Documents/CODING/VS Code/PYTHON BASIC/Chapter10/data.pickle","wb", encoding="utf8" )
    pickle.dump(data,file)
    file.close() 


# # 2. pickle 파일을 파이썬으로 가져오기
# file = open("/Users/chanhupark/Documents/CODING/VS Code/data.pickle", "rb")
# data = pickle.load(file)
# print(data)
# file.close