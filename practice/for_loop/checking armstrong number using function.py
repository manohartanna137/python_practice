def armstrong_number(num):
    num_copy=num
    out=0
    while num>0:
        rem=num%10
        out=out+(rem**3)
        num=num//10
    if num_copy==out:
        return 1
    else:
        return 0
armstrong_list=[]
armstrong_not=[]
for i in range(1,1001):
    if (armstrong_number(i) == 1):
        armstrong_list.append(i)
    else:
        armstrong_not.append(i)
print(armstrong_list)
print(armstrong_not)


