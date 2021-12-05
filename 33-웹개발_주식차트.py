import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import datetime

st.write("# 주식차트")

# ticker = "GOOGL"
ticker = st.text_input("티커 입력")
data = yf.Ticker(ticker)
today = datetime.datetime.today().strftime("%Y-%m-%d")
df = data.history(period="1d", start="2015-1-1", end=today)
st.dataframe(df)

st.write("## 주가차트 - 종가 기준")
st.line_chart(df["Close"])

st.write("## 주가차트 - 캔들 차트")
candle = go.Candlestick(x=df.index, open=df["Open"], close=df["Close"],
               high=df["High"], low=df["Low"])
layout = go.Layout(yaxis={"fixedrange":False})
fig = go.Figure(data=[candle], layout=layout)
st.plotly_chart(fig)

st.write("## 거래량 차트")
st.bar_chart(df["Volume"])