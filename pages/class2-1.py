print(1 == 1)  # 這是比較是否相等運算
print(1 != 1)  # 這是比較是否不相等運算
print(1 > 1)  # 這是比較是否大於運算
print(1 < 1)  # 這是比較是否小於運算
print(1 >= 1)  # 這是比較是否大於或等於運算
print(1 <= 1)  # 這是比較是否小於或等於運算

print(not True)  # 這是相反運算
print(not False)  # 這是相反運算

print(True and True)  # 這是全部要符合才是True
print(True and False)  # 這是全部要符合才是True
print(False and True)  # 這是全部要符合才是True
print(False and False)  # 這是全部要符合才是True

print(True or True)  # 這是只要有其中一個符合就是True
print(True or False)  # 這是只要有其中一個符合就是True
print(False or True)  # 這是只要有其中一個符合就是True
print(False or False)  # 這是只要有其中一個符合就是True

# 符號的優先順序
# 1.()
# 2.**
# 3./ // %
# 4.+ -
# 5.< > <= >= == !=
# 6.and or not

pwd = input("請輸入密碼: ")
if pwd == "123456":
    print("密碼正確")
elif pwd == "12345678":
    print("密碼正確")
else:
    print("密碼錯誤")
# 判斷一定要if開頭, if只能有一個
# 判斷可以有無限多個elif, 也可以沒有
# 判斷可以有一個else, 也可以沒有
# elif和else是選擇性的
