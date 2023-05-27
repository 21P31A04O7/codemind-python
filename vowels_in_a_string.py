n=input()
p=str(n)
m=input()
s=str(m)
if s in p:
    print("True")
    print(p.index(s))
else:
    print("False")