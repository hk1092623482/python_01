

# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
# a = input('请输入一个整数')
# b = input('请输入一个整数')
# c = input('请输入一个整数')
# d = input('请输入一个整数')
# print(int(a) + int(b) - int(c) * int(d))
# 2. 打印1~100内被3整除的所有数的和 。
sum = 0
for x in range(1,101):
    if x % 3 == 0:
        sum += x
    x += 1
print(sum)
# 3. 使用range()输出1~10内的所有奇数 。
for x in range(1,11,2):
    print(x)
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
for x in range(1,101):
    if x % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1 - sum2)
# 5. 求1+2+3+...+100的和
sum3 = 0
for x in range(1,101):
    sum3 += x
    x += 1
print(sum3)
# 6. 判断一个数n能同时被3和5整除
# n = input('请输入一个整数')
# if int(n) % 3 == 0 and int(n) % 5 ==0:
#     print("能")
# else:
#     print('不能')
# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
# x1 = input("请输入一个整数")
# if 1 <= int(x1) <= 100:
#     print(x1)
# else:
#     print('不是')
# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
lst = []
x = input('请输入一个数')
y = input('请输入一个数')
z = input('请输入一个数')
lst.append(int(x))
lst.append(int(y))
lst.append(int(z))
print(lst)
lst.sort()
print(lst)
# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，

# 60分以下的用C表示。备注：需要使用input()方法
# 10. 将一个列表的数据复制到另一个列表中。
# 11. 输出 9*9 乘法口诀表。