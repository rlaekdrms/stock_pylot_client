import streamlit as st
import requests

API_BASE = "http://localhost:8000"

st.title("👀 자동거래 감시기")

status_res = requests.get(f"{API_BASE}/watchdog/status")
status_data = status_res.json().get("status", [])
watching_codes = [item["code"] for item in status_data if item["watching"]]

print(watching_codes)
status_res = requests.get(f"{API_BASE}/watchdog/status")
status_data = status_res.json().get("status", [])

watching_codes = [item["code"] for item in status_data if item["watching"]]

if watching_codes:
    for code in watching_codes:
        st.markdown(f"✅ 감시 중: **{code}**")
else:
    st.markdown("🔴 현재 감시 중인 종목 없음")

st.divider()

st.subheader("📉 감시 중지")
if watching_codes:
    stop_code = st.selectbox("중지할 종목 선택", watching_codes)
    if st.button("감시 중지"):
        res = requests.post(f"{API_BASE}/watchdog/stop/" + stop_code)
        st.success(res.json())
else:
    st.info("감시 중인 종목이 없습니다.")