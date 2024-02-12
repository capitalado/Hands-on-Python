#Twin primes in python
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    primes = []
    i = 2
    while i <= limit:
        if is_prime(i) and is_prime(i + 2):
            primes.append((i, i + 2))
        i += 1
    return primes

limit = 1000
twin_primes = find_twin_primes(limit)
for pair in twin_primes:
    print(pair[0] ,'and', pair[1],'are twin primes")