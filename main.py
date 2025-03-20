import streamlit as st
from data import mockup_request
import pandas as pd
from matplotlib import pyplot as plt


st.title("주식정보조회")

## Sidebar Header
st.sidebar.header("User Input")

## Sidebar User Input

# ticker_type: 라디오 버튼
stock_ticker_type_selector = st.sidebar.radio("Ticker Type Selector",("stock_ticker","stock_code")) 

# "stock_ticker"를 stock_ticker_type_selector에 대입하고 있는 코드
# 목표: stock_ticker_type_selector 가 "stock_ticker"인지 물어봐야 함
# if stock_ticker_type_selector="stock_ticker":
if stock_ticker_type_selector == "stock_ticker":
    stock_ticker = st.sidebar.text_input("Ticker", "AAPL")
    st.write(f"Stock ticker: {stock_ticker}")
# else stock_ticker_type_selector="stock_code":
else:
    stock_code = st.sidebar.text_input("Code","000660")
    st.write(f"Stock code: {stock_code}")

stock_start_date = st.sidebar.date_input("Start Date") # 조회 시작 날짜 입력
stock_end_date = st.sidebar.date_input("End Date") # 조회 끝 날짜 입력기

## 본 페이지 내용

st.write(f"stock start date: {stock_start_date}")
st.write(f"stock end date: {stock_end_date}")

# Mock-up Request 
## 디자인 목업: 회사 사이트 - 내용을 실제로 입력하지 않고, 디자인만 먼저
### 제목: 나는 제목이다, 내용: Lorem Ipsum Dolor
## 개발 목업(리퀘스트 목업)
### 원래 리퀘스트: 클라이언트 -> 서버로 요청 -> 서버가 지정된 프로세스를 처리 -> 프론트에 응답
### 목업 리퀘스트: 클라이언트 0> (가짜 서버로 요청) -> (가짜 응답) -> 사이트 먼저 만들기

## 가짜 응답 양식 지정 -> 데이터 만들고 -> 프론트에서 DF로 만들고 -> 사이트 완성
response = mockup_request()

def mean_average(data, mean_width):
    new_array = []
    mean_width = int(mean_width)
    half_width = int(mean_width / 2)

    for _ in range(half_width):
        new_array.append(0)

    for idx, _ in enumerate(data):
        if idx < half_width:
            continue
        elif idx > len(data) - (half_width + 1):
            continue
        else:
            newValue = sum(data[idx - half_width : idx + half_width + 1]) / mean_width
            new_array.append(newValue)

    for _ in range(half_width):
        new_array.append(0)

    return new_array

df = pd.DataFrame(response)

df_ma15 = mean_average(df['value'], 15)
df_ma30 = mean_average(df['value'], 30)

df['ma15'] = df_ma15
df['ma30'] = df_ma30

st.dataframe(df, hide_index=True)
st.line_chart(df, x='date', y=[ 'ma15', 'ma30', 'value',])


