


# 索引
lst = ['a','b','c','e','f','g']
print(lst[0])
print(lst[-1])
# 切片
print(lst[1:6]) # 获取第二个到第六个数
print(lst[0:6:2]) # 获取奇数位

alst = str(lst)
for x in alst:
    print(x)
print([x for x in range(1, 11) if x % 2])