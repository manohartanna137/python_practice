lis=[2,5,5,5,6,1,8,9]
d={}
for i in lis:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
