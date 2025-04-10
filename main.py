import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("Stock Pylot")

st.header("주식정보조회")
st.write("주식정보조회를 이용한 차트 분석")
st.write("sidebar로 이동하여 사용하시오")
# 예시
# st.header("_Streamlit_ is :blue[cool] :sunglasses:")
# st.header("This is a header with a divider", divider="gray")
# st.header("These headers have rotating dividers", divider=True)
# st.header("One", divider=True)
# st.header("Two", divider=True)
# st.header("Three", divider=True)
# st.header("Four", divider=True)

st.sidebar.header("Menu")


st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )
