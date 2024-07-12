import streamlit as st

st.title("數字金字塔")
number = st.number_input("請輸入一個整數(1~9)", min_value=1, max_value=9)
st.markdown("數字金字塔")
for i in range(1, number + 1):
    st.markdown(str(i) * i)

st.title("箭頭金字塔")
number = st.number_input(
    "請輸入一個整數",
    step=1,
    min_value=1,
)
arrow = ""
for i in range(1, number * 2, 2):
    arrow += " " * ((number * 2 - i) // 2 + "*" * i)


if x > 5:
    x = 20
