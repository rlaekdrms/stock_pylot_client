import streamlit as st
import os
import json
import time
from collections import defaultdict
import matplotlib.pyplot as plt


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

def aggregate_portfolio(portfolio_list):
    aggregated = defaultdict(lambda:{"total_quantity":0,"total_cost":0})

    for item in portfolio_list:
        code = item["code"]
        qty = item["quantity"]
        avg_price = item["avg_price"]
        aggregated[code]["total_quantity"] += qty
        aggregated[code]["total_cost"] += qty * avg_price

    result = []     
    for code, data in aggregated.items():
        total_qty = data["total_quantity"]
        total_cost = data["total_cost"]
        result.append(
            {
                "code":code,
                "avg_price":round(total_cost/total_qty,2),
                "quantity":total_qty,
            }
        )
    return result

st.subheader("📊 포트폴리오 요약")
aggregated_portfolio = aggregate_portfolio(portfolio_list)

if aggregated_portfolio:
    col1, col2 = st.columns([2,3])
    with col1:
        labels = [item["code"]for item in aggregated_portfolio]
        sizes = [item["quantity"]for item in aggregated_portfolio]

        fig, ax = plt.subplots()
        
        wedges, text, autotexts = ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops=dict(width=0.4),
        )
        
        ax.axis("equal")
        st.pyplot(fig)

