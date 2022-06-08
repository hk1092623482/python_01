


class Students():

    name = ""
    grade = ""


    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade,self.name))


s1 = Students()
s1.grade = '5'
s1.name = '胡坤'
print(s1.study())

s2 = Students()
s2.name = '胡一刀'
s2.grade = '5'
print(s2.study())