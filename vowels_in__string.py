s=input()
p='aeiouAEIOU'
l=[]
for i in s:
    if i in p and i not in l:
        l.append(i)
print(*l)