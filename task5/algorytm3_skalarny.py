a=[1,2,12,4]
b=[2,4,2,8]
n= len(a)
c=[0]*len(a)

for i in range (0,n):
    c[i]=a[i]*b[i]


c=sum(c)
print(c)
