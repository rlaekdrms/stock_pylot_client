from datetime import datetime
import os
import json
import streamlit as st
import time

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SUB_DIR = "Data"
FILE_NAME = "trade_log.json"

TRADE_DIR = os.path.join(BASE_DIR, SUB_DIR, FILE_NAME)

def load_trades():
    '''
    trade_log 파일을 로딩하는 함수
    '''
    if os.path.exists(TRADE_DIR):
        with open(TRADE_DIR, "r") as file:
            return json.load(file)
    return []

def save_trades(data):
    '''
    trade_log 파일에 새 데이터를 쓰는 함수
    '''
    with open(TRADE_DIR, "w") as file:
        json.dump(data, file, indent=2)

trades = load_trades()

def record_trade(code,action,price,quantity):
    trades = load_trades()
    trades.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "code": code,
        "action": action,
        "price": price,
        "quantity": quantity
    })
    save_trades(trades)


action_type = st.sidebar.selectbox("거래형태",("buy","sell"))

new_stock_code = st.sidebar.text_input("주식 코드")
desired_price = st.sidebar.number_input("거래 희망가")
tra_quantity = st.sidebar.number_input("거래 수량")

if st.sidebar.button("매수하기" if action_type == "매수" else "매도하기"):
    if not new_stock_code:
        st.toast("코드를 입력해주세요",icon=":material/warning:")
        time.sleep(2)
    elif not desired_price:
        st.toast("거래희망가를 입력해주세요",icon=":material/warning:")
        time.sleep(2)
    elif not tra_quantity:
        st.toast("거래수량을 입력해주세요",icon=":material/warning:")
        time.sleep(2)
    else:
        record_trade(new_stock_code,action_type,desired_price,tra_quantity)
        st.toast("거래 성공",icon=":material/check:")

