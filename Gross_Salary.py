
bs=int(input())
if bs<=10000:
    gs=bs+(0.8*bs)+(0.2*bs)
elif bs<=20000:
    gs=bs+(0.9*bs)+(0.25*bs)
else:
    gs=bs+(0.95*bs)+(0.3*bs)
print('%0.2f'%gs)