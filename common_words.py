n=input().lower().split()
s=input().lower().split()
l=[]
for i in s:
    if i!=' '  and i in n:
        l.append(i)
print(*l)