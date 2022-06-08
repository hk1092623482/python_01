

def ads(x,y):
    z = x + y
    return z
print(ads(2,3))
print(ads('2','a'))


def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info
print(study_language("胡坤"))


def add(x,y,*args):
    print(args)
    z = x + y + sum(args)
    return z
print(add(1,2,3,4,5,6,7))
print(add(1,2,*[3,4,5,6,7]))