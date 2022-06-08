



def div(x,y):
    try:
        z = x / y
        return z
    except Exception as e:
        print("除法不能出现被0除的情况")
        print(e)

print(div(5,6))
print(div(6,0))
print(div(5,5))