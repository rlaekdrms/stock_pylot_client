import requests
from Shared.utils import mean_average
import os
import json

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="주식정보조회",
    page_icon="📈",
)


st.title("주식정보조회")

## Sidebar Header
st.sidebar.header("User Input")

stock_code = st.sidebar.text_input("Code","000660")
stock_start_date = st.sidebar.date_input("Start Date") # 조회 시작 날짜 입력
stock_end_date = st.sidebar.date_input("End Date") # 조회 끝 날짜 입력기

if st.sidebar.button("조회", icon=":material/query_stats:", type="primary"):
    st.write(f"Stock Code: {stock_code}")
    st.write(f"stock start date: {stock_start_date}")
    st.write(f"stock end date: {stock_end_date}")

    url = "http://localhost:8000/query_stock/"

    headers = {
        "Content-Type":"application/json"
    }

    data = {
	    "stock_code": stock_code,
        "start_date": stock_start_date.strftime("%Y%m%d"),
        "end_date": stock_end_date.strftime("%Y%m%d")
    }
    
    # 서버에 주가 정보 요청 Try
    try:
        response = requests.post(url,headers=headers,json=data)
    except Exception as err:
        # 요청이 제대로 안 됨(에러)
        st.write(err)

    # Data를 받아서 그리기
    try:    
        data = response.json()

        print(data)

        df = pd.DataFrame(data)


        df_ma15 = mean_average(df['values'], 15)
        df_ma30 = mean_average(df['values'], 30)

        df['ma15'] = df_ma15
        df['ma30'] = df_ma30

        st.dataframe(df, hide_index=True)
        st.line_chart(df, x='dates', y=[ 'ma15', 'ma30', 'values',])
    except Exception as err:
        st.write("주식정보를 조회하는데 실패했습니다")

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    SUB_DIR = "Data"
    FILE_NAME = "favorites.txt"

    FAV_DIR = os.path.join(BASE_DIR, SUB_DIR, FILE_NAME)
