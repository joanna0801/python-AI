L = [3, 12, 7, 9, 5, 3, 3, 3, 2, 4]

L.append(8)
print(L)

c = L.count(3)
for i in range(c):
    L.remove(3)

print(L)


L.pop(0)
print(L)
# pop 與 remove 的差別, pop 是用remove 是用元素來刪除

L.sort()
print(L)
L.sort(reverse=True)
print(L)

print(L.index(5))
