# 파일 열기 모드
# "r" 모드 : 읽기모드
# - 파일이 존재하지 않을 때 에러!
f = open("./test.txt", "r", encoding="utf-8")
# result = f.read()
# result = f.readline()
result = f.readlines()
f.close()
print(result)