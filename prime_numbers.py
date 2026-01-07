from sympy import isprime

res = []

def calc_primes(n):
    if n < 2:
        return False
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
                
    primes_only = []
    for i in range(len(sieve)):
        if sieve[i] == True:
            primes_only.append(i)

    return primes_only

res = calc_primes(250)

with open("results.txt", "w", encoding="utf-8") as f:
    f.write("Primer Numbers between 1 and 250\n")
    for i in range(len(res)):
        f.write(str(res[i]) + '\n')