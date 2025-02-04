def monte(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i], l[i+1]=l[i+1], l[i]
            print(l)
monte([12,5,13,8,11,6])