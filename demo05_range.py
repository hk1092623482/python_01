

for X in range(0,10,1):
    print(X)
print("===========")
for Y in range(1, 10, 2):
        print(Y)


lst1 = []
lst2 = [1,2,2.1,-1]
lst3 = ['asd','qwer','zxc']
print(lst1)
print(lst2)
for X in lst2:
    print("列表中的值:",X)

lst2.append('red')
print(lst2)
lst2.extend(lst3)
print(lst2)
lst2.reverse()
print(lst2)
# lst2.sort()
# print(lst3)
print(lst2.count(1))
print(lst2.index(1))
lst2.insert(2,'hello')
print(lst2)
lst4 = ['a','b','c','a']
print(lst4)
lst4.remove('a')
print(lst4)
lst5 = lst4.copy()
print(lst5)
lst5.clear()
print(lst5)