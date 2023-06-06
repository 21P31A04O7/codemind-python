def is_happy_number(n):
    seen=set()
    while n!=1:
        n=sum(int(digit)**2 for digit in str(n))
        if n in seen:
            return False
        seen.add(n)
    return True
n=int(input())
is_happy=is_happy_number(n)
print(is_happy)