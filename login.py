
for i in range(1,4):
    username = input("请输入用户名：")
    password = input("请输入密码：")

    if username == "seven" and password == "1234":
        print("登录成功")
        break
    else:
        print("密码输入错误，还有{}次机会".format(3-i))