n=int(input())
l=list(map(int,input().split()))
a,a1=[],[]
for j in l:
    a.append(len(str(j)))
for k in range(n):
    if a[k]==min(a):
        a1.append(l[k])
print(len(a1))