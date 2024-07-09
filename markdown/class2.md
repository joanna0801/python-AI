# 程式技巧筆記

## 比較運算

```python
print(1 == 1)  # 這是比較是否相等運算
print(1 != 1)  # 這是比較是否不相等運算
print(1 > 1)   # 這是比較是否大於運算
print(1 < 1)   # 這是比較是否小於運算
print(1 >= 1)  # 這是比較是否大於或等於運算
print(1 <= 1)  # 這是比較是否小於或等於運算
```

## 邏輯運算

```python
print(not True)       # 這是相反運算
print(not False)      # 這是相反運算

print(True and True)  # 這是全部要符合才是True
print(True and False) # 這是全部要符合才是True
print(False and True) # 這是全部要符合才是True
print(False and False) # 這是全部要符合才是True

print(True or True)   # 這是只要有其中一個符合就是True
print(True or False)  # 這是只要有其中一個符合就是True
print(False or True)  # 這是只要有其中一個符合就是True
print(False or False) # 這是只要有其中一個符合就是True
```

## 運算符號的優先順序

1. `()`
2. `**`
3. `/`, `//`, `%`
4. `+`, `-`
5. `<`, `>`, `<=`, `>=`, `==`, `!=`
6. `and`, `or`, `not`

## 條件判斷

```python
pwd = input("請輸入密碼: ")
if pwd == "123456":
    print("密碼正確")
elif pwd == "12345678":
    print("密碼正確")
else:
    print("密碼錯誤")
```
* `if`一定要開頭且只能有一個。
* 可以有無限多個`elif`，也可以沒有。
* 可以有一個`else`，也可以沒有。
* `elif`和`else`是選擇性的。

## Streamlit 基本應用

### 輸入與顯示數字

```python
import streamlit as st

number = st.number_input("請輸入一個數字", step=1)
st.markdown(f"您輸入的數字是：{number}")
```

### 分數評級

```python
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
```

### 按鈕元件

```python
st.title("按鈕元件練習")
st.button("點我", key="button1")
if st.button("點我", key="button2"):
    st.balloons()
```

## 迴圈

### 基本範例

```python
for i in range(10):  
    print(i)  # 從0到9的數字顯示
```

### 指定範圍的迴圈

```python
for i in range(2, 100):  
    print(i)  # 從2到99的數字顯示
```

### 指定步長的迴圈

```python
for i in range(2, 100, 2):  
    print(i)  # 從2到99的偶數顯示
```

### 反向迴圈

```python
for i in range(100, 3, -2):  
    print(i)  # 從100到4的偶數顯示
```

## Streamlit 進階應用

### 數字金字塔

```python
st.title("數字金字塔")
number = st.number_input("請輸入一個整數(1~9)", min_value=1, max_value=9)
st.markdown("數字金字塔")
for i in range(1, number + 1):
    st.markdown(str(i) * i)
```

### 箭頭金字塔

```python
st.title("箭頭金字塔")
number = st.number_input("請輸入一個整數", step=1, min_value=1)
arrow = ""
for i in range(1, number * 2, 2):
    arrow += " " * ((number * 2 - i) // 2) + "*" * i
    st.markdown(arrow)
```

## 列表操作

### 列表的建立與打印

```python
print([])  
print([1, 2, 3])  
print([1, 2, 3, "a", "b", "c"])  
print([1, 2, 3, ["a", "b", "c"]])  
```

### 列表元素的訪問

```python
L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(L[0])  # 打印第一個元素
print(L[1])  # 打印第二個元素
print(L[2])  # 打印第三個元素
```

### 使用迴圈遍歷列表

```python
for index in range(len(L)):
    print(L[index])  # 使用索引遍歷列表

for cow in L:
    print(cow)  # 直接遍歷列表元素
```

### 修改列表元素

```python
L[0] = "moo"  # 修改第一個元素的值
```