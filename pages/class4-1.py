i = 0
while i < 10:  # 條件式迴圈,當 i < 5時執行迴圈
    print(i)
    i += 1  # i = i + 1

    # 算術指定運算式
    a = 10
    a += 1  # a = 等同於 a + 1
    a -= 1  # a = 等同於 a - 1
    a *= 2  # a = 等同於 a * 2
    a /= 2  # a = 等同於 a / 2
    a %= 2  # a = 等同於 a % 2
    a **= 2  # a = 等同於 a ** 2

# 跟據以上符號的優先順序
# 1.()
# 2.**
# 3./ // %
# 4.+ -
# 5.< > <= >= == !=
# 6.and or not

# break 跳出一層迴圈
i = 1
while i < 6:  # 條件式迴圈,當 i < 6時執行迴圈
    print(i)  # 印出 i
    i += 1
    if i == 3:
        break  # 當 i == 3 時，跳出迴圈
    i += 1

for i in range(1, 6):  # for 迴圈
    print(i)  # 印出 i
    if i == 3:
        break  # 當 i == 3 時，跳出迴圈


# random
import random  # 匯入 random 模組

print(random.randint(10))  # 隨機產生 0~9 的整數
print(random.random(1, 10))  # 隨機產生 1~9 的整數
print(random.random(1, 10, 2))  # 隨機產生 1~9 的奇數
# randrange跟range一樣, 第一個參數為開始數, 第二個參數為結束數, 第三個參數為間隔
# 不會數到結束的數字,randrange(1,10)只會從1~9隨機選一個數字

print(random.randrange(1, 10))  # 隨機產生 1~10 的整數
# randint跟range一樣,第一個參數為開始數,第二個參數為結束數
# 但randint一定要設定兩個數字,且會數到結束的數字
