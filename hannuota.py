def move(n,A,B,C):
    if n ==1:
        return "{0}->{1}".format(A,C)
    else:
        return move(n-1,A,C,B)+"\n"+"{0}->{1}".format(A,C)+"\n"+move(n-1,B,A,C)

print(move(5,"A","B","C"))

