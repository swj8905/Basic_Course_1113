from selenium import webdriver
from chromedriver_autoinstaller import install
import time

hash_tag = input("해시태그 입력 >> ")

browser = webdriver.Chrome(install())
browser.implicitly_wait(7)
# 로그인하기
browser.get("https://www.instagram.com/accounts/login/")
id = browser.find_element_by_name("username")
id.send_keys("tutor_pyson")
pw = browser.find_element_by_name("password")
pw.send_keys("q1w2e3r4!@#$")
button = browser.find_element_by_css_selector("div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB")
button.click()
time.sleep(5)
# 해시태그 검색
url = "https://www.instagram.com/explore/tags/" + hash_tag
browser.get(url)
# 첫번째 게시물 클릭
first_photo = browser.find_element_by_css_selector("div._9AhH0")
first_photo.click()
while True:
    like = browser.find_element_by_css_selector("section.ltpMr.Slqrh span > svg._8-yf5")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("div.l8mY4.feth3 svg._8-yf5")
    if value == "좋아요":
        like.click()
        time.sleep(30)
        next.click()
        time.sleep(30)
    elif value == "좋아요 취소":
        next.click()
        time.sleep(30)