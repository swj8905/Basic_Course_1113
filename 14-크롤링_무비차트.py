from bs4 import BeautifulSoup
import urllib.request as req


# 서버로부터 HTML코드 받아오기
code = req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

# HTML코드 이쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 내가 원하는 요소 가져오기
# title = soup.select_one("strong.title")
title = soup.select("div.sect-movie-chart strong.title")

# 요소 내용 출력
# 복습용 영상 강의에도 .string으로 설명하지만,
# 그냥 .string 쓰지 말고, .text 써주세요. 그게 더 좋습니다.
# print(title.text) # .string : 요소의 내용 가져옴 / .text : .string보다 더 좋음.
for i in title:
    print(i.text)