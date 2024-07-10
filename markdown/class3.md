## 程式技巧筆記

### 列表操作

```python
L = [3, 12, 7, 9, 5, 3, 3, 3, 2, 4]

L.append(8)  # 使用 `append` 方法在列表末尾添加元素
print(L)

c = L.count(3)  # 使用 `count` 方法計算元素在列表中出現的次數
for i in range(c):
    L.remove(3)  # 使用 `remove` 方法移除列表中的指定元素

print(L)

L.pop(0)  # 使用 `pop` 方法移除並返回列表中的指定位置元素
print(L)

L.sort()  # 使用 `sort` 方法對列表進行升序排序
print(L)
L.sort(reverse=True)  # 使用 `sort` 方法並設置 `reverse` 參數對列表進行降序排序
print(L)

print(L.index(5))  # 使用 `index` 方法獲取指定元素的索引位置
```

### `pop` 與 `remove` 的差別

- `pop` 是根據索引位置來刪除元素，並返回被刪除的元素。
- `remove` 是根據元素值來刪除第一個匹配的元素。

### Streamlit 應用程式

#### 基本布局

```python
import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 建立兩個欄位
col1.button("按鈕1")
col1.button("按鈕2")
with col1:
    st.markdown("這這是欄1")
    st.button("左邊按鈕")

with col2:
    st.markdown("這這是欄2")
    st.button("右邊按鈕")

cols = st.columns([1, 5, 1])  # 建立比例為 1:5:1 的三個欄位
cols[0].button("按鈕1", key="1")
cols[1].button("按鈕2", key="2")
cols[2].button("按鈕3", key="3")
```

#### 文字輸入框

```python
st.title("文字輸入框")
text = st.text_input("輸入文字")  # 建立文字輸入框
st.markdown(f"您輸入的文字是{text}")
```

#### 使用 `session_state`

```python
st.title("session_state")
ans = 1
st.markdown(f"#####{ans}")
if st.button("按鈕", key="btn"):  # 如果按鈕按下，網頁會重新載入
    ans += 1  # ans = ans + 1
st.markdown(f"#####{ans}")  # 這時候ans會是2, 不會變成3或以上, 因為按鈕按下後，網頁會重新載入ans會重新設定為1

if "ans" not in st.session_state:  # 如果session_state中沒有ans就建立一個
    st.session_state.ans = 1  # 建立一個ans的狀態變數, 初始值為1

if st.button("session_state按鈕", key="session_stateans_button"):  # 如果按鈕按下，網頁會重新載入
    st.session_state.ans += 1  # 將session_state中的ans加1, 這時候ans可以持續增加

st.markdown(f"#####{st.session_state.ans}")
```

#### 網頁重新載入

```python
import streamlit as st
import time

if st.button("重新整理", key="button1"):  # 如果按鈕按下，網頁會重新載入
    st.success("準備重新整理")  # 顯示綠色按鈕
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新載入網頁
```

#### 點餐機功能

```python
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
```