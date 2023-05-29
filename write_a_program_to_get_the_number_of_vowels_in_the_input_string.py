n=input()
c=0
vowel='aeiouAEIOU'
for i in n:
    if i in vowel:
        c+=1
print(c)