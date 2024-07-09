import streamlit as st

number = st.number_input("請輸入一個數字", step=1)
st.markdown(f"您輸入的數字是：{number}")

st.title("練習")
s = st.number_input("分數", step=1, min_value=0, max_value=100)
if s >= 90:
    st.markdown("A")
elif s >= 80:
    st.markdown("B")
elif s >= 70:
    st.markdown("C")
elif s >= 60:
    st.markdown("D")
else:
    st.markdown("F")

st.title("按鈕元件練習")
st.button("點我", key="button1")
if st.button("點我", key="button2"):
    st.balloons()
