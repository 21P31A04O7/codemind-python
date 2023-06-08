s=input().split()
lst=[]
for i in s:
    if s.index(i)%2==0:
        lst.append(i[::-1])
    else:
        lst.append(i)
print(*lst)