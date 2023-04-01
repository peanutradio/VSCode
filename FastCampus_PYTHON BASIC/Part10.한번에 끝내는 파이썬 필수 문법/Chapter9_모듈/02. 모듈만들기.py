import pay_module

#모듈 불러오는 방법
# code>preference>setting> 오른쪽 버튼 클릭>해당폴더 주소 입력 
                #  >     "python.analysis.extraPaths": "/Users/chanhupark/Documents/Githhub/VSCode/FastCampus_PYTHON BASIC/Part10.한번에 끝내는 파이썬 필수 문법/Chapter9_모듈",

#변수 사용
print(pay_module.version)

# 함수 사용
pay_module.printAurthor()

# 클래스 사용
pay_info = pay_module.Pay("A102030", 13000, "2023-06-07" )
print(pay_info.get_pay_info())

# 해당 파일을 직접 실행했을 때만 실행된다. 
if __name__ == "__main__":   #모듈이 name과 동일할 경우 실행
    print("pay module 실행")