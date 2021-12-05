import streamlit as st

st.text("안녕하세요.")
st.text("스트림릿 테스트")

st.write("이런 것도 됩니다.")
st.write("# 이런 것도 됩니다.")
st.write("## 이런 것도 됩니다.")
st.write("### 이런 것도 됩니다.")
st.write("#### 이런 것도 됩니다.")
st.write("##### 이런 것도 됩니다.")
st.write("###### 이런 것도 됩니다.")
st.write("> 이런 것도 됩니다.")
st.write(">> 이런 것도 됩니다.")
st.write(">>> 이런 것도 됩니다.")
st.write(">>>> 이런 것도 됩니다.")
st.write("-------")

st.write("https://www.naver.com")
st.write(["아이언맨", "헐크", "스파이더맨"])
st.write({"짜장면":5000, "짬뽕":6000})
st.write("1 + 1 = ", 2)

st.code("""
a = 1
if a == 1:
    print("OK")
else:
    print("NO!!")
""")


"# 안녕하세요"

"""
# 매직커맨드

|       |   국어   |   수학  |
|-------|:----------:|:---------:|
|철수   | 참잘했어요. | 참잘했어요|
|영희   | 분발하세요. | 분발하세요.|

https://www.naver.com

```python
print("Hello World")
```
"""