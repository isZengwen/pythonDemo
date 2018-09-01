import random

li = []
for i in range(0,10):
    li.append(random.randint(0,99))
print("排序前：")
for i in li:
    print(i,end=",")

N: int = len(li)


print()
for i in range(0,N-1):
    for j in range(0,N-i-1):
        if li[j]> li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]
print("排序后：")
for i in li:
    print(i,end=",")


