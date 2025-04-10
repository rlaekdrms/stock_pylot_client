import streamlit as st
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SUB_DIR = "Data"
FILE_NAME = "favorites.json"

FAV_DIR = os.path.join(BASE_DIR, SUB_DIR, FILE_NAME)

st.set_page_config(
    page_title="즐겨찾기",
    page_icon=":material/star:"
)

st.sidebar.title("즐겨찾기")
st.sidebar.header("주식 목록")

with open(FAV_DIR,"r") as file: 
    favorites = json.load(file)
    st.write(favorites)