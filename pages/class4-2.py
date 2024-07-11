import random

隨機數字 = random.randint(1, 100)  # 生成一個1到100之間的隨機數字

# 設置一個標誌來表示遊戲是否結束
遊戲結束 = False

print("猜一個1到100之間的數字吧！")

while not 遊戲結束:
    # 讓使用者輸入一個數字
    猜測 = int(input("請輸入你的猜測："))
    if 猜測 < 1 or 猜測 > 100:  # 檢查猜測的數字
        print("請輸入正確的數字！")
    elif 猜測 < 隨機數字:
        print("大一點！再試一次。")
    elif 猜測 > 隨機數字:
        print("小一點！再試一次。")
    else:
        print("恭喜你，猜中了！")
        遊戲結束 = True
