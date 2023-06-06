n=int(input())
s=[]
p=[]
l=list(map(int,input().split()))
for i in l:
    if i%2!=0:
        s.append(i)
    if i%2==0:
        p.append(i)
new=s+p
for j in new:
    print(j,end=" ")