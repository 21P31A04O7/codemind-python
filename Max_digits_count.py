n=int(input())
l=list(map(int,input().split()))
a,a1=[],[]
for j in l:
    a.append(len(str(j)))
for k in range(n):
    if a[k]==max(a):
        a1.append(a)
print(len(a1))
    