import os
import requests
from datetime import datetime

from Shared.utils import mean_average

import streamlit as st
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SUB_DIR = "Data"
FILE_NAME = "favorites.txt"

FAV_DIR = os.path.join(BASE_DIR, SUB_DIR, FILE_NAME)

st.set_page_config(
    page_title="즐겨찾기",
    page_icon=":material/star:"
)

st.sidebar.title("즐겨찾기")
st.sidebar.header("주식 목록")


    
favorites = []
with open(FAV_DIR,"r") as file: 
    try:
        favorites = [line.strip() for line in file if line.strip()]
    except Exception as e:
        st.write(e)

stock_end_date = datetime.now()
stock_start_date = datetime(stock_end_date.year, stock_end_date.month - 1, stock_end_date.day)

for favorite in favorites:
    if st.sidebar.button(favorite):
        url = "http://localhost:8000/query_stock/"

        headers = {
            "Content-Type":"application/json"
        }

        data = {
            "stock_code": favorite,
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


new_stock_id = st.sidebar.text_input("즐겨찾기 추가하기")

if st.sidebar.button("추가하기", type="primary"):
    favorites.append(new_stock_id)
    with open(FAV_DIR, "a") as file: 
        file.write(f"\n{new_stock_id}")