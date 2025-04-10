import streamlit as st
from data import mockup_request
import pandas as pd
from matplotlib import pyplot as plt
import requests


st.set_page_config(
    page_title="주식정보조회",
    page_icon="📈",
)

def mean_average(data, mean_width):
    new_array = []
    mean_width = int(mean_width)
    half_width = int(mean_width / 2)

    # 원래코드
    # for _ in range(half_width):
    #     new_array.append(0)

    for idx, _ in enumerate(data):
        if idx < half_width:
            # 원래코드: continue
            newValue = data[idx]
            new_array.append(newValue)
        elif idx > len(data) - (half_width + 1):
            # 원래코드: continue
            newValue = data[idx]
            new_array.append(newValue)
        else:
            newValue = sum(data[idx - half_width : idx + half_width + 1]) / mean_width
            new_array.append(newValue)

    # 원래코드
    # for _ in range(half_width):
    #     new_array.append(0)

    return new_array

st.title("주식정보조회")

## Sidebar Header
st.sidebar.header("User Input")

## Sidebar User Input


stock_code = st.sidebar.text_input("Code","000660")

stock_start_date = st.sidebar.date_input("Start Date") # 조회 시작 날짜 입력
stock_end_date = st.sidebar.date_input("End Date") # 조회 끝 날짜 입력기

# TODO: 밑 코드 이해하고, 코드리뷰하기
# left, middle, right = st.sidebar.columns(3)
left, right = st.sidebar.columns(2)

if right.button("조회", icon=":material/query_stats:", type="primary"):

    st.write(f"Stock Code: {stock_code}")

    st.write(f"stock start date: {stock_start_date}")
    st.write(f"stock end date: {stock_end_date}")

    # Mock-up Request 
    ## 디자인 목업: 회사 사이트 - 내용을 실제로 입력하지 않고, 디자인만 먼저
    ### 제목: 나는 제목이다, 내용: Lorem Ipsum Dolor
    ## 개발 목업(리퀘스트 목업)
    ### 원래 리퀘스트: 클라이언트 -> 서버로 요청 -> 서버가 지정된 프로세스를 처리 -> 프론트에 응답
    ### 목업 리퀘스트: 클라이언트 0> (가짜 서버로 요청) -> (가짜 응답) -> 사이트 먼저 만들기

    ## 가짜 응답 양식 지정 -> 데이터 만들고 -> 프론트에서 DF로 만들고 -> 사이트 완성
    # response = mockup_request(stock_code if stock_ticker_type_selector=="stock_code" else stock_ticker)
    url = "http://localhost:8000/query_stock/"

    headers = {
        "Content-Type":"application/json"
    }

    data = {
	    "stock_code": stock_code,
        "start_date": stock_start_date.strftime("%Y%m%d"),
        "end_date": stock_end_date.strftime("%Y%m%d")
    }
    
    print(stock_start_date)
    
    try:
        response = requests.post(url,headers=headers,json=data)
    except Exception as err:
        st.write(err)
      
    

    # if response["status_code"] == "200":
    # data = response["data"]
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
       

