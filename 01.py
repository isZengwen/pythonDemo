#定义一个类
class Student():
    pass

# 定义一个对象

mingyue = Student()

# 再定义一个类
class PythonStudent():
    name = None
    age = 18
    course = "python"

    def doHomework(self):
        print("doing")
        return None



yueyue = PythonStudent()#实例化
print(yueyue.name)
yueyue.doHomework()