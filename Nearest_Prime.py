def is_prime(number):
    if number<2:
        return False
    for i in range(2,int(number//2)+1):
        if number%i==0:
            return 0
    return 1
def nearest_prime(number):
    smaller=number-1
    greater=number+1
    while True:
        if is_prime(smaller):
            return smaller
        elif is_prime(greater):
            return greater
        smaller-=1
        greater+=1
n=int(input())
for _ in range(n):
    num=int(input())
    if is_prime(num):
        print(num)
    else:
        nearest=nearest_prime(num)
        print(nearest)