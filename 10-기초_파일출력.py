# 파일 열기 모드
# "w" 모드 : 쓰기 모드
# - 파일이 존재하지 않을 때, 파일 자동 생성
# - 파일을 열 때, 모든 내용을 지움.
# "a" 모드 : 더해서 쓰기 모드
# - 파일이 존재하지 않을 때, 파일 자동 생성
# - 파일을 열 때, 모든 내용을 유지함.
f = open("./test.txt", "w")
f.write("Hello\n")
f.write("World\n")
f.write("Python")
f.close()