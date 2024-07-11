# 程式技巧筆記

## 迴圈

### while 迴圈
```python
i = 0
while i < 10:  # 當 i < 10 時執行迴圈
    print(i)
    i += 1  # i = i + 1
```

### for 迴圈
```python
for i in range(1, 6):  # 產生從 1 到 5 的數字
    print(i)
    if i == 3:
        break  # 當 i == 3 時，跳出迴圈
```

### break 跳出迴圈
```python
i = 1
while i < 6:  # 當 i < 6 時執行迴圈
    print(i)
    i += 1
    if i == 3:
        break  # 當 i == 3 時，跳出迴圈
```

## 算術運算與賦值
```python
a = 10
a += 1  # 等同於 a = a + 1
a -= 1  # 等同於 a = a - 1
a *= 2  # 等同於 a = a * 2
a /= 2  # 等同於 a = a / 2
a %= 2  # 等同於 a = a % 2
a **= 2  # 等同於 a = a ** 2
```

## 運算符優先順序
1. `()`
2. `**`
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. `<`, `>`, `<=`, `>=`, `==`, `!=`
6. `and`, `or`, `not`

## 隨機數
```python
import random

print(random.randint(0, 9))  # 隨機產生 0 到 9 的整數
print(random.randrange(1, 10))  # 隨機產生 1 到 9 的整數
```

## 猜數字遊戲
```python
import random

隨機數字 = random.randint(1, 100)  # 生成 1 到 100 之間的隨機數字
遊戲結束 = False

print("猜一個 1 到 100 之間的數字吧！")

while not 遊戲結束:
    猜測 = int(input("請輸入你的猜測："))
    if 猜測 < 1 or 猜測 > 100:
        print("請輸入正確的數字！")
    elif 猜測 < 隨機數字:
        print("大一點！再試一次。")
    elif 猜測 > 隨機數字:
        print("小一點！再試一次。")
    else:
        print("恭喜你，猜中了！")
        遊戲結束 = True
```

## 字典操作
### 讀取字典
```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
print(d["星期一"])  # 蘋果
```

### 建立與打印字典
```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
for key in d:
    print(key)
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(f"key={key}, value={value}")
```

### 新增/修改元素
```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
d["星期一"] = "橘子"
d["星期三"] = "蘋果"  # 新增元素, 當 key 不存在時會新增元素
print(d)
```

### 檢查 key 是否存在
```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
print("星期一" in d)  # True
print("星期三" in d)  # False
print("蘋果" in d.values())  # True
```

### 刪除元素
```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
d.pop("星期一")  # 刪除 key="星期一" 的元素
print(d)
```

## Streamlit
### 顯示圖片
```python
import streamlit as st
import os

st.title("圖片元件")
image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

image_size = st.number_input("圖片大小", min_value=50, step=50, value=100)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)
```
