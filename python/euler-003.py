import math

def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, n):
        if (n%i == 0):
            return False
    return True

rest = 600851475143
# rest = 1000000000

# define limit for primes
limit = int(math.sqrt(rest))
# limit = rest

primes = []
primes.append(2)

factors = []

# get all primes within the limit
for i in range(0, limit):
    if (isPrime(i*2+1)):
        primes.append(i*2+1)

# do the prime factorization
index = 0
while (index < len(primes)) & (rest != 0):
    if (rest%primes[index] == 0):
        rest = int(rest/primes[index])
        factors.append(primes[index])
        # index = 0
    else:
        index += 1

print("factors:" + str(factors))
