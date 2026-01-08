upUntilValue = 0

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

def writeIntoFile(fileName, res):
    with open(fileName, "w", encoding="utf-8") as f:
        f.write(f"Primer Numbers between 1 and {upUntilValue}\n")
        for i in range(len(res)):
            if i == len(res) - 1: 
                f.write(str(res[i]) + '\n')
            else:
                f.write(str(res[i]) + ',')

if __name__ == '__main__':
    print('Welcome to the prime numbers calculator up to your given number! :)')
    numberInput = int(input('Now give your desired limit, until which we calculate all the primer numbers: '))
    fileNameInput = input('Now give the file name (with extension) you want to save the results in: ')
    print(f'*** Printing primer number within the range 1 to {numberInput} ***')
    res = []
    res = calc_primes(numberInput)
    upUntilValue = numberInput
    writeIntoFile(fileNameInput, res)
    print('*** Finished writing into the file ***')
    print(res)