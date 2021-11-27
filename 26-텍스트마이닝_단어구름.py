from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

keyword = input("키워드 입력 >> ")
encoded = par.quote(keyword) # 한글 -> 특수한 문자

page_num = 1
output_total = ""
while True:
    url = f"https://www.joongang.co.kr/_CP/496?keyword={encoded}&sort%20=&pageItemId=439&page={page_num}"
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline a")
    if len(title) == 0: # 끝 페이지까지 크롤링 완료했으면?
        break
    for i in title:
        print("제목 :", i.text.strip())
        print("링크 :", i.attrs["href"])
        code_news = req.urlopen(i.attrs["href"])
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div#article_body")
        result = content.text.strip().replace("     ", " ").replace("   ", "")
        output_total += result
        print(result)
        print()
    if page_num == 2:
        break
    page_num += 1
print("-----------------------------------")
# 명사들만 추출
from konlpy.tag import Okt
print("[알림] 형태소 분석 중.. 명사들만 추출합니다.")
okt = Okt()
nouns_result = okt.nouns(output_total)
# print(nouns_result)

# 불용어 제거
nouns_without_stopwords = []
for i in nouns_result:
    if len(i) != 1: # != : 양쪽값이 다르다면?
        nouns_without_stopwords.append(i)

# 단어 출현 빈도수 카운트
from collections import Counter
print("[알림] 명사들의 출현 빈도수를 카운트합니다.")
count_result = Counter(nouns_without_stopwords)
# print(count_result)

# 원하는 이미지 불러옴.
from PIL import Image
import numpy as np
image_data = np.array(Image.open("./image.jpg"))

# 그 이미지의 색깔 추출하기
from wordcloud import ImageColorGenerator
image_color = ImageColorGenerator(image_data)

# 단어구름 만들기
from wordcloud import WordCloud
print("[알림] 단어구름을 생성합니다.")
wc = WordCloud(mask=image_data, font_path="./NanumMyeongjoBold.ttf", background_color="white").generate_from_frequencies(count_result)

# 이미지 화면에 띄우기
import matplotlib.pyplot as plt

plt.figure() # 창을 만듦
# plt.imshow(wc.recolor(color_func=image_color), interpolation="bilinear") # 창에 이미지를 띄움
plt.imshow(wc, interpolation="bilinear") # 창에 이미지를 띄움
plt.axis("off") # 쓸데없이 뜨는 가로축, 세로축을 없앰.
plt.show() # 화면에 그 창을 띄움