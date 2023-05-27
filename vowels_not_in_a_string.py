s=input().lower()
p='aeiou'
l=[]
for i in p:
    if i not in s:
        l.append(i)
if len(l)==0:
    print('0')
else:
    print(*l)