from selenium import webdriver
from chromedriver_autoinstaller import install
import time

# time.sleep() 사용하지말고,
# implicitly_wait() 사용하다가
# 만약 실행했는데, 원하는 결과가 안나온다.
# --> 어떤 페이지로 이동을 시켰는데, 이동을 하기도 전에 에러가 난다.
# 이러면 implicitly_wait()가 제대로 동작하지 않은 것이므로
# 그 페이지 전환되는 그 시점에만 time.sleep() 문장을 추가해준다.

browser = webdriver.Chrome(install())
browser.implicitly_wait(3) # 최대 3초 기다리기 옵션을 설정해라.
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
# 로그인하기
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython") # 타이핑 치게하기
pw = browser.find_element_by_css_selector("input#pw")
pw.send_keys("1q2w3e!@#")
button = browser.find_element_by_css_selector("button.btn_login")
button.click()
