import streamlit as st
import os
import json
import time


## 페이지 구성
st.set_page_config(
    page_title="포트폴리오",
    page_icon=":material/business_center:"
)

## 포트폴리오 파일 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SUB_DIR = "Data"
FILE_NAME = "portfolio.json"

PORTFOLIO_DIR = os.path.join(BASE_DIR, SUB_DIR, FILE_NAME)

def load_portfolio():
    '''
    포트폴리오 파일을 로딩하는 함수
    '''
    if os.path.exists(PORTFOLIO_DIR):
        with open(PORTFOLIO_DIR, "r") as file:
            return json.load(file)
    return []

def save_portfolio(data):
    '''
    포트폴리오 파일에 새 데이터를 쓰는 함수
    '''
    with open(PORTFOLIO_DIR, "w") as file:
        json.dump(data, file, indent=2)

portfolio = load_portfolio()

portfolio_list: list[dict] = portfolio["portfolio"]

st.header("📊 현재 포트폴리오")
if portfolio:
    st.table(portfolio)
    # TODO: 과제, 여기 데이터를 보기 예쁘게 바꾸기(차트 등 활용)

else:
    st.write("보유 종목이 없습니다")


st.sidebar.header("포트폴리오 추가하기")
new_stock_code = st.sidebar.text_input("추가 종목코드")
new_avg_price = st.sidebar.number_input("매수 평단가")
new_stock_amount = st.sidebar.number_input("보유 수량")

if st.sidebar.button("추가하기"):
    if not new_stock_code:
        st.toast("코드를 입력해주세요",icon=":material/warning:")
        time.sleep(2)
    elif not new_avg_price:
        st.toast("매수 평단가를 입력해주세요",icon=":material/warning:")
        time.sleep(2)
    elif not new_stock_amount:
        st.toast("보유수량을 입력해주세요",icon=":material/warning:")
        time.sleep(2)
    else:
        portfolio_list.append({
            "code": new_stock_code, 
            "avg_price": new_avg_price,
            "quantity": new_stock_amount
        })

        save_portfolio(portfolio)
    
    st.rerun()
