from selenium import webdriver
from chromedriver_autoinstaller import install
import time

# 헤드리스 모드 #
opt = webdriver.ChromeOptions()
opt.add_argument("headless")
browser = webdriver.Chrome(install(), options=opt)
browser.implicitly_wait(3) # 최대 3초 기다리기 옵션을 설정해라.
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
# 로그인하기
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython") # 타이핑 치게하기
pw = browser.find_element_by_css_selector("input#inputPwd")
pw.send_keys("q1w2e3!@#")
button = browser.find_element_by_css_selector("button#loginBtn")
button.click() # 버튼 클릭하게 하기
time.sleep(3) # 로그인 다 될 때까지 기다리기
# 이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2) # 웹페이지 다 뜰 때까지 기다리기
# 이메일 제목들 크롤링
title = browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text)
browser.close()