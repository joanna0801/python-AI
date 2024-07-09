import streamlit as st

with st.expander("class1 程式筆記 "):
    st.markdown(
        """
# 註解筆記

```python
    # 這是多行註解
    '''
    這是多行註解
    '''

    # 單行註解方式
    print("hello")  # ctrl+? 可以單行註解
    print(123)  # 整數
    print(123.456)  # 浮點數
    print(True)  # 布林值
    print("hello")  # 字串
    print(True)  # 布林值
    print(False)  # 布林值
    print('"')  # 印出雙引號
    print("'")  # 印出單引號

    a = 10  # 把10存到變數a的空間, = 就是將右邊的值存到左邊的變數的空間
    print(a)  # 印出整數

    b = "hello"

    # 算術運算
    print(1 + 1)  # 加法計算
    print(1 - 1)  # 減法計算
    print(1 * 1)  # 乘法計算
    print(1 / 1)  # 除法計算
    print(1 // 1)  # 整數除法計算
    print(1 % 1)  # 取餘數
    print(1 ** 1)  # 指數

    # 符號的優先順序
    # 1.()
    # 2.**
    # 3./ // %
    # 4.+ -

    # 字串運算
    a = "hello"
    b = "world"
    print(a + b)  # 字串加法
    print(a + " " + b)  # 字串加法
    print(a * 3)  # 字串重複
    print(a + b * 3)  # 字串加法乘法
    print(a * 3 + "!")  # 字串乘法加法

    # 格式化字串
    print(f"hello {10}{True}")  # 在字串前加上f就可以在字串中使用變數, 變數會用{}包起來

    # 字串函數
    print(len("hello"))  # 字串長度
    print(int("123"))  # 字串轉整數
    # print(float("123.456"))  # 字串轉浮點數
    # print(str("123"))  # 字串轉布林值
    # print(bool(1))  # 整數轉字串

    # 使用input()函數
    print("input()可以在終端輸入資料")
    a = input("請輸入一段文字: ")  # 輸入整數
    print(f"input()輸入的值是{a}")  # 印出輸入的值
    print(f"input()輸入的型態是{type(a)}")  # 印出輸入的型態

    # 計算正方形的面積
    a = int(input("請輸入正方形的邊長: "))  # 輸入整數
    area = int(a) * int(a)  # 計算正方形的面積
    print(f"正方形的面積是{a * a}")  # 印出正方形的面積
```

        """
    )

with st.expander("class2 程式筆記 "):
    st.markdown(
        """
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
        """
    )
