s=input()
t=set(s)
p='aeiou'
q='AEIOU'
l=0
for i in t:
    if i in p:
        l+=1
k=0
for i in t:
    if i in q:
        k+=1
if l==5 or k==5:
    print("True")
else:
    print("False")