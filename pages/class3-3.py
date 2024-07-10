import streamlit as st
import time

if st.button("重新整理", key="button1"):  # 如果按鈕按下，網頁會重新載入
    st.success("準備重新整理")  # 顯示綠色按鈕
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新載入網頁

st.title("點餐機")

if "order" not in st.session_state:
    st.session_state.order = []  # 新增購物車list

col1, col2 = st.columns(2)  # 2欄
with col1:
    foodInput = st.text_input("請輸入餐點")  # 建立文字輸入框

with col2:
    if st.button("加入", key="add"):  # 如果按鈕被按下
        st.session_state.order.append(foodInput)  # 把餐點加入購物車

st.write(f"### 購物籃")  # 寫入標題
for i in range(len(st.session_state.order)):  # 用index來取得購物車中的餐點
    col1, col2 = st.columns(2)  # 2欄
    with col1:
        st.write(st.session_state.order[i])  # 寫入餐點
    with col2:
        if st.button("刪除", key=i):  # 如果按鈕被按下
            st.session_state.order.pop(i)  # 刪除購物車中的餐點
            st.rerun()  # 重新載入網頁
