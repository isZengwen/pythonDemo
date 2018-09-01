names=' Kunpen Ji, Li XIAO, Caron Li, Donl SHI, Ji ZHAO, Fia YUAN Y, Weue DING, Xiu XU, Haiying WANG, Hai LIN, Jey JIANG, Joson WANG E, Aiyang ZHANG, Hay MENG, Jak ZHANG E, Chang Zhang, Coro ZHANG'



def count(*args):
    count = 0
    for i in args:
        if "Zhang" in i.split():
            count += 1
        if "ZHANG" in i.split():
            count += 1
    return count


def paixu(args):
    result = args.split(",")
    result.sort()
    return result


def pick(args):
    ls = args.split(",")
    length = 0
    for items in ls:

        if len(items) > length:
            length = len(items)
            result = items
    return result



"""
print("排序后的列表为：")
print(paixu(names))
print("Zhang姓有：{0}个".format(count(*paixu(names))))
"""

print(pick(names))