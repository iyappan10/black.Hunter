n=int(input())
num=list(map(int,input().split()))
m=num[::-1]
print(*m,sep="->")
