n,m=map(int,input().split())
num=list(map(int,input().split()))
mum=list(map(int,input().split()))
sum=0
for i in range(len(num)):
    for j in range(len(mum)):
         if(mum[j]==num[i]):
             sum=sum+1
if(sum==n-1):
    print('YES')
else:
    print('NO')
