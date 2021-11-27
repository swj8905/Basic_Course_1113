from selenium import webdriver
import time
from chromedriver_autoinstaller import install

browser = webdriver.Chrome(install())
browser.implicitly_wait(5)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
browser.get("http://cafe.daum.net/talingpython")
# 중고나라 게시판 클릭
time.sleep(2)
browser.switch_to.frame("down")
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()

try:
    f = open("./중고나라.txt", "r")
    ref = f.readlines()
except: # 위 문장에서 에러가 난다는 것은, 파일이 존재하지 않는다는 뜻!
    f = open("./중고나라.txt", "w")
    ref = []
f.close()

title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if (i.text+"\n") not in ref: # 최신에 올라온 글이라면?
        f = open("./중고나라.txt", "a") # "a"모드 : 더해서 쓰기모드
        f.write(i.text + "\n")
        f.close()
        if "선풍기" in i.text:
            new_one += 1
print(f"선풍기 관련 글이 {new_one}개 올라왔습니다.")
browser.close()