# with 구문을 사용하면 자동으로 file close 해준다. 
with open("/Users/chanhupark/Documents/CODING/VS Code/PYTHON BASIC/Chapter10/data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)