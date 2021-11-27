from selenium import webdriver
import time
from chromedriver_autoinstaller import install
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(install())
browser.implicitly_wait(6)
browser.get("https://www.youtube.com/watch?v=95ULYjyiFLQ")
time.sleep(5)
# 스크롤 내려주기
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN) # PAGE_DOWN : 스크롤을 살짝 내려줌. / END : 스크롤을 끝까지 내려줌.
time.sleep(5) # 댓글 생성 기다리기
comments = browser.find_elements_by_css_selector("#content-text")
idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("------- 크롤링 끝! ---------")
        break
    idx += 1
    if idx % 20 == 0:
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(4)  # 댓글 생성 기다리기
        comments = browser.find_elements_by_css_selector("#content-text")

