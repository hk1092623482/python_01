

# 连接字符串 ： join(seq)
astr = '+'
bstr = astr.join('hello')
print(bstr)

# 分割字符串 ： split(str=""),其中str代表分割符
cstr = "wo de lian ling 28"
dstr = cstr.split(' ')
print(dstr)

fstr = "abcdef ghopq"
print(len(fstr))
gstr = fstr.replace('abcdef','qwer')
print(gstr)

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
sum = "sasasd 5511 2155 /..,/,/,;.asd"
zf = 0
kg = 0
sz = 0
qt = 0
for x in sum:
    if x.isalpha():   # 判断字符
        zf += 1
    elif x.isdigit():  # 判断数字
        sz += 1
    elif x.isspace():  # 判断空格
        kg += 1
    else:
        qt += 1
print("字符：",zf)
print("数字：",sz)
print("空格：",kg)
print("其他：",qt)


