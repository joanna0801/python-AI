import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1")
col1.button("按鈕2")
with col1:
    st.markdown("這這是欄1")
    st.button("左邊按鈕")

with col2:
    st.markdown("這這是欄2")
    st.button("右邊按鈕")

cols = st.columns([1, 5, 1])
cols[0].button("按鈕1", key="1")
cols[1].button("按鈕2", key="2")
cols[2].button("按鈕3", key="3")

st.title("文字輸入框")
text = st.text_input("輸入文字")
st.markdown(f"您輸入的文字是{text}")


st.title("session_state")
ans = 1
st.markdown(f"#####{ans}")
if st.button("按鈕", key="btn"):  # 如果按鈕按下，網頁會重新載入
    ans += 1  # ans = ans + 1
st.markdown(
    f"#####{ans}"
)  # 這時候ans會是2, 不會變成3或以上, 因為按鈕按下後，網頁會重新載入ans會重新設定為1

if "ans" not in st.session_state:  # 如果session_state中沒有ans就建立一個
    st.session_stateans.ans = 1  # 建立一個ans的狀態變數, 初始值為1

if st.button(
    "sessino_state按鈕", key="session_stateans_button"
):  # 如果按鈕按下，網頁會重新載入
    st.session_state.ans += 1  # 將session_state中的ans加1, 這時候ans可以持續增加

st.markdown(f"#####{st.session_state.ans}")
