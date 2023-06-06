n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=[]
for i in l:
    if l.count(i)==k and i not in s:
        s.append(i)
if len(s)!=0:
    print(*s)
else:
    print("-1")