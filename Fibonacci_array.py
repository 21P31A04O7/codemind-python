n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if lst[i]!=lst[i+1]-lst[i-1]:
        c=c+1
if c==0 and lst[n-1]==lst[n-2]+lst[n-3]:
    print("yes")
else:
    print("no")