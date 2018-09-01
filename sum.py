n = 2
sum = 0
while n != 100:
    if n % 2 == 0:
        sum += n
    else:
        sum -= n
    n += 1
#print(sum)
for item in [i for i in range(1,101) if i%2!=0]:
    print(item)