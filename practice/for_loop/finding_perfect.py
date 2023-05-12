
n=int(input())
sum_=0
for i in range(1,n):
  if n%i == 0:
    sum_=sum_+i
if sum_==n:
    print('perfect')
else:
  print('not perfect')
