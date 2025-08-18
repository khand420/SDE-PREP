def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if  num % i == 0:
            return False
    return True    
        


def gen(num):
    for i in range(num):
        if is_prime(i):
            yield i
    
obj = gen(35)
for prime in obj:
    print(prime)      