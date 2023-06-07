n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
for i in l1:
    if i in l2 and i not in s:
        s.append(i)
for j in l2:
    if j in l1 and j not in s:
        s.append(j)
print(*s)