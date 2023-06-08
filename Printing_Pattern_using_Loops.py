n=int(input())
l=n*2-1
for i in range(l):
    for j in range(l):
        if i<j:
            m=i
        else:
            m=j
        if m<l-i:
            m=m
        else:
            m=l-i-1
        if m<l-j-1:
            m=m
        else:
            m=l-j-1
        print(n-m,end=' ')
    print()