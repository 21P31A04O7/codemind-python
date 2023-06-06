n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if l.count(i)==i and i not in s:
        s.append(i)
if len(s)!=0:
    k=sum(s)/len(s)
    print("%.2f"%k)
else:
    print("-1")
    