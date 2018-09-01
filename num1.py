l = list()
for i in range(1,21):
    l.append(i)
    if i%2 == 0:
        del l[i-1]
        l.append("apple")
    elif i%3 == 0:
        del l[i-1]
        l.append("banana")


print('apple'[:])