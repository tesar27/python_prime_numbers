from sympy import isprime

res = []
def primeNumbers():
    global res
    for i in range(1,250):
        if i == 1: continue
        if i == 2 or i == 3: 
            res.append(i)
            continue
        if isprime(i): res.append(i)
        
    print(str(res))

primeNumbers()
with open("results.txt", "w", encoding="utf-8") as f:
    f.write("Primer Numbers between 1 and 250\n")
    for i in range(len(res)):
        f.write(str(res[i]) + '\n')