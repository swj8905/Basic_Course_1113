import urllib.request as req
from bs4 import BeautifulSoup
import streamlit as st

st.write("# 무비차트")
code = req.urlopen("http://www.cgv.co.kr/movies/")
soup = BeautifulSoup(code, "html.parser")
title = soup.select("div.sect-movie-chart strong.title")
img = soup.select("div.sect-movie-chart span.thumb-image > img")
for i in range(len(title)):
    st.write(f"**{i+1}위.** {title[i].text}")
    st.image(img[i].attrs["src"], width=200)