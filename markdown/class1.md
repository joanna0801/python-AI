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
