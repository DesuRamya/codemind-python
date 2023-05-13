n=int(input())
for i in range(n):
    for j in range(n):
        if i==j:
            print("x",end='')
        elif j+1==n-i:
            print("x",end='')
        else:
            print("0",end='')
    print( )