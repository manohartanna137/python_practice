n=int(input())
a=0
b=1
print(a,b,end=" ")
for i in range(2,n):
    d=a+b
    print(d,end=" ")
    a=b
    b=d

