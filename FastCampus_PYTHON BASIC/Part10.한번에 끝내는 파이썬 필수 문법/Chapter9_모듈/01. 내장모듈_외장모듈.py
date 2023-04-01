# 모듈: 한개의 완성된 프로그램 파일.
#      ** 다른 파일에서 내 파일을 참조하게 하는 방법 **

# import 모듈이름
# 모듈이름.변수
# 모듈이름.함수()

# 내장모듈: 파이썬 설치시 자동으로설치되는 모듈

# import math
# print(math.pi)
# print(math.ceil(2.7))

# 외부모듈: 다른 사람들이 만든 파이썬 피일을 pip로 설치해서 사용

# pyautogui 모듈 설치
# 터미널에 입력 : pip install pyautogui

import pyautogui as pg
pg.moveTo(500, 500,duration=2)

# Command+shift+p  > Python: select interpreter

