n=int(input())
arr=list(map(int,input().split()))
l=[]
k=[]
for i in arr:
    if i%2==0:
        l.append(i)
    else:
        k.append(i)
new=l+k
for j in new:
    print(j,end=" ")
        