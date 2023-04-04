u=float(input())
if u<200:
    c=1.20
elif u>=200 and u<400:
    c=1.50
elif u>=400 and u<600:
    c=1.80
else:
    c=2.00
b=u*c
if b<400:
    s=100
else:
    s=0.15*b
tb=b+s
print("%.2f"%tb)
