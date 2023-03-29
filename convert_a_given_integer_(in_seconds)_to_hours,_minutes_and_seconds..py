s=int(input())
h=s//3600
s=s-h*3600
m=s//60
s=s-m*60
print('H:M:S-%d:%d:%d'%(h,m,s))
