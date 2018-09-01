#input的作用：
#1. 接受输入的内容并返回，返回值一定是字符串
#2.输出括号内的内容

def f(args):
    a = args.split(",")
    return a

s = "ssd,fa.s"
print(f(s))