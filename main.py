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

# TODO 1. 데이터를 DataFrame(판다스)으로 바꾸기

## Hint
    # df2 = pd.DataFrame(data)
    # print(df2)
def Stock_date(data)
    columns = ["dates","values"]
    df = pd.DataFrame(columns=columns)

# TODO 2. 바꾼 DataFrame으로 그래프 그리기
    for row in data['output2']:
        dateText = f"{row['stck_bsop_date'][2:4]}/{row['stck_bsop_date'][4:6]}/{row['stck_bsop_date'][6:8]}"
        new_row =  pd.DataFrame([{"dates":dateText,"values":int(row['stck_clpr'])}])
        df = pd.concat([df,new_row],ignore_index=True)

        fig, ax = plt.subplots()
        df_sorted = df.sort_values("dates")

        df_smoothed1 = mean_average(df_sorted["values"], 5)
        df_smoothed2 = mean_average(df_sorted["values"], 15)
        df_smoothed3 = mean_average(df_sorted["values"], 30)

        ax.plot(df_sorted["dates"], df_sorted["values"])
        ax.plot(df_smoothed1, "orange")
        ax.plot(df_smoothed2, "red")
        ax.plot(df_smoothed3, "green")
        ax.legend(["Original", "Smoothed1", "Smoothed2", "Smoothed3"])

        ax.set_xlabel("Date")

        ax.tick_params(axis='x', labelrotation=45)

        fig.savefig(f"{data['output1']['stck_shrn_iscd']}_result.png")

        
        print(df)
        return df



