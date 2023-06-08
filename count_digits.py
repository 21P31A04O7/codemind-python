b=int(input())
a=list(map(int,input().split()))
l,k=[],[]
for i in a:
    l.append(abs(i))
for j in l:
    k.append(str(j))
for p in k:
    print(len(p),end=' ')